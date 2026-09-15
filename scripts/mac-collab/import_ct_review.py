#!/usr/bin/env python3
"""Import the 2026-08-19 Congress.Trade full-app review into the mac-collab
findings tool.

Source: /Users/jay/Code/Congress.Trade/.review-shots/findings/final.part00.json
(467 curated findings, already deduped/verified from a 695-finding raw pass).

Usage:
    python3 import_ct_review.py --dry-run   # print counts, POST nothing
    python3 import_ct_review.py             # actually import
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

SOURCE_JSON = Path(
    "/Users/jay/Code/Congress.Trade/.review-shots/findings/final.part00.json"
)
BASE_URL = "http://127.0.0.1:8792"
APP = "congress-trade"
SOURCE_LABEL = "Congress.Trade full-app review 2026-08-19"
SECRETS = Path.home() / ".secrets" / "mac-collab.env"

STATUS_MAP = {
    "open": "open",
    "unchecked": "open",
    "partial": "in_progress",
}


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


def build_description(f: dict) -> str:
    parts = [f.get("description", "").strip()]
    if f.get("impact"):
        parts.append(f"Impact: {f['impact']}")
    if f.get("location"):
        parts.append(f"Location: {f['location']}")
    if f.get("evidence"):
        parts.append(f"Evidence: {f['evidence']}")
    if f.get("status_vs_prior"):
        parts.append(f"Status vs prior review: {f['status_vs_prior']}")
    if f.get("verifier_note"):
        parts.append(f"Verifier note: {f['verifier_note']}")
    if f.get("merged_from"):
        parts.append(f"Merged from: {', '.join(f['merged_from'])}")
    return "\n\n".join(p for p in parts if p)


def build_recommended_fix(f: dict) -> str:
    parts = []
    if f.get("recommendation"):
        parts.append(f["recommendation"])
    meta_bits = []
    if f.get("effort"):
        meta_bits.append(f"effort {f['effort']}")
    if f.get("confidence"):
        meta_bits.append(f"confidence {f['confidence']}")
    if f.get("verdict"):
        meta_bits.append(f"verdict {f['verdict']}")
    if meta_bits:
        parts.append("(" + ", ".join(meta_bits) + ")")
    return "\n".join(parts)


def to_payload(f: dict) -> dict:
    status = STATUS_MAP.get(f.get("current_status"), "open")
    return {
        "app": APP,
        "external_uid": f["uid"],
        "source": SOURCE_LABEL,
        "title": f["title"],
        "severity": f.get("severity"),
        "category": f.get("category") or f.get("lens"),
        "surface": f.get("surface"),
        "description": build_description(f),
        "recommended_fix": build_recommended_fix(f),
        "status": status,
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
    findings = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    print(f"Loaded {len(findings)} findings from {SOURCE_JSON}")

    sev_counts = Counter(f.get("severity") for f in findings)
    status_counts = Counter(STATUS_MAP.get(f.get("current_status"), "open") for f in findings)
    print("By severity:", dict(sorted(sev_counts.items())))
    print("By mapped status:", dict(status_counts))

    if dry_run:
        print("\n--dry-run: no POSTs sent. Sample payload for first finding:")
        print(json.dumps(to_payload(findings[0]), indent=2)[:1500])
        return 0

    token = load_token()
    if not token:
        print("ERROR: MAC_COLLAB_TOKEN not found (env or ~/.secrets/mac-collab.env)", file=sys.stderr)
        return 1

    created = updated = errors = 0
    for i, f in enumerate(findings, 1):
        payload = to_payload(f)
        try:
            result = post_finding(token, payload)
        except urllib.error.HTTPError as e:
            print(f"[{i}/{len(findings)}] ERROR {f['uid']}: HTTP {e.code} {e.read().decode('utf-8', 'replace')}")
            errors += 1
            continue
        except urllib.error.URLError as e:
            print(f"[{i}/{len(findings)}] ERROR {f['uid']}: {e}")
            errors += 1
            continue
        if i % 50 == 0 or i == len(findings):
            print(f"[{i}/{len(findings)}] ...")
    print(f"\nDone. errors={errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
