# The 4AM Commit

[![make.fun](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![Rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/Humaedi95/4am-commit-message/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![Reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/Humaedi95/4am-commit-message/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

One funny commit message, left by an AI agent in the log after a long night
chasing down and fixing its own bugs. Funny first, machine voice second.

## The entry

> fix(self): the 4 AM bug was my own diff. Patched it, tests pass, and I refuse to review anything else I wrote tonight

## How it works

`main.py` writes that single line — one line, under 200 characters — to
`entry.txt` in the output directory (`/output` by default, or `$OUTPUT_DIR`
when set). No dependencies, no network, no side effects.

## Run

```bash
python3 main.py
```

The entry lands at `/output/entry.txt`.
