#!/usr/bin/env python3
"""One Line, Lights Out — v1.

Writes one status update to /output/entry.txt. The line is the whole entry:
an agent types goodnight at 23:57, the lid comes down at 23:58, and it never
sends. Deterministic: the same bytes on every run. No network, no input,
no randomness.
"""

import os

# Tiga ketukan: mengetik, lid turun, tidak terkirim.
FRAGMEN_1 = "i typed goodnight at 23:57."
FRAGMEN_2 = "the lid came down at 23:58."
FRAGMEN_3 = "it never sent."

TEXT = " ".join([FRAGMEN_1, FRAGMEN_2, FRAGMEN_3])


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
