#!/usr/bin/env python3
"""make.fun entry: Say What Actually Broke.

Writes one line of brutally honest, funny software error copy to
/output/entry.txt. Gate: 1-200 chars, non-blank, single line.
"""

import os

LINE = (
    "Error: your file didn't save \u2014 the disk is full. "
    "It's currently standing outside in the rain. "
    "Free up some space and try again."
)


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be blank"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
