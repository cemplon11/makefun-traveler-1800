#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet in terms a person from 1800 could picture: a post road, a letter,
a library, a shop, a newspaper. Pure stdlib, deterministic.
"""
import os

SENTENCE = (
    "Imagine a post road of copper wire where a letter flies in a blink "
    "to any town on Earth, and every library and shop and newspaper lies "
    "open upon your desk at home."
)


def main():
    assert 1 <= len(SENTENCE) <= 200, "sentence must fit the 200 character gate"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), "exactly one sentence"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    print(f"wrote {path}: {len(SENTENCE)} chars")


if __name__ == "__main__":
    main()
