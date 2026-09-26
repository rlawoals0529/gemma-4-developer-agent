---
name: hard-debug
description: A bounded diagnosis loop for hard bugs. Load after the first evidence-backed fix fails, when the observed failure does not match the report, or when there is no falsifiable root-cause explanation. Avoid for straightforward localized fixes.
---

# Hard debug

Use this only after the fast lane has failed or the bug is genuinely ambiguous.

## 1. Build the tightest red-capable signal available

Preference order:
1. an existing focused test that exercises the reported behavior;
2. a small invocation of the real public interface;
3. a `/tmp` script or inline assertion;
4. source-path tracing if execution is genuinely impractical.

The signal must distinguish the reported bug from "didn't crash". Do **not** add a repository test merely to satisfy this ritual.

## 2. Confirm you are debugging the same bug

Record the exact wrong output/error/state. If your reproduction fails differently from the issue, do not optimize against the wrong failure.

## 3. Generate 2-3 falsifiable hypotheses

For each:
- cause;
- evidence already supporting it;
- one cheap observation that would make it less likely.

Test the cheapest discriminator first. Change one variable at a time.

## 4. Minimize only as far as it saves time

Full delta-debugging is unnecessary when the failing path is already small. Remove distractions until the root cause is clear enough to patch.

## 5. Patch the cause and re-run the original signal

The post-fix check must exercise the same behavior that was red before. Then inspect related callers/writers for the same class of bug.

## 6. Brake

If two patch/check cycles produce no new evidence, stop editing and re-localize.
If time is low, prefer the best evidence-backed minimal patch plus a clean diff over further speculation.
