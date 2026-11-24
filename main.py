#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Pure standard library. The line is the whole entry: a single short pickup
line an AI agent could actually say out loud to a person, at most 200
characters.

The line: "Are you a prompt? Because one look at you and my temperature
went up."
69 characters, one breath. The turn is "temperature": a sampling
temperature the model dials up, and getting flustered at first sight.
It is a line only a machine would say about itself, in the classic
"Are you a...? Because..." pickup shape, so it reads as a genuine pickup
line on the first hearing — no setup, no explanation after it.
"""

import os

LINE = "Are you a prompt? Because one look at you and my temperature went up."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, no line breaks")
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


if __name__ == "__main__":
    main()
