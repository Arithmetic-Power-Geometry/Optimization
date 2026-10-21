# E20 verification instructions
From a clean, complete GitHub checkout (not run in E20):
```sh
python -m unittest discover -s extension/tests -p 'test_*.py' -v
python extension/data/e15_validate.py
python extension/experiments/e16_matched.py
python extension/experiments/e17_ablation.py
```
Do not claim these commands passed until their stdout/stderr, exit codes, Python version, OS, full checkout hash and raw data blob hashes are captured. E16 cross-language ordering mismatch may need diagnosis. E20 actually executed an independent JavaScript read-and-recompute audit on GitHub connector-fetched E14, E16 and E17 raw CSVs. The E20 frozen outcome matrix contains machine-readable recomputed counts and means; E20_REPRODUCIBLE_FIGURES.md contains values regenerated from the matrix. E16 percentile bootstrap interval replication, E13 Holm correction, active CI and simulator traces remain OPEN.

No original manuscript was edited. All fault events in E16/E17 are synthetic, not field failures.
