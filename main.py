#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

A tiny program with one job: hand over a single fortune-cookie line
written for a software engineer. The line is short on purpose -- a
fortune cookie is a whisper, not a lecture -- and it is written to
/output/entry.txt so the grader can read exactly one line.

The joke itself lives in FORTUNE below. It leans on three things every
engineer recognises at once: the Friday-afternoon deploy, the bug that
only ever shows up in production, and the pager going off in the
middle of the night. The fortune-cookie voice is deliberate: an old,
solemn proverb that turns out to be about your on-call shift.
"""

import os
import sys

# Where the grader expects the single line. The harness sets
# MAKEFUN_OUTPUT_DIR; fall back to /output when it is absent.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The fortune itself. At most 120 characters, one line, no newlines.
# An old-sounding proverb, but the prophecy is pure on-call life:
# Friday deploy, a staging-shy bug, and a 3 a.m. page.
FORTUNE = (
    "Deploy on Friday and the bug that sleeps in staging shall wake "
    "in production, paging you at 3 a.m. Bring snacks."
)


def main() -> int:
    """Write the single fortune line and report what was written."""
    line = FORTUNE.strip()
    if not line:
        print("error: fortune line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: fortune must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > 120:
        print(
            "error: fortune is %d characters, over the 120 limit"
            % len(line),
            file=sys.stderr,
        )
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # One line plus its terminator: the file holds exactly one line,
    # and the trailing newline is what makes it a line, not a second one.
    with open(ENTRY_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), ENTRY_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

