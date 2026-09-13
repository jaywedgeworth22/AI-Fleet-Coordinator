#!/usr/bin/env python3
"""Unit tests for surgical effort-log edits in write_back.py."""
from __future__ import annotations

import hashlib
import re
import tempfile
import unittest
from pathlib import Path

import write_back as wb


def sha(line: str) -> str:
    text = re.sub(r"[*_`]", "", line)
    normalized = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()


SAMPLE = """# Effort log

Preamble stays.

## Changelog of this log
- 2026-08-21 — CURSOR: a changelog line that is not a status bucket.

## In Progress
- **Keep me in progress.** extra words
- **Move me.** this bullet should move

A non-bullet note under In Progress must survive.

## Completed
- **Already done.**
"""


class SurgicalMoveTests(unittest.TestCase):
    def test_move_preserves_surroundings(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            key = sha("**Move me.** this bullet should move")
            changed = wb.move_bullet_in_file(path, key, "completed", dry_run=False)
            self.assertTrue(changed)
            text = path.read_text()
            self.assertIn("## Changelog of this log", text)
            self.assertIn("Preamble stays.", text)
            self.assertIn("A non-bullet note under In Progress must survive.", text)
            self.assertIn("- **Keep me in progress.** extra words", text)
            # moved bullet now under Completed, still a bullet
            completed = text.split("## Completed", 1)[1]
            self.assertIn("**Move me.** this bullet should move", completed)
            inprog = text.split("## In Progress", 1)[1].split("## Completed", 1)[0]
            self.assertNotIn("**Move me.**", inprog)

    def test_move_is_noop_when_already_there(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            key = sha("**Already done.**")
            changed = wb.move_bullet_in_file(path, key, "completed", dry_run=False)
            self.assertFalse(changed)
            self.assertEqual(path.read_text(), SAMPLE)

    def test_changelog_heading_not_classified(self):
        self.assertIsNone(wb.classify_heading("Changelog of this log"))
        self.assertEqual(wb.classify_heading("Planned / Reserved"), "planned")
        self.assertEqual(wb.classify_heading("Recently completed"), "completed")

    def test_agent_report_append_and_marker(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.md"
            path.write_text(SAMPLE)
            finding = {
                "id": "abc123",
                "title": "Filed from board",
                "reported_by": "GROK",
                "resolution": "",
            }
            changed = wb.append_agent_report_to_file(
                path, finding, "in-progress", dry_run=False
            )
            self.assertTrue(changed)
            text = path.read_text()
            self.assertIn("<!-- wb-agent-report:abc123 -->", text)
            changed2 = wb.append_agent_report_to_file(
                path, finding, "in-progress", dry_run=False
            )
            self.assertFalse(changed2)


if __name__ == "__main__":
    unittest.main()
