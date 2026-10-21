# E17 reproduction gate
Python 3.11+ stdlib, from full repository checkout:
```sh
python extension/data/e15_validate.py
python extension/experiments/e16_matched.py
python extension/experiments/e17_ablation.py
```
All three commands are **NOT EXECUTED** in E17. The last script independently compares the committed 960-row CSV with deterministic reconstruction, after invoking E15 validation. Source GraphML and cleaned tables must be present locally. E16 Python script also has a documented possible JS localeCompare/Python ordering discrepancy; if reproduction fails, diagnose and fix the implementation, never rewrite the historical raw CSV to disguise discrepancies.

The 960 CSV rows and 24 descriptive summary cells were generated via JavaScript over connector-verified graph edge tables. The 20 seeds are identifiers for deterministic fault schedules, not iid stochastic draws. This stage did not compute bootstrap CIs or hypothesis tests. All outcomes are exact deterministic indicators for the restricted fixed-path model, not empirical physical repair measurements.
