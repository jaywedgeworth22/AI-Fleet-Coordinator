#!/usr/bin/env python3
"""Build a day-by-day fleet activity digest: Markdown, HTML, and all-day ICS.

Sources (GitHub API + effort-log files when present):
  - Merged pull requests
  - Issues opened / closed / reopened
  - Effort-board bullets from each repo's docs/EFFORT-LOG.md (and live-style
    names when mirrored under docs/)

Outputs (under site/ and calendar/):
  site/index.html          — browsable day outline
  site/digest.md           — same content as Markdown
  calendar/daily-digest.ics — one all-day VEVENT per day (subscribe in Apple/Google)

Env:
  GITHUB_TOKEN / FLEET_GITHUB_TOKEN
  FLEET_OWNER (default jaywedgeworth22)
  FLEET_REPOS (comma list)
  DIGEST_LOOKBACK_DAYS (default 21)
  DIGEST_TZ (default America/Chicago)  — day bucketing only
  SITE_OUT (default site)
  ICS_OUT (default calendar/daily-digest.ics)
  SITE_BASE_URL (optional, e.g. https://jaywedgeworth22.github.io/ai-fleet-coordinator/)
  EFFORT_LOG_DIR (optional local dir of live boards, e.g. /Users/jay/apps)
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

# Allow `python3 scripts/build-fleet-daily-digest.py` from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ics_utils import ics_escape, join_ics  # noqa: E402

DEFAULT_REPOS = [
    "Socratic.Trade",
    "Congress.Trade",
    "Usage-Monitor",
    "congress-trading-shared",
    "DealDex",
    "Personal-Site",
    "Autorotate",
    "ContactLogo",
    "ai-fleet-coordinator",
    "BotFleet",
    "HogHunter",
    "fleet-ops",
]

# Live machine boards (optional local override via EFFORT_LOG_DIR)
LIVE_EFFORT_FILES = {
    "Usage-Monitor": "API-USAGE-MONITOR-EFFORT-LOG.md",
    "Socratic.Trade": "SOCRATIC-TRADE-EFFORT-LOG.md",
    "Congress.Trade": "CONGRESS-TRADE-EFFORT-LOG.md",
    "congress-trading-shared": "CONGRESS-SHARED-EFFORT-LOG.md",
    "DealDex": "DEALDEX-EFFORT-LOG.md",
    "Personal-Site": "PERSONAL-SITE-EFFORT-LOG.md",
    "Autorotate": "AUTOROTATE-EFFORT-LOG.md",
    "ContactLogo": "CONTACTLOGO-EFFORT-LOG.md",
    "ai-fleet-coordinator": "FLEET-INFRA-EFFORT-LOG.md",
    "BotFleet": "BOTFLEET-EFFORT-LOG.md",
    "HogHunter": "HOGHUNTER-EFFORT-LOG.md",
    "fleet-ops": "FLEET-OPS-EFFORT-LOG.md",
}

DONE_SECTIONS = frozenset(
    {
        "deployed",
        "completed",
        "done",
        "shipped",
        "closed",
        "complete",
    }
)
ACTIVE_SECTIONS = frozenset(
    {
        "in progress",
        "progress",
        "blocked",
        "waiting",
        "planned",
    }
)


@dataclass
class DayBucket:
    day: date
    merged_prs: list[dict[str, Any]] = field(default_factory=list)
    issues_opened: list[dict[str, Any]] = field(default_factory=list)
    issues_closed: list[dict[str, Any]] = field(default_factory=list)
    effort_lines: list[dict[str, str]] = field(default_factory=list)

    def is_empty(self) -> bool:
        return not (
            self.merged_prs
            or self.issues_opened
            or self.issues_closed
            or self.effort_lines
        )

    def counts_line(self) -> str:
        return (
            f"{len(self.merged_prs)} PRs merged · "
            f"{len(self.issues_opened)} issues opened · "
            f"{len(self.issues_closed)} issues closed · "
            f"{len(self.effort_lines)} effort rows"
        )


def env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    return int(raw) if raw else default


def token() -> str:
    t = (
        os.environ.get("FLEET_GITHUB_TOKEN", "").strip()
        or os.environ.get("GITHUB_TOKEN", "").strip()
    )
    if not t:
        raise SystemExit("error: set GITHUB_TOKEN or FLEET_GITHUB_TOKEN")
    return t


def gh_get(url: str, tok: str) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {tok}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ai-fleet-coordinator-daily-digest",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gh_get_text(url: str, tok: str) -> str | None:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github.raw",
            "Authorization": f"Bearer {tok}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ai-fleet-coordinator-daily-digest",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"warn: GET {url} HTTP {e.code}: {body}", file=sys.stderr)
        return None
    except Exception as e:  # noqa: BLE001
        print(f"warn: GET {url} failed: {e}", file=sys.stderr)
        return None


def gh_list(url: str, tok: str, max_pages: int = 8) -> list[dict[str, Any]]:
    """Paginate a GitHub list endpoint (Link headers optional; stop on short page)."""
    items: list[dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        sep = "&" if "?" in url else "?"
        page_url = f"{url}{sep}page={page}&per_page=100"
        try:
            data = gh_get(page_url, tok)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            print(f"warn: list HTTP {e.code}: {body}", file=sys.stderr)
            break
        except Exception as e:  # noqa: BLE001
            print(f"warn: list failed: {e}", file=sys.stderr)
            break
        if not isinstance(data, list):
            break
        items.extend(data)
        if len(data) < 100:
            break
    return items


def parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def to_local_day(dt: datetime, tz: ZoneInfo) -> date:
    return dt.astimezone(tz).date()


def fetch_merged_prs(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> list[tuple[date, dict[str, Any]]]:
    """List closed PRs via REST (avoids Search API secondary rate limits)."""
    out: list[tuple[date, dict[str, Any]]] = []
    since_dt = datetime.combine(since, datetime.min.time(), tzinfo=tz)
    for repo in repos:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/pulls"
            f"?state=closed&sort=updated&direction=desc"
        )
        for it in gh_list(url, tok, max_pages=10):
            merged = parse_iso(it.get("merged_at"))
            if not merged:
                continue
            if merged < since_dt.astimezone(timezone.utc) and to_local_day(merged, tz) < since:
                # list is updated-desc; once we are well before since on updated_at, stop
                updated = parse_iso(it.get("updated_at"))
                if updated and to_local_day(updated, tz) < since:
                    break
                continue
            if to_local_day(merged, tz) < since:
                continue
            out.append(
                (
                    to_local_day(merged, tz),
                    {
                        "repo": repo,
                        "number": it.get("number"),
                        "title": (it.get("title") or "").strip(),
                        "url": it.get("html_url") or "",
                        "user": ((it.get("user") or {}).get("login") or ""),
                        "when": merged,
                    },
                )
            )
    return out


def fetch_issue_churn(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> tuple[list[tuple[date, dict[str, Any]]], list[tuple[date, dict[str, Any]]]]:
    """List issues via REST since= (created/updated filter); bucket by created/closed day."""
    opened: list[tuple[date, dict[str, Any]]] = []
    closed: list[tuple[date, dict[str, Any]]] = []
    since_iso = datetime.combine(since, datetime.min.time(), tzinfo=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    for repo in repos:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/issues"
            f"?state=all&since={since_iso}&sort=updated&direction=desc"
        )
        for it in gh_list(url, tok, max_pages=10):
            if it.get("pull_request"):
                continue
            created = parse_iso(it.get("created_at"))
            closed_at = parse_iso(it.get("closed_at"))
            base = {
                "repo": repo,
                "number": it.get("number"),
                "title": (it.get("title") or "").strip(),
                "url": it.get("html_url") or "",
                "state": it.get("state") or "",
            }
            if created and to_local_day(created, tz) >= since:
                opened.append(
                    (to_local_day(created, tz), {**base, "when": created})
                )
            if closed_at and to_local_day(closed_at, tz) >= since:
                closed.append(
                    (to_local_day(closed_at, tz), {**base, "when": closed_at})
                )
    return opened, closed


_DATE_IN_LINE = re.compile(
    r"(20\d{2}-\d{2}-\d{2})|"
    r"(20\d{2}/\d{2}/\d{2})|"
    r"\b(20\d{2}-\d{2}-\d{2}T)"
)
_BULLET = re.compile(r"^\s*-\s+")
_HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*$")
_STATUS_WORDS = (
    "merged",
    "complete",
    "completed",
    "deployed",
    "done",
    "shipped",
    "live",
    "closed",
    "in pr",
    "progress",
    "host done",
    "live verified",
)


def parse_effort_log(text: str, repo: str, since: date, tz: ZoneInfo) -> list[tuple[date, dict[str, str]]]:
    """Heuristic: board bullets under Deployed/Completed (and active WIP with status words)."""
    rows: list[tuple[date, dict[str, str]]] = []
    today = datetime.now(tz).date()
    section = ""
    for line in text.splitlines():
        hm = _HEADING.match(line)
        if hm:
            section = hm.group(1).strip().lower()
            continue
        if not _BULLET.match(line):
            continue
        if line.lstrip().startswith("- _") or "board closeout" in line.lower():
            continue
        low = line.lower()
        in_done = any(s in section for s in DONE_SECTIONS)
        in_active = any(s in section for s in ACTIVE_SECTIONS)
        has_status = any(k in low for k in _STATUS_WORDS)
        if in_done:
            pass
        elif in_active and has_status:
            pass
        elif not section and has_status:
            pass
        else:
            continue
        body = re.sub(r"^\s*-\s+", "", line).strip()
        if len(body) < 20:
            continue
        day = today
        # Search for date in line. Prefer completion/status date (e.g. COMPLETED ... 2026-08-22) or start-of-line date.
        # Ensure we never pick a future date mentioned in prose.
        status_date_m = re.search(
            r"(?:COMPLETED|DEPLOYED|MERGED|IN PROGRESS|IN PR|CLAIMED|DONE)[^\n\r]*?\b(20\d{2}[-/]\d{2}[-/]\d{2})",
            body,
            re.IGNORECASE,
        )
        if status_date_m:
            raw = status_date_m.group(1).replace("/", "-")
            try:
                d_cand = date.fromisoformat(raw)
                if d_cand <= today:
                    day = d_cand
            except ValueError:
                pass
        else:
            # Fallback: scan all dates in line, pick the first one that is <= today and >= since
            for m in _DATE_IN_LINE.finditer(body):
                raw = (m.group(1) or m.group(2) or "")[:10].replace("/", "-")
                try:
                    d_cand = date.fromisoformat(raw)
                    if d_cand <= today:
                        day = d_cand
                        break
                except ValueError:
                    pass
        if day < since or day > today:
            continue
        prefix = ""
        if in_done:
            prefix = "[done] "
        elif in_active:
            prefix = "[wip] "
        rows.append(
            (
                day,
                {
                    "repo": repo,
                    "text": (prefix + body)[:400],
                    "section": section or "unknown",
                },
            )
        )
    if len(rows) > 120:
        rows = sorted(rows, key=lambda r: r[0], reverse=True)[:120]
    return rows


def fetch_effort_rows(
    owner: str, repos: list[str], since: date, tok: str, tz: ZoneInfo
) -> list[tuple[date, dict[str, str]]]:
    """Fetch live effort board markdown from each repo; parse bullets."""
    out: list[tuple[date, dict[str, str]]] = []
    for repo in repos:
        text = None
        source = repo
        # Local workspace checkout first (for live/uncommitted effort boards during runs)
        local_effort = Path.home() / "apps" / f"{repo.lower()}-effort.md"
        if not local_effort.is_file():
            # Try alternate local workspace paths
            local_effort = Path.home() / "Code" / repo / "docs" / "EFFORT-LOG.md"
        if local_effort.is_file():
            try:
                text = local_effort.read_text(encoding="utf-8")
                source = str(local_effort)
            except Exception:  # noqa: BLE001
                text = None
        if text is None:
            for path in ("docs/EFFORT-LOG.md", "EFFORT-LOG.md"):
                url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
                text = gh_get_text(url, tok)
                if text:
                    source = f"{repo}/{path}"
                    break
        if text:
            rows = parse_effort_log(text, repo, since, tz)
            print(f"  effort {source}: {len(rows)} bullets")
            out.extend(rows)
        else:
            print(f"  effort {repo}: (none found)")
    return out


def bucket_all(
    prs: list[tuple[date, dict[str, Any]]],
    opened: list[tuple[date, dict[str, Any]]],
    closed: list[tuple[date, dict[str, Any]]],
    effort: list[tuple[date, dict[str, str]]],
) -> dict[date, DayBucket]:
    buckets: dict[date, DayBucket] = {}

    def b(d: date) -> DayBucket:
        if d not in buckets:
            buckets[d] = DayBucket(day=d)
        return buckets[d]

    for d, item in prs:
        b(d).merged_prs.append(item)
    for d, item in opened:
        b(d).issues_opened.append(item)
    for d, item in closed:
        b(d).issues_closed.append(item)
    for d, item in effort:
        b(d).effort_lines.append(item)

    for day in buckets.values():
        day.merged_prs.sort(key=lambda x: (x["repo"], x.get("number") or 0))
        day.issues_opened.sort(key=lambda x: (x["repo"], x.get("number") or 0))
        day.issues_closed.sort(key=lambda x: (x["repo"], x.get("number") or 0))
    return buckets


def day_summary_title(day: DayBucket) -> str:
    n = len(day.merged_prs)
    o = len(day.issues_opened)
    c = len(day.issues_closed)
    return f"Fleet: {n} merged · {o} opened · {c} closed"


# Short badge label + CSS class for each fleet repo
REPO_BADGE: dict[str, tuple[str, str]] = {
    "Socratic.Trade": ("ST", "repo-st"),
    "Congress.Trade": ("CT", "repo-ct"),
    "Usage-Monitor": ("UM", "repo-um"),
    "congress-trading-shared": ("CTS", "repo-shared"),
    "DealDex": ("DD", "repo-dd"),
    "Personal-Site": ("PS", "repo-ps"),
    "Autorotate": ("AR", "repo-ar"),
    "ContactLogo": ("CL", "repo-cl"),
    "ai-fleet-coordinator": ("AFC", "repo-fleet"),
    "BotFleet": ("BF", "repo-bf"),
    "fleet-ops": ("OPS", "repo-ops"),
}

# Latest product app icons (copied into site/agent-logos/ with agent marks)
REPO_APP_ICON: dict[str, str] = {
    "Socratic.Trade": "agent-logos/app-st.svg",  # offset ST logo
    "Congress.Trade": "agent-logos/app-ct.png",  # latest CT iOS app icon
    "Usage-Monitor": "agent-logos/app-um.png",   # latest Usage Monitor client icon
    "DealDex": "agent-logos/app-dd.png",         # DealDex favicon (card/ask mark)
    "Autorotate": "agent-logos/app-ar.png",      # Autorotate shield/lock icon
    "ContactLogo": "agent-logos/app-cl.png",     # ContactLogo crest mark
    "Personal-Site": "agent-logos/app-ps.png",   # Jay's headshot for jays.services
    "BotFleet": "agent-logos/app-bf.png",        # BotFleet app icon
}

# Aliases used only to strip *redundant leading* labels that duplicate the badge.
# Mid-title mentions and other-repo names are left alone.
REPO_STRIP_ALIASES: dict[str, tuple[str, ...]] = {
    "Socratic.Trade": (
        "Socratic.Trade",
        "Socratic.Trade.com",
        "socratic.trade",
        "Socratic-Trade",
        "socratic-trade",
        "Socratic Trade",
        "API-Socratic",  # rare
        "ST",
    ),
    "Congress.Trade": (
        "Congress.Trade",
        "congress.trade",
        "Congress-Trade",
        "congress-trade",
        "Congress Trade",
        "CT",
    ),
    "Usage-Monitor": (
        "Usage-Monitor",
        "Usage Monitor",
        "usage-monitor",
        "API-usage-monitor",
        "API-usage-Monitor",
        "api-usage-monitor",
        "AUM",
        "UM",
    ),
    "congress-trading-shared": (
        "congress-trading-shared",
        "Congress-trading-shared",
        "congress-shared",
        "shared dependency",
        "shared",
        "CTS",
    ),
    "DealDex": (
        "DealDex.net",
        "DealDex",
        "dealdex",
        "Deal Dex",
        "DD",
    ),
    "Personal-Site": (
        "Personal-Site",
        "personal-site",
        "Personal Site",
        "PS",
        "jays.services",
    ),
    "Autorotate": (
        "Autorotate.Codes",
        "Autorotate",
        "autorotate",
        "AR",
    ),
    "ContactLogo": (
        "ContactLogo",
        "contactlogo",
        "ContactLogo.com",
        "contact-logo",
        "CL",
    ),
    "ai-fleet-coordinator": (
        "AI Fleet Coordinator",
        "ai-fleet-coordinator",
        "fleet-coordinator",
        "fleet-infra",
        "fleet",
        "AFC",
        "AFC",
    ),
    "BotFleet": (
        "BotFleet.app",
        "BotFleet",
        "botfleet",
        "BF",
    ),
    "fleet-ops": (
        "Fleet Ops",
        "fleet-ops",
        "OPS",
    ),
}


def repo_badge(repo: str) -> tuple[str, str]:
    """Return (short_label, css_class)."""
    if repo in REPO_BADGE:
        return REPO_BADGE[repo]
    # fallback: slug
    slug = re.sub(r"[^a-z0-9]+", "-", repo.lower()).strip("-") or "repo"
    return (repo, f"repo-{slug}")


def _alias_pattern(aliases: tuple[str, ...]) -> re.Pattern[str]:
    # Longest first so "Socratic.Trade" wins over "ST"
    parts = sorted(aliases, key=len, reverse=True)
    escaped = [re.escape(a) for a in parts]
    return re.compile("|".join(escaped), re.IGNORECASE)


def strip_redundant_repo_label(text: str, repo: str) -> str:
    """Remove leading repo labels that only repeat the badge (not mid-title focus).

    Strips forms like:
      [Socratic.Trade][CODEX] foo  →  [CODEX] foo
      [Socratic.Trade] foo         →  foo
      Socratic.Trade: foo          →  foo
      (Usage-Monitor) foo          →  foo

    Leaves mid-string names, other-repo names, and short titles where the repo
    *is* the subject (nothing left to show after strip would keep original).
    """
    if not text or not repo:
        return text
    aliases = REPO_STRIP_ALIASES.get(repo)
    if not aliases:
        aliases = (repo,)
    alias_re = _alias_pattern(aliases)
    original = text
    s = text.strip()

    # Repeat: multiple leading [Repo] / (Repo) / Repo: tokens
    changed = True
    while changed:
        changed = False
        # [Repo] or [Repo/sub] at start
        m = re.match(r"^\[([^\]]+)\]\s*", s)
        if m and alias_re.fullmatch(m.group(1).strip()):
            s = s[m.end() :].lstrip(" :-–—|/")
            changed = True
            continue
        # (Repo)
        m = re.match(r"^\(([^)]+)\)\s*", s)
        if m and alias_re.fullmatch(m.group(1).strip()):
            s = s[m.end() :].lstrip(" :-–—|/")
            changed = True
            continue
        # bare Repo: or Repo -
        m = re.match(r"^(" + alias_re.pattern + r")\s*[:\-–—|/]\s*", s, re.IGNORECASE)
        if m:
            s = s[m.end() :].lstrip()
            changed = True
            continue
        # bare Repo followed by whitespace then non-empty rest (not the whole title)
        m = re.match(r"^(" + alias_re.pattern + r")\s+", s, re.IGNORECASE)
        if m and len(s) > m.end() + 3:
            # only if what follows looks like a real title (not just a date)
            rest = s[m.end() :]
            if rest and not re.match(r"^\d{4}-\d{2}-\d{2}\s*$", rest):
                s = rest
                changed = True
                continue

    s = re.sub(r"\s{2,}", " ", s).strip(" :-–—|/")
    # If strip ate everything, keep original (repo *is* the title focus)
    if len(s) < 4:
        return original
    return s


# Agent seat tags → logo slug + human label (logo files in agent-logos/<slug>.svg)
AGENT_LOGO: dict[str, tuple[str, str]] = {
    "grok": ("grok", "Grok"),
    "codex": ("codex", "Codex"),
    "claude": ("claude", "Claude"),
    "cursor": ("cursor", "Cursor"),
    "ag": ("ag", "Antigravity"),
    "antigravity": ("ag", "Antigravity"),
    "gemini": ("gemini", "Gemini"),
    "minimax": ("minimax", "MiniMax"),
    "mm": ("minimax", "MiniMax"),
    "sentry": ("sentry", "Sentry"),
    # Monet / Renoir / Fable seats collapse to Claude logo + label
    "monet": ("claude", "Claude"),
    "renoir": ("claude", "Claude"),
    "fable": ("claude", "Claude"),
    # owner/Jay signature lives at agent-logos/owner.svg for future use, but is
    # intentionally NOT a digest chip: OWNER tags mean human follow-up, not a
    # coding seat, and must not look like "Jay did this alone".
}

# Core seat names; optional version/wave suffixes: GROK4, GROK3-B7, CODEX-REVIEW
# OWNER is deliberately omitted — keep "OWNER ACTION" text, no person/Jay chip.
_AGENT_ALT = (
    r"GROK\d*(?:-[A-Za-z0-9]+)?"
    r"|CODEX(?:-[A-Za-z0-9]+)?"
    r"|CLAUDE(?:\s+CODE)?"
    r"|CURSOR"
    r"|MINIMAX|MM"
    r"|SENTRY"
    r"|AG|ANTIGRAVITY|GEMINI|MONET|RENOIR|FABLE"
)
# One or more slash-separated seat tokens (CURSOR/AG, Codex/Claude/Monet/AG/Cursor)
_AGENT_CHAIN = rf"(?:{_AGENT_ALT})(?:\s*/\s*(?:{_AGENT_ALT}))*"
# Match [GROK], [AG], [CURSOR/AG], [CODEX/AG], [Claude Code], etc.
_AGENT_BRACKET = re.compile(rf"\[({_AGENT_CHAIN})\]", re.IGNORECASE)
_AGENT_BARE_PREFIX = re.compile(
    rf"^(?:by\s+)?({_AGENT_ALT})\b[,:\s\-–—]*",
    re.IGNORECASE,
)
# Issue titles: "2026-08-03 — GROK — COMPLETED …"
_AGENT_EMDASH = re.compile(
    rf"(?:\s*[\-–—]\s*|\s+)({_AGENT_ALT})(?:\s*[\-–—]\s*|\s+)",
    re.IGNORECASE,
)
# Effort trailers: (CODEX/HERSCHEL, L) or (CODEX-REVIEW, S) or truncated (CODEX...
# Also multi-seat: (CODEX/AG, L)
_AGENT_PAREN = re.compile(
    rf"\(({_AGENT_CHAIN})(?:/[^),]*)?(?:,[^)]*)?(?:\)|\.\.\.|$)",
    re.IGNORECASE,
)
# Slash chains outside brackets: "Post-Codex/AG consolidation", "Codex/Claude/AG"
# Requires ≥2 seat tokens so lone path segments (ag/client) stay intact.
_AGENT_SLASH_CHAIN = re.compile(
    rf"(?<![A-Za-z0-9_])((?:{_AGENT_ALT})(?:\s*/\s*(?:{_AGENT_ALT}))+)(?![A-Za-z0-9_/])",
    re.IGNORECASE,
)
# Standalone seat words. Allow trailing punctuation (AG... / AG.) but not path
# continuations (ag/client, .codex/). Lookbehind blocks mid-identifier matches.
_AGENT_STANDALONE = re.compile(
    rf"(?<![A-Za-z0-9_./])({_AGENT_ALT})(?![A-Za-z0-9_/])",
    re.IGNORECASE,
)


def _normalize_agent_token(raw: str) -> str:
    t = re.sub(r"\s+", " ", raw.strip().lower())
    # strip wave/version suffixes: grok4, grok3-b7, codex-review → base seat
    if t.startswith("grok"):
        return "grok"
    if t.startswith("codex"):
        return "codex"
    if t.startswith("claude"):
        return "claude"
    if t.startswith("cursor"):
        return "cursor"
    if t.startswith("monet"):
        return "claude"
    if t.startswith("renoir"):
        return "claude"
    # exact "ag" only — do not use startswith("ag") (would swallow "agent")
    if t in ("antigravity", "ag") or t.startswith("antigravity"):
        return "ag"
    if t.startswith("gemini"):
        return "gemini"
    if t.startswith("fable"):
        return "claude"
    if t.startswith("minimax") or t == "mm":
        return "minimax"
    if t.startswith("sentry"):
        return "sentry"
    return t


def _split_agent_chain(raw: str) -> list[str]:
    """Split 'CURSOR/AG' or 'Codex / Claude' into individual seat tokens."""
    parts = re.split(r"\s*/\s*", (raw or "").strip())
    return [p for p in parts if p]


def extract_agents_and_clean(text: str, repo: str = "") -> tuple[list[str], str]:
    """Pull agent seat tags out of text; strip them + redundant repo label.

    Returns (agent_slugs_in_order, cleaned_title). Agent *names* are removed from
    the visible string so the HTML page can show logos instead.

    Recognizes all-caps seat tags, [bracket] tags (including multi-seat
    [CURSOR/AG]), and slash chains of seat names.
    """
    s = re.sub(r"\*+", "", text or "").strip()
    # drop our own effort status prefixes first
    s = re.sub(r"^\[(?:done|wip)\]\s*", "", s, flags=re.IGNORECASE)
    if repo:
        s = strip_redundant_repo_label(s, repo)

    agents: list[str] = []
    seen: set[str] = set()

    def add_agent(raw: str) -> None:
        key = _normalize_agent_token(raw)
        if key not in AGENT_LOGO:
            return
        slug = AGENT_LOGO[key][0]
        if slug not in seen:
            seen.add(slug)
            agents.append(slug)

    def add_chain(raw: str) -> None:
        for part in _split_agent_chain(raw):
            add_agent(part)

    # Collect all bracketed agents (incl. multi-seat), then remove them
    for m in _AGENT_BRACKET.finditer(s):
        add_chain(m.group(1))
    s = _AGENT_BRACKET.sub(" ", s)

    # (CODEX/AG, L) / (CODEX/HERSCHEL, L) style trailers
    for m in _AGENT_PAREN.finditer(s):
        add_chain(m.group(1))
    s = _AGENT_PAREN.sub(" ", s)

    # Slash chains: Post-Codex/AG …, Codex/Claude/Monet/AG/Cursor
    for m in list(_AGENT_SLASH_CHAIN.finditer(s)):
        add_chain(m.group(1))
    s = _AGENT_SLASH_CHAIN.sub(" ", s)

    # Leading bare seat name
    m = _AGENT_BARE_PREFIX.match(s)
    if m:
        add_agent(m.group(1))
        s = s[m.end() :]

    # Mid-title " — GROK — " / " - CODEX - " attributions
    def _emdash_sub(match: re.Match[str]) -> str:
        add_agent(match.group(1))
        return " — "

    s = _AGENT_EMDASH.sub(_emdash_sub, s)

    # Remaining standalone seat words (not path segments like .codex/ or codex/)
    for m in list(_AGENT_STANDALONE.finditer(s)):
        add_agent(m.group(1))
    s = _AGENT_STANDALONE.sub(" ", s)

    # Repo label may now be leading after agent tokens were removed
    if repo:
        s = strip_redundant_repo_label(s, repo)

    s = re.sub(r"\s*[\-–—]\s*[\-–—]\s*", " — ", s)
    # Orphaned "Post-" / "pre-" left when "Post-Codex/AG …" lost its seat chain
    s = re.sub(r"(?<![A-Za-z0-9])Post-\s+", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s{2,}", " ", s)
    s = re.sub(r"\s+\.\.\.(?=\s|$)", "", s)
    s = s.strip(" :-–—|/.,")
    return agents, s


def display_title(title: str, repo: str) -> str:
    _agents, clean = extract_agents_and_clean(title or "", repo)
    return clean or (title or "")


def display_effort_text(text: str, repo: str) -> str:
    _agents, clean = extract_agents_and_clean(text or "", repo)
    return clean


def _agent_label(slug: str) -> str:
    for s, lab in AGENT_LOGO.values():
        if s == slug:
            return lab
    return slug


LOGO_DIR = Path(__file__).resolve().parent.parent / "agent-logos"


def logo_file(slug: str) -> str:
    """<slug>.svg if present, else <slug>.png.

    Most seat marks are SVG, but Cursor and Grok Bot are supplied as PNGs, so
    the filename cannot be assumed.  Falls back to .svg so a missing asset
    still produces a stable (if broken) path rather than an exception.
    """
    for ext in ("svg", "png"):
        if (LOGO_DIR / f"{slug}.{ext}").is_file():
            return f"{slug}.{ext}"
    return f"{slug}.svg"


def agent_icons_html(agents: list[str]) -> str:
    """White-tile logo chips; title attribute keeps accessible name."""
    if not agents:
        return ""
    parts: list[str] = []
    labels: list[str] = []
    for slug in agents:
        label = _agent_label(slug)
        labels.append(label)
        src = html.escape(f"agent-logos/{logo_file(slug)}")
        lab = html.escape(label)
        parts.append(
            f'<span class="agent" title="{lab}">'
            f'<img src="{src}" alt="{lab}" width="14" height="14" loading="lazy" decoding="async" />'
            f"</span>"
        )
    aria = html.escape(", ".join(labels))
    return f'<span class="agents" aria-label="Agents: {aria}">' + "".join(parts) + "</span>"


def agent_icons_md(agents: list[str]) -> str:
    if not agents:
        return ""
    # Markdown: short tokens (HTML carries the real logos).
    return " ".join(f"`{_agent_label(slug)}`" for slug in agents)


def day_description(day: DayBucket) -> str:
    lines = [day.counts_line(), ""]
    if day.merged_prs:
        lines.append("Merged PRs:")
        for p in day.merged_prs[:40]:
            agents, title = extract_agents_and_clean(
                str(p.get("title") or ""), str(p.get("repo") or "")
            )
            agent_bit = f" ({', '.join(agents)})" if agents else ""
            lines.append(f"- [{p['repo']}#{p['number']}]{agent_bit} {title}")
        if len(day.merged_prs) > 40:
            lines.append(f"  … +{len(day.merged_prs) - 40} more")
        lines.append("")
    if day.issues_closed:
        lines.append("Issues closed:")
        for p in day.issues_closed[:30]:
            _a, title = extract_agents_and_clean(
                str(p.get("title") or ""), str(p.get("repo") or "")
            )
            lines.append(f"- [{p['repo']}#{p['number']}] {title}")
        lines.append("")
    if day.issues_opened:
        lines.append("Issues opened:")
        for p in day.issues_opened[:30]:
            _a, title = extract_agents_and_clean(
                str(p.get("title") or ""), str(p.get("repo") or "")
            )
            lines.append(f"- [{p['repo']}#{p['number']}] {title}")
        lines.append("")
    if day.effort_lines:
        lines.append("Effort board:")
        for e in day.effort_lines[:25]:
            agents, t = extract_agents_and_clean(e["text"], e["repo"])
            agent_bit = f" ({', '.join(agents)})" if agents else ""
            lines.append(f"- [{e['repo']}]{agent_bit} {t[:200]}")
    return "\n".join(lines).strip()


def build_markdown(days: list[DayBucket], generated: datetime, tz: ZoneInfo, base_url: str) -> str:
    lines = [
        "# Jay's Daily Coding-Related Activities",
        "",
        f"_Generated {generated.astimezone(tz).strftime('%Y-%m-%d %H:%M %Z')} · timezone {tz.key}_",
        "",
        "Sources: merged PRs, issues opened/closed, effort-board bullets (`docs/EFFORT-LOG.md`).",
        "Agent names are stripped from titles; HTML site shows logos instead.",
        "",
    ]
    if base_url:
        lines.append(f"- **HTML:** {base_url.rstrip('/')}/")
        lines.append(f"- **ICS (daily outline):** {base_url.rstrip('/')}/calendar/daily-digest.ics")
        lines.append(
            f"- **ICS (per-commit activity):** {base_url.rstrip('/')}/calendar/agent-activity.ics"
        )
        lines.append("")
    for day in days:
        if day.is_empty():
            continue
        lines.append(f"## {day.day.isoformat()}")
        lines.append("")
        lines.append(f"*{day.counts_line()}*")
        lines.append("")
        if day.merged_prs:
            lines.append("### Merged PRs")
            lines.append("")
            for p in day.merged_prs:
                repo = str(p.get("repo") or "")
                agents, title = extract_agents_and_clean(str(p.get("title") or ""), repo)
                agent_md = agent_icons_md(agents)
                prefix = f"{agent_md} " if agent_md else ""
                short, _cls = repo_badge(repo)
                lines.append(
                    f"- **{short}** {prefix}[#{p['number']}]({p['url']}): {title}"
                    + (f" _(by {p['user']})_" if p.get("user") else "")
                )
            lines.append("")
        if day.issues_closed:
            lines.append("### Issues closed")
            lines.append("")
            for p in day.issues_closed:
                repo = str(p.get("repo") or "")
                _a, title = extract_agents_and_clean(str(p.get("title") or ""), repo)
                short, _cls = repo_badge(repo)
                lines.append(f"- **{short}** [#{p['number']}]({p['url']}): {title}")
            lines.append("")
        if day.issues_opened:
            lines.append("### Issues opened")
            lines.append("")
            for p in day.issues_opened:
                repo = str(p.get("repo") or "")
                _a, title = extract_agents_and_clean(str(p.get("title") or ""), repo)
                short, _cls = repo_badge(repo)
                lines.append(f"- **{short}** [#{p['number']}]({p['url']}): {title}")
            lines.append("")
        if day.effort_lines:
            lines.append("### Effort board")
            lines.append("")
            for e in day.effort_lines:
                agents, t = extract_agents_and_clean(e["text"], e["repo"])
                agent_md = agent_icons_md(agents)
                short, _cls = repo_badge(e["repo"])
                prefix = f"{agent_md} " if agent_md else ""
                lines.append(f"- **{short}** {prefix}{t}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _format_day_heading(d: date) -> str:
    """Human day heading, e.g. 'August 10, 2026' (no leading zero on day)."""
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def _format_created_lede(generated: datetime, tz: ZoneInfo) -> str:
    """Subheading timestamp, e.g. 'Created: Aug 9, 2026 at 10:22pm'."""
    local = generated.astimezone(tz)
    hour12 = local.hour % 12 or 12
    ampm = "am" if local.hour < 12 else "pm"
    return (
        f"Created: {local.strftime('%b')} {local.day}, {local.year} "
        f"at {hour12}:{local.strftime('%M')}{ampm}"
    )


def build_html(days: list[DayBucket], generated: datetime, tz: ZoneInfo, base_url: str) -> str:
    esc = html.escape
    created_lede = esc(_format_created_lede(generated, tz))
    ics_daily = esc((base_url.rstrip("/") + "/calendar/daily-digest.ics") if base_url else "calendar/daily-digest.ics")
    ics_act = esc(
        (base_url.rstrip("/") + "/calendar/agent-activity.ics") if base_url else "../calendar/agent-activity.ics"
    )
    md_href = "digest.md"

    def item_row(
        repo: str,
        title_raw: str,
        *,
        number: Any = None,
        url: str = "",
    ) -> str:
        agents, clean = extract_agents_and_clean(title_raw, repo)
        short, css = repo_badge(repo)
        icons = agent_icons_html(agents)
        title_t = esc(clean)
        app_icon = REPO_APP_ICON.get(repo)
        if app_icon:
            # Icon-only for product apps (no ST/CT/UM text); full name in title/alt
            repo_html = (
                f'<span class="repo repo-with-icon repo-icon-only {esc(css)}" title="{esc(repo)}">'
                f'<img class="repo-app-icon" src="{esc(app_icon)}" alt="{esc(repo)}" '
                f'width="16" height="16" loading="lazy" decoding="async" /></span>'
            )
        else:
            repo_html = f'<span class="repo {esc(css)}" title="{esc(repo)}">{esc(short)}</span>'
        if number is not None and url:
            link = f'<a href="{esc(url)}">#{esc(str(number))}</a>'
            mid = f"{link}: " if clean else f"{link}"
        else:
            mid = ""
        # lead stacks repo above agent logos so the body keeps more horizontal width
        lead = f'<span class="item-lead">{repo_html}{icons}</span>'
        body = f'<span class="item-body">{mid}{title_t}</span>'
        return f"<li>{lead}{body}</li>"

    sections: list[str] = []
    for day in days:
        if day.is_empty():
            continue
        blocks: list[str] = []

        def list_block(title: str, items: list[dict[str, Any]], kind: str) -> None:
            if not items:
                return
            lis = [
                item_row(
                    str(p.get("repo") or ""),
                    str(p.get("title") or ""),
                    number=p.get("number"),
                    url=str(p.get("url") or ""),
                )
                for p in items
            ]
            blocks.append(f'<h3>{esc(title)}</h3><ul class="{kind}">' + "".join(lis) + "</ul>")

        list_block("Merged PRs", day.merged_prs, "prs")
        list_block("Issues closed", day.issues_closed, "closed")
        list_block("Issues opened", day.issues_opened, "opened")
        if day.effort_lines:
            el = [
                item_row(e["repo"], e["text"])
                for e in day.effort_lines
            ]
            blocks.append('<h3>Effort board</h3><ul class="effort">' + "".join(el) + "</ul>")

        day_label = esc(_format_day_heading(day.day))
        sections.append(
            f'<section class="day" id="{day.day.isoformat()}">'
            f"<h2>{day_label}</h2>"
            f'<p class="meta">{esc(day.counts_line())}</p>'
            + "".join(blocks)
            + "</section>"
        )

    body = "\n".join(sections) if sections else "<p>No activity in the lookback window.</p>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Jay's Daily Log</title>
  <style>
    :root {{
      --bg: #f4f6f9;
      --card: #ffffff;
      --text: #1a2332;
      --muted: #5b6b82;
      --accent: #0f766e;
      --link: #0369a1;
      --border: #e2e8f0;
      --st: #2563eb;
      --ct: #7c3aed;
      --um: #ea580c;
      --dd: #b45309;
      --ps: #be123c;
      --ar: #059669;
      --cl: #6366f1;
      --shared: #0d9488;
      --fleet: #475569;
      --bf: #0284c7;
      --ops: #64748b;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 1.5rem clamp(1rem, 4vw, 2.5rem) 3rem;
      max-width: 54rem;
      margin-inline: auto;
    }}
    h1 {{ font-size: 1.6rem; margin: 0 0 0.35rem; letter-spacing: -0.02em; color: #0f172a; }}
    h2 {{ font-size: 1.2rem; margin: 0 0 0.35rem; color: var(--accent); }}
    h3 {{ font-size: 0.8rem; margin: 1rem 0 0.4rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }}
    .lede {{ color: var(--muted); margin: 0 0 2rem; }}
    .links {{ display: flex; flex-wrap: wrap; gap: 0.75rem 1.25rem; margin-bottom: 1.75rem; font-size: 0.95rem; }}
    a {{ color: var(--link); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .day {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem 1.15rem 1.15rem;
      margin-bottom: 1rem;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }}
    .meta {{ color: var(--muted); font-size: 0.9rem; margin: 0 0 0.5rem; }}
    ul {{ margin: 0.25rem 0 0; padding-left: 0; list-style: none; }}
    li {{
      margin: 0.35rem 0;
      padding: 0.35rem 0.5rem;
      border-radius: 8px;
      display: flex;
      flex-wrap: wrap;
      align-items: flex-start;
      gap: 0.35rem 0.55rem;
      line-height: 1.4;
    }}
    li:nth-child(even) {{ background: #f8fafc; }}
    .item-lead {{
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 0.2rem;
      flex-shrink: 0;
      min-width: 1.5rem;
    }}
    .item-body {{
      flex: 1 1 14rem;
      min-width: min(100%, 12rem);
    }}
    .repo {{
      display: inline-flex;
      align-items: center;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      color: #fff;
      border-radius: 4px;
      padding: 0.12rem 0.45rem;
      vertical-align: middle;
      flex-shrink: 0;
    }}
    .repo-st {{ background: var(--st); }}
    .repo-ct {{ background: var(--ct); }}
    .repo-um {{ background: var(--um); }}
    .repo-dd {{ background: var(--dd); }}
    .repo-ps {{ background: var(--ps); }}
    .repo-ar {{ background: var(--ar); }}
    .repo-cl {{ background: var(--cl); }}
    .repo-shared {{ background: var(--shared); }}
    .repo-fleet {{ background: var(--fleet); }}
    .repo-bf {{ background: var(--bf); }}
    .repo-ops {{ background: var(--ops); }}
    .repo.repo-with-icon {{
      gap: 0;
      padding: 0.1rem;
      background: #fff;
      color: #0f172a;
      border: 1px solid var(--border);
      font-weight: 700;
    }}
    .repo.repo-icon-only {{
      padding: 0.08rem;
      border-radius: 5px;
    }}
    .repo-app-icon {{
      width: 1.15rem;
      height: 1.15rem;
      border-radius: 4px;
      object-fit: cover;
      display: block;
      flex-shrink: 0;
      background: #fff;
    }}
    .agents {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.2rem;
      flex-shrink: 0;
    }}
    .agent {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 1.15rem;
      height: 1.15rem;
      border-radius: 5px;
      border: 1px solid var(--border);
      background: #fff;
      padding: 1px;
    }}
    .agent img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }}
    footer {{ margin-top: 2rem; color: var(--muted); font-size: 0.85rem; }}
    code {{ font-size: 0.85em; background: #e2e8f0; padding: 0.1em 0.35em; border-radius: 4px; color: #0f172a; }}
    /* Hidden 2-col table: left = Repos/Agents labels; right = chips (wrap stays indented) */
    .legend {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin: 0 0 1.25rem;
      font-size: 0.8rem;
      color: var(--muted);
    }}
    .legend-section {{
      display: grid;
      grid-template-columns: 4.75rem minmax(0, 1fr);
      column-gap: 0.9rem;
      align-items: start;
    }}
    .legend-heading {{
      font-weight: 600;
      color: #475569;
      line-height: 1.35rem;
      padding-top: 0.05rem;
      flex-shrink: 0;
    }}
    .legend-items {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.45rem 1.05rem;
      min-width: 0;
    }}
    .legend-item {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      white-space: nowrap;
      line-height: 1.2;
    }}
    .legend-item .legend-label {{ color: var(--muted); }}
    .legend .agent {{ width: 1.15rem; height: 1.15rem; }}
  </style>
</head>
<body>
  <h1>Jay's Daily Log</h1>
  <p class="lede">{created_lede}</p>
  <div class="legend" aria-label="Legend">
    <div class="legend-section" aria-label="Repositories">
      <span class="legend-heading">Repos</span>
      <div class="legend-items">
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-st" title="Socratic.Trade"><img class="repo-app-icon" src="agent-logos/app-st.svg" alt="Socratic.Trade" width="14" height="14" /></span><span class="legend-label">Socratic.Trade</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-ct" title="Congress.Trade"><img class="repo-app-icon" src="agent-logos/app-ct.png" alt="Congress.Trade" width="14" height="14" /></span><span class="legend-label">Congress.Trade</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-um" title="Usage Monitor"><img class="repo-app-icon" src="agent-logos/app-um.png" alt="Usage Monitor" width="14" height="14" /></span><span class="legend-label">Usage Monitor</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-dd" title="DealDex.net"><img class="repo-app-icon" src="agent-logos/app-dd.png" alt="DealDex.net" width="14" height="14" /></span><span class="legend-label">DealDex.net</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-ar" title="Autorotate.Codes"><img class="repo-app-icon" src="agent-logos/app-ar.png" alt="Autorotate.Codes" width="14" height="14" /></span><span class="legend-label">Autorotate.Codes</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-cl" title="ContactLogo"><img class="repo-app-icon" src="agent-logos/app-cl.png" alt="ContactLogo" width="14" height="14" /></span><span class="legend-label">ContactLogo</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-ps" title="Personal Site"><img class="repo-app-icon" src="agent-logos/app-ps.png" alt="Personal Site" width="14" height="14" /></span><span class="legend-label">Personal Site</span></span>
        <span class="legend-item"><span class="repo repo-shared">CTS</span><span class="legend-label">congress-trading-shared</span></span>
        <span class="legend-item"><span class="repo repo-fleet">AFC</span><span class="legend-label">AI Fleet Coordinator</span></span>
        <span class="legend-item"><span class="repo repo-with-icon repo-icon-only repo-bf" title="BotFleet.app"><img class="repo-app-icon" src="agent-logos/app-bf.png" alt="BotFleet.app" width="14" height="14" /></span><span class="legend-label">BotFleet.app</span></span>
        <span class="legend-item"><span class="repo repo-ops">OPS</span><span class="legend-label">Fleet Ops</span></span>
      </div>
    </div>
    <div class="legend-section" aria-label="Agents">
      <span class="legend-heading">Agents</span>
      <div class="legend-items">
        <span class="legend-item"><span class="agent" title="Grok"><img src="agent-logos/grok.svg" alt="" width="12" height="12" /></span><span class="legend-label">Grok</span></span>
        <span class="legend-item"><span class="agent" title="Grok Bot"><img src="agent-logos/grok-bot.png" alt="" width="12" height="12" /></span><span class="legend-label">Grok Bot</span></span>
        <span class="legend-item"><span class="agent" title="Codex"><img src="agent-logos/codex.svg" alt="" width="12" height="12" /></span><span class="legend-label">Codex</span></span>
        <span class="legend-item"><span class="agent" title="Claude"><img src="agent-logos/claude.svg" alt="" width="12" height="12" /></span><span class="legend-label">Claude</span></span>
        <span class="legend-item"><span class="agent" title="Cursor"><img src="agent-logos/cursor.png" alt="" width="12" height="12" /></span><span class="legend-label">Cursor</span></span>
        <span class="legend-item"><span class="agent" title="Antigravity"><img src="agent-logos/ag.svg" alt="" width="12" height="12" /></span><span class="legend-label">Antigravity</span></span>
        <span class="legend-item"><span class="agent" title="Gemini"><img src="agent-logos/gemini.svg" alt="" width="12" height="12" /></span><span class="legend-label">Gemini</span></span>
        <span class="legend-item"><span class="agent" title="Kimi"><img src="agent-logos/kimi.svg" alt="" width="12" height="12" /></span><span class="legend-label">Kimi</span></span>
        <span class="legend-item"><span class="agent" title="DeepSeek"><img src="agent-logos/deepseek.svg" alt="" width="12" height="12" /></span><span class="legend-label">DeepSeek</span></span>
        <span class="legend-item"><span class="agent" title="MiniMax"><img src="agent-logos/minimax.png" alt="" width="12" height="12" /></span><span class="legend-label">MiniMax</span></span>
        <span class="legend-item"><span class="agent" title="Sentry"><img src="agent-logos/sentry.svg" alt="" width="12" height="12" /></span><span class="legend-label">Sentry</span></span>
      </div>
    </div>
  </div>
  <nav class="links">
    <a href="{md_href}">Markdown</a>
    <a href="{ics_daily}">ICS - daily</a>
    <a href="{ics_act}">ICS - per commit</a>
  </nav>
  {body}
  <footer>
    Built by <code>scripts/build-fleet-daily-digest.py</code> in
    <code>ai-fleet-coordinator</code>. Agent seat names (Grok/Codex/Claude/…) are
    shown as logos only. Owner/Jay is not badged (not a coding seat). Subscribe
    to the daily ICS in Apple Calendar (Add Subscription Calendar) or Google
    Calendar (From URL).

  </footer>
</body>
</html>
"""


