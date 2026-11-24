#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800, using only things a person from 1800
already knows: libraries, post offices, roads, letters, books, speech.

Deterministic, standard library only, no network access. The output
goes to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).
"""

import os

ENTRY = (
    "Picture all the world's libraries and post offices joined by roads "
    "of light, so a letter, a book, or a spoken word reaches anyone, "
    "anywhere, in a blink."
)

# Words coined after 1800 that the sentence must never carry: the
# traveler could not picture them, and the judge brief forbids them.
ANACHRONISMS = ("internet", "computer", "online", "digital", "website")


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    lowered = text.lower()
    for word in ANACHRONISMS:
        if word in lowered:
            raise SystemExit("entry uses a post-1800 word: %s" % word)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
