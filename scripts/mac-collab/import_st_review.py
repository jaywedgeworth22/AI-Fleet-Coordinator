#!/usr/bin/env python3
"""Import the 2026-08-19 Socratic.Trade full-app review into the mac-collab
findings tool.

Source: a saved Claude.ai artifact HTML report ("Socratic Trade Audit").
The report already folds 386 raw findings into 45 actionable work items
(each a `<details class="row" data-tranche="...">` block in the "work plan"
section) -- those 45 are what gets imported, not the underlying raw finds.

Usage:
    python3 import_st_review.py --dry-run   # print counts, POST nothing
    python3 import_st_review.py             # actually import
"""
from __future__ import annotations

import html as html_lib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

SOURCE_HTML = Path(
    "/Users/jay/.claude/projects/-Users-jay-Code-ai-fleet-coordinator/"
    "e0490435-4974-4eec-99db-38e558e22530/tool-results/"
    "artifact-eb4784aa-1787176034-d819.html"
)
BASE_URL = "http://127.0.0.1:8792"
APP = "socratic-trade"
SOURCE_LABEL = "Socratic.Trade full-app review 2026-08-19"
SECRETS = Path.home() / ".secrets" / "mac-collab.env"

TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(fragment: str | None) -> str:
    if not fragment:
        return ""
    text = TAG_RE.sub("", fragment)
    text = html_lib.unescape(text)
    return re.sub(r"[ \t]+", " ", text).strip()


def load_token() -> str:
    env = os.environ.get("MAC_COLLAB_TOKEN", "").strip()
    if env:
        return env
    if SECRETS.is_file():
        for line in SECRETS.read_text().splitlines():
            s = line.strip()
            if s.startswith("export "):
                s = s[7:]
            if s.startswith("MAC_COLLAB_TOKEN="):
                return s.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def extract_attr(block: str, name: str) -> str | None:
    m = re.search(rf'{name}="([^"]*)"', block)
    return m.group(1) if m else None


def extract_labeled_p(block: str, label: str) -> str:
    m = re.search(
        rf'<span class="lab">{re.escape(label)}</span>\s*<p>(.*?)</p>', block, re.DOTALL
    )
    return strip_tags(m.group(1)) if m else ""


def extract_labeled_list(block: str, label: str) -> list[str]:
    m = re.search(
        rf'<span class="lab">{re.escape(label)}</span>\s*<ul>(.*?)</ul>', block, re.DOTALL
    )
    if not m:
        return []
    return [strip_tags(li) for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.DOTALL)]


def extract_labeled_files(block: str, label: str) -> list[str]:
    m = re.search(
        rf'<span class="lab">{re.escape(label)}</span>\s*<div class="files">(.*?)</div>',
        block,
        re.DOTALL,
    )
    if not m:
        return []
    return [strip_tags(c) for c in re.findall(r"<code>(.*?)</code>", m.group(1), re.DOTALL)]


def parse_work_items(html: str) -> list[dict]:
    blocks = re.findall(r'<details class="row"[^>]*data-tranche="[^"]*"[^>]*>.*?</details>', html, re.DOTALL)
    items = []
    for block in blocks:
        key_m = re.search(r'<span class="key">([^<]*)</span>', block)
        title_m = re.search(r'<span class="rtitle">([^<]*)</span>', block)
        effort_m = re.search(r'<span class="pill eff">effort ([^<]*)</span>', block)
        closes = re.findall(r'<span class="uid">([^<]*)</span>', block)

        item = {
            "key": strip_tags(key_m.group(1)) if key_m else None,
            "title": strip_tags(title_m.group(1)) if title_m else None,
            "severity": extract_attr(block, "data-sev"),
            "tranche": extract_attr(block, "data-tranche"),
            "surface": extract_attr(block, "data-surface"),
            "effort": strip_tags(effort_m.group(1)) if effort_m else None,
            "closes": [strip_tags(c) for c in closes],
            "root_cause": extract_labeled_p(block, "Root cause"),
            "the_one_change": extract_labeled_p(block, "The one change"),
            "plan": extract_labeled_p(block, "Plan"),
            "edit_sites": extract_labeled_files(block, "Edit sites"),
            "approach": extract_labeled_p(block, "Approach"),
            "tests_that_must_fail_first": extract_labeled_list(block, "Tests that must fail first"),
            "what_could_break": extract_labeled_p(block, "What could break"),
        }
        items.append(item)
    return items


