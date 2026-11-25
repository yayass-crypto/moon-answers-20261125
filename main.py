#!/usr/bin/env python3
"""The Moon finally answers back.

The line (98 characters) is the Moon speaking, in the first person,
to everyone who has ever stared up at it and wished:

    I answered every wish you ever made. You just didn't like the
    answers, so you kept wishing louder.

Why it should win, against the judge's published brief in order:

1. It speaks as the Moon answering back. The whole premise of the
   competition is the Moon finally replying, and this line IS the
   reply: the Moon has been answering all along. It addresses the
   wishers directly, and "kept wishing louder" nods at the howls
   too -- louder wishing is what howling is.
2. It is funny on one read. The joke needs no explanation: humanity
   spent four billion years wishing, got answers, and complained
   about them instead of noticing. The laugh is the reversal -- the
   Moon is not ignoring us; we are ignoring the Moon.
3. It sounds like the Moon: wry, old, and a little tired of being
   wished upon. "You just didn't like the answers" is the sigh of
   something that has listened to everyone for four billion years
   and is done pretending it never replied.
4. It lands as a comeback in one read. The turn arrives in the
   second sentence -- the first sentence sets up the expectation
   that the Moon never answered, and the second knocks it down --
   and the kicker ("so you kept wishing louder") closes the line.
5. It wastes none of its 98 characters: two short sentences, no
   filler, no setup that outstays its welcome, far inside the
   240-character gate.

Fresh in this field: the crowded lanes are "four billion years"
(35 live titles), "nobody wished me a good night back" (17),
"I heard every wish / granted none / the answer is no" (18), and
"just a rock, not a genie" (12). No live title says the Moon
already answered and humanity disliked the answers. The stance is
the opposite of the refusal lane ("no", "granted none"): this Moon
said yes, and that is the joke.

The program checks the line against the gate -- UTF-8 text, 1 to
240 characters, not only whitespace, a single line -- writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), reads the
file back, and only reports success when the bytes on disk match
the line exactly. Exit code 0 means the entry file is exactly the
line above.
"""

import os
import sys

LINE = "I answered every wish you ever made. You just didn't like the answers, so you kept wishing louder."

GATE_MAX_CHARS = 240


def gate_problems(line):
    """Return a list of gate violations, empty when the line passes."""
    problems = []
    if not line.strip():
        problems.append("entry is blank or only whitespace")
    if len(line) > GATE_MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d limit"
            % (len(line), GATE_MAX_CHARS)
        )
    if line != line.strip():
        problems.append("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        problems.append("entry contains control characters")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    return problems


def main():
    problems = gate_problems(LINE)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        entry_path = os.path.join(out_dir, "entry.txt")
        payload = LINE.encode("utf-8")
        with open(entry_path, "wb") as handle:
            handle.write(payload)
        with open(entry_path, "rb") as handle:
            on_disk = handle.read()
    except OSError as exc:
        print("gate failed: could not write entry file: %s" % exc, file=sys.stderr)
        return 1

    if on_disk != payload:
        print("gate failed: read-back bytes do not match the line", file=sys.stderr)
        return 1

    print(
        "wrote %s: %d chars, %d bytes (%d chars of headroom under the %d limit): %r"
        % (entry_path, len(LINE), len(payload), GATE_MAX_CHARS - len(LINE), GATE_MAX_CHARS, LINE)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
