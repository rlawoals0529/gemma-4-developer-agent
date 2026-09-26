# Atlas v2.0 - adaptive SWE agent

Date: 2026-09-26

Starting point:
Measured control: JAgent v0.1 = 0.05 public score.

Question:
Can the agent keep a short path for obvious fixes while spending extra context and review only on
issues that show evidence of ambiguity?

Change:
Atlas keeps one root coder and moves expensive behavior behind triggers. Exact search comes before
graph search. `deep-localization` and `hard-debug` are skills loaded only when needed. A fresh
`patch_critic` is available for uncertain or multi-file patches rather than running on every task.
The per-task time budget is four minutes with explicit no-progress brakes.

Cost:
Tool-call budget: 55
Time budget: 4 minutes per task
Permanent prompt/context added: one root prompt; skill and critic context are conditional

Result:
Local resolution rate: pending
Kaggle public score: pending
Rank at submission time: pending

What is already testable:
The bundle validates structurally and contains the intended Atlas components. That proves packaging,
not software-issue resolution.

Decision:
pending official evaluation

Next:
Run the official evaluator unchanged. If the score moves, inspect which failure class actually
changed before adding another architectural component.
