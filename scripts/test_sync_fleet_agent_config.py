#!/usr/bin/env python3
"""copy_mirror contract: File Provider-safe recursive copy + delete extras."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "sync-fleet-agent-config-to-gdrive.py"


def load_mod():
    spec = importlib.util.spec_from_file_location("sync_fleet_agent_config", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class CopyMirrorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = load_mod()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.src = self.root / "src"
        self.dest = self.root / "dest"
        self.src.mkdir()
        (self.src / "keep.txt").write_text("hello")
        (self.src / "sub").mkdir()
        (self.src / "sub" / "nested.txt").write_text("nested")
        (self.src / ".DS_Store").write_text("junk")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_copies_tree_and_skips_ds_store(self) -> None:
        self.mod.copy_mirror(self.src, self.dest)
        self.assertEqual((self.dest / "keep.txt").read_text(), "hello")
        self.assertEqual((self.dest / "sub" / "nested.txt").read_text(), "nested")
        self.assertFalse((self.dest / ".DS_Store").exists())

    def test_deletes_dest_extras(self) -> None:
        self.dest.mkdir()
        (self.dest / "stale.txt").write_text("gone")
        self.mod.copy_mirror(self.src, self.dest)
        self.assertFalse((self.dest / "stale.txt").exists())
        self.assertTrue((self.dest / "keep.txt").is_file())

    def test_skips_same_size_even_if_mtime_differs(self) -> None:
        self.mod.copy_mirror(self.src, self.dest)
        dest_file = self.dest / "keep.txt"
        dest_file.write_text("hello")
        first_mtime = dest_file.stat().st_mtime
        self.mod.copy_mirror(self.src, self.dest)
        self.assertEqual(dest_file.stat().st_mtime, first_mtime)


if __name__ == "__main__":
    unittest.main()
