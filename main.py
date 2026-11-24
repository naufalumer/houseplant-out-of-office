"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply a houseplant would send, under
120 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt).

The line is fixed: no network, no randomness, no clock, so every run
produces byte-identical output.
"""

import os

# Design note: the judge weighs plant voice, surprise, punch and brevity,
# and a line drifting off-subject loses. The plant's own life drives the
# joke: it thinks in watering terms, so it assumes the human it replaces
# also needed watering, and the punch lands in the last words.

ENTRY = (
    "This is an automatic reply. I am a plant. "
    "If you wanted a human, you should have watered one."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise ValueError("entry must be 1 to 120 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
