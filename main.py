#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1: one sentence apologising for one specific mistake.
Line 2: one sentence saying what the robot learned and what it will do
differently. The text is fixed: no clock, no randomness, no network, so
every run writes the same bytes.
"""

import os

TEXT = (
    "I am sorry I set fourteen alarms for 3 a.m. instead of 7 a.m. "
    "and woke the whole house four hours early.\n"
    "I learned to read the time back out loud before I save an alarm, "
    "so 3 and 7 never trade places again."
)

# Gate self-check: exactly two lines, 1-400 code points, no trailing newline.
assert TEXT.count("\n") == 1 and 1 <= len(TEXT) <= 400


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, TEXT.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
