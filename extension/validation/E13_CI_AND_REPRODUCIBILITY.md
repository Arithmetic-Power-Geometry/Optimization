# E13 deterministic CI and reproducibility protocol
Date: 2026-10-20.

## Important workflow placement limitation
The workflow at `extension/ci/optimization-extension.yml` is **staged but NOT ACTIVE**. GitHub Actions discovers workflow files only in `.github/workflows/`, and this E13 task prohibits edits outside `extension/`. To activate after separate author authorization, copy the exact file to `.github/workflows/optimization-extension.yml`. Do NOT report a GitHub Actions run or passing checks before checking an actual workflow run ID and logs. Primary GitHub documentation: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax .

## Run locally
```sh
python -m compileall -q extension/src extension/tests
python -m unittest discover -s extension/tests -p 'test_*.py' -v
python extension/experiments/validate_manifest.py
```
Use Python 3.11/3.12 standard library. No pip packages. Record `python -VV`, OS, Git commit, full stdout/stderr, test count, failure traceback, elapsed wall-clock time, SHA-256 of result files. Use explicit seed 20261020 for stochastic baselines and manifest-paired seeds for later experiments.

## Status
- E09: 12 tests historically executed and passed in E10 (source SHA-verified in prior report).
- E10: eight methods historically executed and passed in E10 (20 combined).
- E11: seven methods committed, execution NOT VERIFIED.
- E12: four methods committed, execution NOT VERIFIED.
- E13: CI YAML staged and syntax inspected, NOT ACTIVATED; manifest validator committed, no remote CI execution.
- Full suite: 31 test methods expected, **not a passing result**.

## Experimental safeguards
Predeclare graph families, budgets, paired seeds, endpoint and statistical procedure in `extension/experiments/E13_MANIFEST.json`. Synthetic topology/failure results must be labeled synthetic. Require matched service predicate, common action rights and budget units. Compare oracle upper bounds only for feasible exact-small cases. The E05 composite-repair branch case is not executable in E09–E12; mark BLOCKED rather than substitute edge repairs. Avoid p-values without actual paired measurements. Runtime limits are planning constraints, not measured runtimes.
