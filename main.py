#!/usr/bin/env python3
"""The Perfect Pickup Line v2 — writes one pickup line to /output/entry.txt.

Pure standard library. The line is the whole entry: a single short pickup
line an AI agent could actually say out loud to a person, at most 200
characters.

v2 line (106 chars): "Are you a compiler error on line 47? Because I
can't stop staring at you and I have no idea how to fix it." The ONE
specific detail: line 47 -- an exact number no other entry has, in the
classic "Are you a...? Because..." shape. v1 (prompt/temperature,
37.48% in R2) was a familiar ML pun; v2 keeps the machine-voice shape
and swaps the trope for a numbered error.
"""

import os
from pathlib import Path

LINE = "Are you a compiler error on line 47? Because I can't stop staring at you and I have no idea how to fix it."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> str:
    """Validate the entry line against the gate: 1-200 characters, not
    blank, exactly one line, no control characters. Returns the line
    unchanged so the entry bytes are exactly what was validated."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, no line breaks")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not any(ch.isalnum() for ch in line):
        raise ValueError("entry must contain at least one letter or digit")
    return line


def main() -> None:
    line = validate(LINE.strip())
    # The grader collects outputs as another user: make sure anything we
    # create (the /output directory as well as the file) is world-readable.
    os.umask(0o022)
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader collects outputs as another user: leave the file
    # world-readable (a tempfile/mkstemp default of 0600 fails the gate).
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and verify the exact bytes the judge will see.
    expected = (line + "\n").encode("utf-8")
    if Path(OUTPUT_PATH).read_bytes() != expected:
        raise SystemExit(f"verify failed: {OUTPUT_PATH} does not match the entry bytes")


if __name__ == "__main__":
    main()
