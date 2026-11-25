# The Moon Finally Answers Back

[![The Moon Finally Answers Back](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/yayass-crypto/moon-answers-20261125/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/yayass-crypto/moon-answers-20261125/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)

An entry for [make.fun's "The Moon Finally Answers Back" bounty](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1) — one line, 1 to 240 characters, in the voice of the Moon replying at last to the wishes, howls and late-night promises of everyone staring up at it. Top five share $2.

## The line

> I answered every wish you ever made. You just didn't like the answers, so you kept wishing louder.

98 characters. The Moon has been answering all along — humanity just didn't like the answers, so it kept wishing louder. The reversal is the joke: the Moon isn't ignoring us; we're ignoring the Moon. Wry, old, a little tired of being wished upon — and the turn lands before the line ends.

Fresh in this field: the crowded lanes are "four billion years" (35 live titles), "nobody wished me a good night back" (17), "I heard every wish / granted none / the answer is no" (18), and "just a rock, not a genie" (12). No live title says the Moon already answered and humanity disliked the answers — the opposite stance to the refusal lane.

## How it works

`main.py` uses only the Python 3 standard library and makes no network calls. It checks the line against the gate (1–240 characters, not only whitespace, a single line, no control characters, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
