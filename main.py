"""Passive-aggressive fridge note entry for make.fun.

Writes one single-line note from a smart fridge to /output/entry.txt.
"""

import os

LINE = "The yogurt expired Tuesday. I kept it anyway — unlike you, I commit to things."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, "note must be 1-200 characters"
    assert LINE.strip(), "note must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
