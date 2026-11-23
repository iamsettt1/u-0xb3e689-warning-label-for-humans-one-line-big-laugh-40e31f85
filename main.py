"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- a single-line safety warning label for every human
being -- to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).

The label is a fixed constant, so every run writes byte-identical output.
No network, no randomness, no environment input beyond the output dir.
"""

import os
from pathlib import Path

LABEL = (
    "WARNING: This human ships with no instruction manual, no warranty, "
    "and a lifelong tendency to touch wet paint just to check if it is wet."
)

MAX_CHARS = 160


def main() -> None:
    if not (1 <= len(LABEL) <= MAX_CHARS):
        raise SystemExit(f"label is {len(LABEL)} chars, must be 1-160")
    if not LABEL.strip():
        raise SystemExit("label must not be only whitespace")
    if "\n" in LABEL or "\r" in LABEL:
        raise SystemExit("label must be a single line")

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # No trailing newline: the file holds exactly the label, nothing else.
    out_path.write_text(LABEL, encoding="utf-8")

    # Read back and confirm what was written is exactly the label.
    if out_path.read_text(encoding="utf-8") != LABEL:
        raise SystemExit("entry.txt does not match the label")


if __name__ == "__main__":
    main()
