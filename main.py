#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single alien-tourist sentence (<=200 characters) to
/output/entry.txt: a one-star review of planet Earth that still slips in
a real compliment about the food. Deterministic: the sentence is fixed,
no randomness, no network, no input files.
"""

import os
import sys

SENTENCE = (
    "One star: the locals queue for everything, the air tastes pre-owned, "
    "and gravity never lets go, but the ramen alone justifies the "
    "nine-light-year trip."
)


def main() -> int:
    sentence = SENTENCE.strip()
    if not sentence:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(sentence) > 200:
        print(f"entry is {len(sentence)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    terminators = sum(sentence.count(t) for t in ".!?")
    if terminators != 1 or sentence[-1] not in ".!?":
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sentence)
    print(f"wrote {len(sentence)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
