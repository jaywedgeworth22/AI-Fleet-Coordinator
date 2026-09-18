#!/usr/bin/env python3
"""Assert Backup fleet GitHub repositories uses the 600-minute GitHub-delay margin.

Run: python3 scripts/sentry-ci-report-margins_test.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("sentry-ci-report.py")


def _assign_value(tree: ast.AST, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if name in targets:
                return ast.literal_eval(node.value)
    raise AssertionError(f"{name} not found in {SCRIPT.name}")


def main() -> int:
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    default = _assign_value(tree, "DEFAULT_CHECKIN_MARGIN")
    overrides = _assign_value(tree, "CHECKIN_MARGIN_OVERRIDES")
    schedules = _assign_value(tree, "CRON_SCHEDULES")

    assert default == 15, default
    expected = {
        "Backup fleet GitHub repositories": 600,
    }
    assert overrides == expected, overrides
    assert schedules.get("Backup fleet GitHub repositories") == "0 7 * * *", schedules
    print("MARGIN_PARSE_OK", overrides)
    print("BACKUP_REPOS_CRON_OK", schedules["Backup fleet GitHub repositories"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