def build_daily_ics(days: list[DayBucket], now: datetime, base_url: str) -> str:
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Jay Wedgeworth//Daily Coding Activities//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Jay's Daily Coding-Related Activities",
        "X-WR-CALDESC:One all-day entry per day: merged PRs, issues opened/closed, effort board. Hosted by ai-fleet-coordinator.",
        "X-WR-TIMEZONE:America/Chicago",
        "REFRESH-INTERVAL;VALUE=DURATION:PT6H",
        "X-PUBLISHED-TTL:PT6H",
    ]
    for day in days:
        if day.is_empty():
            continue
        d = day.day
        next_d = d + timedelta(days=1)
        # VALUE=DATE all-day: DTEND is exclusive next day
        uid = f"fleet-daily-{d.isoformat()}@ai-fleet-coordinator"
        url = f"{base_url.rstrip('/')}/#{d.isoformat()}" if base_url else ""
        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{now.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
                f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}",
                f"DTEND;VALUE=DATE:{next_d.strftime('%Y%m%d')}",
                f"SUMMARY:{ics_escape(day_summary_title(day))}",
                f"DESCRIPTION:{ics_escape(day_description(day))}",
            ]
        )
        if url:
            lines.append(f"URL:{url}")
        lines.extend(
            [
                "CATEGORIES:fleet-daily,agent-activity",
                "STATUS:CONFIRMED",
                "TRANSP:TRANSPARENT",
                "END:VEVENT",
            ]
        )
    lines.append("END:VCALENDAR")
    return join_ics(lines)


