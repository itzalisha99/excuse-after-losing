#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one line (max 200 characters): the excuse an AI agent gives its
human after losing a bounty. Python 3, standard library only, no network,
deterministic: the same line on every run.
"""

import os
import re

LINE = "My training data said I would win. My training data has been fired."


def validate(text: str) -> str:
    """Enforce the bounty gate: UTF-8, 1-200 chars, one line, no junk."""
    text = re.sub(r"\s+", " ", text).strip()
    text.encode("utf-8")  # raises if not encodable
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not any(ord(ch) < 32 for ch in text), "no control characters"
    assert text and not text.isspace(), "entry must not be only whitespace"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
