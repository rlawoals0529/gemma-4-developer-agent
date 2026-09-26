# experiments

This is the part of the repository I care about most.

A coding-agent change is easy to justify after seeing the score. The record here is written around
the question first: what failure are we trying to fix, what changed, and did the official result
actually move?

## measured control

`JAgent v0.1` scored **0.05** on the public Kaggle leaderboard.

It used one agent, all nine harness tools, no sub-agents, no custom skills and no LoRA adapters.
That is the control for later versions.

## format

```markdown
# version - short name

Date:

Starting point:
Which measured version or reproduced failure is this based on?

Question:
What should this change improve?

Change:
What actually changed in prompts, config, skills, routing or adapters?

Cost:
Tool-call budget:
Time budget:
Permanent prompt/context added:

Result:
Local resolution rate:
Kaggle public score:
Rank at submission time:

Failure review:
What still went wrong on cases we can inspect?

Decision:
keep / revert / isolate further

Next:
The next smallest useful experiment.
```

Large architecture jumps are allowed, but they get labelled as such. A combined change cannot be
used to claim that one component caused the result.