TRANCHE_LABELS = {"1": "Now", "2": "Next", "3": "Later"}


def build_description(item: dict) -> str:
    parts = []
    if item["root_cause"]:
        parts.append(f"Root cause: {item['root_cause']}")
    tranche = TRANCHE_LABELS.get(item["tranche"], item["tranche"])
    parts.append(f"Tranche: {tranche}  ·  Effort: {item['effort'] or 'n/a'}")
    if item["closes"]:
        parts.append(f"Closes {len(item['closes'])} raw finding(s): {', '.join(item['closes'])}")
    if item["plan"]:
        parts.append(f"Plan (verified): {item['plan']}")
    if item["approach"]:
        parts.append(f"Approach: {item['approach']}")
    if item["what_could_break"]:
        parts.append(f"What could break: {item['what_could_break']}")
    return "\n\n".join(parts)


def build_recommended_fix(item: dict) -> str:
    parts = []
    if item["the_one_change"]:
        parts.append(f"The one change: {item['the_one_change']}")
    if item["edit_sites"]:
        parts.append("Edit sites: " + ", ".join(item["edit_sites"]))
    if item["tests_that_must_fail_first"]:
        tests = "\n".join(f"- {t}" for t in item["tests_that_must_fail_first"])
        parts.append(f"Tests that must fail first:\n{tests}")
    return "\n\n".join(parts)


def to_payload(item: dict) -> dict:
    return {
        "app": APP,
        "external_uid": item["key"],
        "source": SOURCE_LABEL,
        "title": item["title"],
        "severity": item["severity"],
        "category": None,
        "surface": item["surface"],
        "description": build_description(item),
        "recommended_fix": build_recommended_fix(item),
        "status": "open",
    }


def post_finding(token: str, payload: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/findings",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    html = SOURCE_HTML.read_text(encoding="utf-8")
    items = parse_work_items(html)
    print(f"Parsed {len(items)} work items from {SOURCE_HTML.name}")

    missing_title = [i for i in items if not i["title"] or not i["key"]]
    if missing_title:
        print(f"WARNING: {len(missing_title)} items missing key/title -- parser may need adjustment", file=sys.stderr)

    sev_counts = Counter(i["severity"] for i in items)
    tranche_counts = Counter(TRANCHE_LABELS.get(i["tranche"], i["tranche"]) for i in items)
    print("By severity:", dict(sorted(sev_counts.items())))
    print("By tranche:", dict(tranche_counts))

    if dry_run:
        print("\n--dry-run: no POSTs sent. Sample payload for first item:")
        print(json.dumps(to_payload(items[0]), indent=2)[:1500])
        return 0

    token = load_token()
    if not token:
        print("ERROR: MAC_COLLAB_TOKEN not found (env or ~/.secrets/mac-collab.env)", file=sys.stderr)
        return 1

    errors = 0
    for i, item in enumerate(items, 1):
        payload = to_payload(item)
        try:
            post_finding(token, payload)
        except urllib.error.HTTPError as e:
            print(f"[{i}/{len(items)}] ERROR {item['key']}: HTTP {e.code} {e.read().decode('utf-8', 'replace')}")
            errors += 1
            continue
        except urllib.error.URLError as e:
            print(f"[{i}/{len(items)}] ERROR {item['key']}: {e}")
            errors += 1
            continue
    print(f"\nDone. errors={errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
