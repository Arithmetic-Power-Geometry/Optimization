# E16 reproduction and execution classification
Date: 2026-10-21.

**EXECUTED:** GitHub connector source/cleaned-graph consistency checks, 720 JS-generated synthetic-failure episodes, 15 paired JS bootstrap comparisons, GitHub commits and independent re-fetches.

**NOT EXECUTED:** Python E15 validator `python extension/data/e15_validate.py`, Python E16 reproducer `python extension/experiments/e16_matched.py`, GitHub Actions CI, packet simulator, full E13 preregistered statistical plan.

Run from a complete checkout:
```sh
python extension/data/e15_validate.py
python extension/experiments/e16_matched.py
```
The E16 Python reproducer calls E15 `verify()` before comparing the 720 frozen CSV rows. The E16 script is a cross-language reproduction specification, not an executed independent replication. E16 matched data: `extension/results/E16_MATCHED_EPISODES.csv`; descriptive paired intervals: `extension/results/E16_PAIRED_BOOTSTRAP.json`. Fixed seed list from E13_MANIFEST.json. Explicit graph/probe/budget semantics and bootstrap algorithm in E16_METRIC_DEFINITIONS.md. No hidden-state observations supplied to policy ranking.

Reproducibility caveat: JavaScript `localeCompare` lexical ordering can differ from Python Unicode sorting for punctuation and numeric edge labels; verify the Python reproducer against frozen CSV before accepting cross-language equivalence. Until that succeeds, exact cross-language bitwise replication is OPEN.
