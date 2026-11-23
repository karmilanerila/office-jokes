"""Office-jokes entry: write one office joke to /output/entry.txt.

The program is deliberately tiny: the joke is a single line, and the
grader only reads the file it writes. Everything is deterministic --
the same bytes are written on every run, with no clock, randomness,
or network involved.
"""

import os

# One line, 143 characters plus the trailing newline -- comfortably
# inside the gate's 1-199 character window, and short enough that
# every word has to earn its place.
JOKE = (
    "I finally blocked focus time on my calendar, and within minutes "
    "three people invited me to a meeting called "
    "'Quick sync about your focus time.'"
)


def main() -> None:
    # The gate requires 1 to 199 characters of UTF-8 text, not only
    # whitespace. Fail loudly here rather than shipping an invalid file.
    text = JOKE + "\n"
    if not 1 <= len(text) <= 199 or not JOKE.strip():
        raise ValueError(f"joke is {len(text)} characters, gate needs 1-199")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
