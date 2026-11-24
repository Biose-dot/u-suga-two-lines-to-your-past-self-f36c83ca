#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
line 1 warns my past self about one specific moment in a single
sentence; line 2 says in one sentence why that moment mattered and what
changed because of it.
"""
import os

ENTRY = (
    "Do not delete the voicemail from Grandma on your eighteenth birthday just to free up space, because her voice saying your name is the one recording you will spend years trying to remember.\n"
    "Losing it taught me that storage is cheap and voices are not, so now I keep every message from the people I love — even the ones I think I will never need again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
