# Prime v1.0 - all-in workflow

Date: 2026-09-26

Starting point:
JAgent v0.1 public score: 0.05.

Question:
Does adding isolated diagnosis plus an independent patch review improve hidden-task resolution enough
to justify the extra fixed cost?

Change:
This was intentionally a combined architecture jump rather than a clean ablation. Prime used a
root coder, a read-only repository scout, and a fresh-context patch reviewer. The root workflow was
localize, reproduce, patch, verify, review, revise if needed, then submit.

Cost:
More permanent instructions, more agent calls, and review work paid on every task.

Result:
Local resolution rate: not recorded
Kaggle public score: not recorded
Rank at submission time: not recorded

What I learned before scoring:
The architecture is easy to explain but expensive by construction. Simple issues pay for the same
multi-stage ceremony as difficult ones, which makes it a poor default under a fixed global runtime
budget.

Decision:
do not treat individual Prime components as proven by this experiment; use it as the contrast that
motivated Atlas' adaptive path

Next:
Keep the useful ideas, but make expensive localization and review conditional rather than mandatory.
