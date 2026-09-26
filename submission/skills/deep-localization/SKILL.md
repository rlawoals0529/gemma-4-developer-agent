---
name: deep-localization
description: Deep repository localization for ambiguous software issues. Load only after focused exact search leaves multiple plausible implementation sites, or when callers/callees/registration/inheritance relationships determine the fix. Do not load for a task that already has an obvious edit site.
---

# Deep localization

The goal is to reduce the search space, not to read the repository.

1. **Re-anchor on the symptom.**
   Write down the exact behavior that is wrong and the first observable boundary where it appears.

2. **Extract concrete anchors.**
   Prefer names already present in the issue or source:
   - class/function/method names
   - exception/error strings
   - API parameters or field names
   - filenames/modules
   - test names

3. **Exact search before semantic search.**
   Use `git grep -n`/`rg` for anchors and inspect the nearest existing tests. Batch related searches in one command when possible.

4. **Use code-graph tools only with real symbols.**
   `search_similar_code` works best with a class/function/module symbol, not prose.
   Use `get_code_neighbors` when callers, callees, imports, or definitions affect the hypothesis.
   Use `get_code_subgraph` only when a small set of known symbols needs relationship context.

5. **Compare one working sibling.**
   Find a nearby path implementing similar behavior correctly. Differences often reveal the missing normalization, guard, state transition, or contract.

6. **Trace one path end-to-end.**
   Follow the failing value/control flow from public entry point to the earliest incorrect state. Stop once a minimal edit site plus affected callers is supported.

7. **Return to implementation.**
   Do not continue searching for completeness. Localization is finished when you can name:
   - the likely root-cause symbol;
   - why it violates the requested behavior;
   - the smallest production change;
   - which caller/writer/test should falsify that hypothesis.
