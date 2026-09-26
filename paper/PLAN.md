# paper plan

The paper track should come from the experiment record, not from rewriting the final system as if it
was obvious from the beginning.

## question

Does adaptive disclosure of agent complexity improve software-issue resolution under a fixed
wall-clock budget compared with a plain single agent or an always-on multi-stage workflow?

The useful part of that question is the budget constraint. More agents can make a trace look more
careful while spending time and context that could have gone to later tasks.

## evidence we already have

- JAgent v0.1 is a measured single-agent control with a public score of 0.05.
- Prime v1.0 is the intentionally expensive contrast: scout, root coder, reviewer.
- Atlas v2.0 moves localization, hard debugging and fresh-context review behind evidence-based
  triggers instead of paying for them on every task.
- the exact Atlas prompt/config/skills live in this repository, so the paper can point to the
  implementation rather than paraphrase it.

## evidence still required

Do not write a result section until these exist:

1. official Atlas public score;
2. local/public evaluation on the same candidate bundle where possible;
3. per-task or sampled trajectory review grouped by failure class;
4. runtime and tool-call counts for representative easy and hard tasks;
5. at least one ablation that removes a major Atlas component;
6. examples where escalation helped and examples where it only added cost.

## ablations worth paying for

Priority order:

1. **fast lane only** — root prompt, no skills, no critic;
2. **+ skills** — conditional localization/debugging, no critic;
3. **+ critic** — full Atlas;
4. only after those, sampling or budget changes.

Changing architecture, sampling and time limits together would make a better competition guess but
a worse experiment. Keep the paper runs narrower than the all-in competition runs.

## failure labels

Use a small set that can be applied consistently when reviewing traces:

- wrong localization;
- correct file, wrong root cause;
- correct idea, bad implementation;
- insufficient verification;
- over-broad patch;
- budget exhausted before a stable patch;
- critic caught a real blocker;
- critic added no useful information.

If a trace does not fit cleanly, keep the raw note instead of forcing a label.

## paper shape

1. problem: fixed-budget SWE agents spend compute unevenly;
2. control: simple single-agent JAgent;
3. failed/expensive direction: always-on Prime workflow;
4. method: Atlas fast lane plus conditional skills and critic;
5. evaluation: resolution rate, runtime/tool use, failure classes;
6. ablations;
7. limitations: public leaderboard size, hidden-task uncertainty, coupled prompt changes;
8. practical takeaway: complexity should be triggered by evidence, not made mandatory by the
   architecture.

## rule

If the measurements do not support the thesis, the thesis changes. The paper is not allowed to
turn a competition architecture into a success story just because it is already built.