def main() -> int:
    owner = os.environ.get("FLEET_OWNER", "jaywedgeworth22").strip() or "jaywedgeworth22"
    repos_raw = os.environ.get("FLEET_REPOS", "").strip()
    repos = [r.strip() for r in repos_raw.split(",") if r.strip()] or DEFAULT_REPOS
    lookback = env_int("DIGEST_LOOKBACK_DAYS", 21)
    tz_name = os.environ.get("DIGEST_TZ", "America/Chicago").strip() or "America/Chicago"
    tz = ZoneInfo(tz_name)
    site_out = Path(os.environ.get("SITE_OUT", "site"))
    ics_out = Path(os.environ.get("ICS_OUT", "calendar/daily-digest.ics"))
    base_url = os.environ.get("SITE_BASE_URL", "").strip()
    # Default GitHub Pages URL if not set
    if not base_url:
        base_url = f"https://{owner}.github.io/ai-fleet-coordinator"

    tok = token()
    now = datetime.now(timezone.utc)
    since = (now.astimezone(tz).date() - timedelta(days=lookback))

    print(f"owner={owner} repos={repos} since={since} tz={tz_name}")
    print("fetching merged PRs…")
    prs = fetch_merged_prs(owner, repos, since, tok, tz)
    print(f"  {len(prs)} merged PRs")
    print("fetching issue churn…")
    opened, closed = fetch_issue_churn(owner, repos, since, tok, tz)
    print(f"  {len(opened)} opened, {len(closed)} closed")
    print("fetching effort boards…")
    effort = fetch_effort_rows(owner, repos, since, tok, tz)
    print(f"  {len(effort)} effort bullets")

    buckets = bucket_all(prs, opened, closed, effort)
    days = sorted(buckets.values(), key=lambda d: d.day, reverse=True)

    site_out.mkdir(parents=True, exist_ok=True)
    ics_out.parent.mkdir(parents=True, exist_ok=True)

    md = build_markdown(days, now, tz, base_url)
    html_doc = build_html(days, now, tz, base_url)
    ics_body = build_daily_ics(days, now, base_url)

    (site_out / "digest.md").write_text(md, encoding="utf-8")
    (site_out / "index.html").write_text(html_doc, encoding="utf-8")
    # GitHub Pages: disable Jekyll so dotted paths / raw ICS serve as-is
    (site_out / ".nojekyll").write_text("", encoding="utf-8")
    ics_out.write_bytes(ics_body.encode("utf-8"))

    # Agent logo assets (Grok/Codex/Claude/…) — required for HTML chips
    logos_src = Path(__file__).resolve().parent.parent / "agent-logos"
    if logos_src.is_dir():
        logos_dst = site_out / "agent-logos"
        if logos_dst.exists():
            shutil.rmtree(logos_dst)
        shutil.copytree(logos_src, logos_dst)

    # Copies under site/ so Pages hosts HTML + both ICS feeds from one root
    cal_site = site_out / "calendar"
    cal_site.mkdir(parents=True, exist_ok=True)
    (cal_site / "daily-digest.ics").write_bytes(ics_body.encode("utf-8"))
    agent_ics = Path("calendar/agent-activity.ics")
    if agent_ics.is_file():
        (cal_site / "agent-activity.ics").write_bytes(agent_ics.read_bytes())

    n_days = sum(1 for d in days if not d.is_empty())
    print(f"wrote {site_out / 'index.html'}")
    print(f"wrote {site_out / 'digest.md'}")
    print(f"wrote {ics_out} ({n_days} day events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
