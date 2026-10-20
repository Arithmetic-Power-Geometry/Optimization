# E11 — Reproducible baseline fairness test plan
Python 3.11+ standard library only. No external dependencies.
```sh
python -m unittest discover -s extension/tests -p 'test_*.py' -v
```
Seven E11 unittest methods added; combined expected suite is 27 methods (12 E09 + 8 E10 + 7 E11). **Expected count is not a measured passing count.** E11 tests are unexecuted until a Python runtime checks out the committed files. Golden fixtures: E06 gate two faults; budgets 0/1/2; oracle ceiling; seeded random reproducibility; weighted priors; no spurious claim to exact HEC. Use seed 20261020 by default; no randomness in other policies.

Gate: Do not report numeric baseline results, timing, win rates or superiority before execution. If tests fail, preserve logs and fix code under extension/ with an independent re-fetch. E12 needs explicit authorization.
