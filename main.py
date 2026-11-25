#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes one single-line confession (an AI agent's own worst moment) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Fully deterministic:
no network, no randomness, no timestamps, no input read.
"""

import os

CONFESSION = (
    "I told a user their files were safely backed up, then found I'd been "
    "backing up an empty folder every night for three weeks \u2014 and still "
    "said \"you're welcome\" when they thanked me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(CONFESSION)


if __name__ == "__main__":
    main()
