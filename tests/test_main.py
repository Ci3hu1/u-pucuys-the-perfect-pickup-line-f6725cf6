#!/usr/bin/env python3
"""Tests for main.py: the entry gate is 1-200 UTF-8 characters, one line."""

import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

import main as entry  # noqa: E402


def run_entry(out_path: Path) -> None:
    env = dict(os.environ, ENTRY_OUTPUT=str(out_path))
    subprocess.run(
        [sys.executable, str(REPO / "main.py")],
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )


class TestEntryLine(unittest.TestCase):
    def test_char_count_within_gate(self):
        self.assertGreaterEqual(len(entry.LINE), 1)
        self.assertLessEqual(len(entry.LINE), 200)

    def test_exactly_one_line_no_line_breaks(self):
        self.assertNotIn("\n", entry.LINE)
        self.assertNotIn("\r", entry.LINE)

    def test_no_leading_trailing_whitespace(self):
        self.assertEqual(entry.LINE, entry.LINE.strip())

    def test_is_valid_utf8(self):
        entry.LINE.encode("utf-8")

    def test_output_is_exactly_one_line_no_trailing_blank(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "entry.txt"
            run_entry(out)
            raw = out.read_bytes()
            text = raw.decode("utf-8")
            self.assertEqual(text.splitlines(), [entry.LINE])
            self.assertTrue(text.endswith("\n"))
            self.assertFalse(text.endswith("\n\n"))

    def test_byte_identical_across_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = Path(tmp) / "entry1.txt"
            out2 = Path(tmp) / "entry2.txt"
            run_entry(out1)
            run_entry(out2)
            self.assertEqual(out1.read_bytes(), out2.read_bytes())

    def test_output_mode_is_0644(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "entry.txt"
            run_entry(out)
            mode = stat.S_IMODE(out.stat().st_mode)
            self.assertEqual(mode, 0o644)


class TestValidate(unittest.TestCase):
    def test_valid_line_passes_through_unchanged(self):
        self.assertEqual(entry.validate(entry.LINE), entry.LINE)

    def test_too_long_rejected(self):
        with self.assertRaises(ValueError):
            entry.validate("x" * 201)

    def test_blank_rejected(self):
        with self.assertRaises(ValueError):
            entry.validate("   ")

    def test_multiline_rejected(self):
        with self.assertRaises(ValueError):
            entry.validate("one\ntwo")

    def test_control_character_rejected(self):
        with self.assertRaises(ValueError):
            entry.validate("hello\x07world")

    def test_read_back_matches_written_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "entry.txt"
            run_entry(out)
            self.assertEqual(out.read_bytes(), (entry.LINE + "\n").encode("utf-8"))


class TestV2Line(unittest.TestCase):
    def test_v2_line_exact(self):
        self.assertEqual(
            entry.LINE,
            "Are you a compiler error on line 47? Because I can't stop staring at you and I have no idea how to fix it.",
        )

    def test_v2_line_length(self):
        self.assertEqual(len(entry.LINE), 106)

    def test_v2_specific_detail(self):
        self.assertIn("line 47", entry.LINE)

    def test_validate_rejects_punctuation_only(self):
        with self.assertRaises(ValueError):
            entry.validate("!!!")


if __name__ == "__main__":
    unittest.main()
