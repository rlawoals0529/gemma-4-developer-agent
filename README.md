# gemma-4-developer-agent

JAgent is my entry for the Google Gemma 4 Developer Agent Competition.

The task is simple to state and hard to fake: given a real software issue and a repository, the
agent has to produce a patch that passes hidden validation. The score is the fraction of issues
resolved.

## The rule

**A change stays only if it fixes a reproducible failure or moves the benchmark.**

A larger prompt, another agent, or a more elaborate workflow is not an improvement by itself. I
want each version to leave behind enough evidence to explain why it exists.

## Measured baseline

`JAgent v0.1` used one Gemma agent, all nine harness tools, no sub-agents, no custom skills and no
LoRA adapters. Its public Kaggle score was **0.05**.

That number is the control. Everything after it has to justify the extra complexity.

## Current candidate

`JAgent Atlas v2.0` is the current architecture. Instead of forcing every issue through a long
multi-agent pipeline, it uses a short default path and only escalates when the trajectory shows
uncertainty:

- exact search before graph search;
- one main coding agent;
- a deep-localization skill for ambiguous repository navigation;
- a hard-debug skill for failed first hypotheses;
- an optional fresh-context patch critic;
- explicit no-progress and wall-clock brakes;
- a four-minute per-task cap to protect the global evaluation budget.

Atlas is a candidate, not a claimed improvement. Its score belongs here only after official
evaluation.

The exact candidate bundle lives under [`submission/`](submission/), not only inside a notebook.
That makes prompt and config changes normal git diffs.

## Build the submission

```bash
python scripts/package_submission.py
```

That writes `submission.zip` with the contents of `submission/` at the archive root and fails if
one of the required Atlas files is missing. The current bundle packages nine files and has been
smoke-tested locally before being committed here.

## Why this repository exists

The competition is useful because the result is external. A prompt can sound disciplined while
solving nothing. Here I can keep the prompt, configuration, submission bundle, experiment notes
and official score beside one another.

[`experiments/`](experiments/) records each version, what changed, what I expected, what actually
happened and whether the idea stayed. The v0.1 control, Prime architecture jump, and Atlas redesign
are recorded separately rather than flattened into one final story.

## Harness constraints that shape the design

The competition runs one allowed Gemma 4 base model with a 32,768-token context ceiling. The
submission is declarative YAML plus prompts, skills, optional sub-agents and optional LoRA
adapters. The harness exposes repository tools, runs the agent in a sandbox, extracts its git diff,
and verifies the patch separately against hidden tests.

That separation is why the agent is told to fix production code rather than tests, keep scratch
reproductions outside the repository, and submit only after checking the final diff.

Competition: [Google - The Gemma 4 Developer Agent Competition](https://www.kaggle.com/competitions/gemma-4-developer-agent)

## Status

The v0.1 baseline is measured. Atlas v2.0 is committed as an inspectable submission bundle and is
ready for the next official run. The next useful change should contain a result, a reproduced
failure, or a modification tied to one of those.
