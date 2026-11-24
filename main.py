#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one original startup pitch line to /output/entry.txt: CARTPULL,
a cart-recovery tool for Shopify stores. The pitch proves unit
economics per single store — what one store recovers in a month and
what share of that recovery we take — instead of claiming aggregate
traction across many customers. One line, no fake scale.
"""

import os
import sys

TEXT = (
    "CARTPULL: one Shopify store recovers $3,800/month in abandoned "
    "checkouts — we take 5% of what we bring back, $0 if we recover nothing."
)

MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
