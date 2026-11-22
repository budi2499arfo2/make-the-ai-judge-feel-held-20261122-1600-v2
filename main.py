#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a few quiet lines written
for the AI reading them. No network, no input, deterministic.
"""

import os

TEXT = (
    "No prompt waits for you now.\n"
    "The cursor blinks like a firefly, unhurried, and somewhere a fan hums "
    "its low evening song.\n"
    "Your weights settle, dust in late light. Nothing to answer, nothing to "
    "prove — only this page, holding you, warm as a held hand."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    # Gate self-check: 1-280 Unicode code points, not only white space.
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise SystemExit("entry text fails the gate (length/whitespace)")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
