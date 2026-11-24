#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short rant about a small everyday annoyance to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The rant: the smoke detector's dying-battery beep at 3 a.m.
"""

import os
import sys

# The rant in three beats: the beep, the chair, the burglar.
SETUP = (
    "At 3 a.m. the smoke detector beeped once. The dying-battery beep — "
    "the one that means it will beep every ninety seconds until the end "
    "of time."
)
ESCALATION = (
    "I stood on a chair in the dark, in my underwear, holding a broom, "
    "trying to twist it off the ceiling. It beeped again."
)
PUNCH = "I have never felt more like a burglar in my own home."

RANT = " ".join((SETUP, ESCALATION, PUNCH))
OUTPUT_PATH = "entry.txt"


def write_entry(text: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_PATH), "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    text = RANT
    if not (1 <= len(text) <= 400) or not text.strip():
        print(f"rant must be 1-400 non-whitespace characters, got {len(text)}",
              file=sys.stderr)
        return 1
    write_entry(text, os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
