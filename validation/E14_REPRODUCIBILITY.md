# E14 reproduction and provenance
Date: 2026-10-20. Actual execution: Linux x86_64, Python 3.13.5, standard library only.

From repository root:
```sh
python -m unittest discover -s extension/tests -p 'test_*.py' -v
python extension/experiments/e14_exact_small.py --output extension/results/E14_EXACT_SMALL.csv
```
Expected first command: 31 tests, no errors/failures in the recorded E14 environment. Second command generates 180 rows (30 instances times six policies), checks exact DP vs independent success-mask enumeration, checks budget and optimality bounds, and prints SHA-256. The script uses seed 20261020 for the random baseline. This is deterministic output except elapsed_ns timings, which depend on host scheduling and hardware. Therefore exact CSV SHA-256 is a **local run fingerprint**, not a cross-machine reproducibility requirement. For reproducibility compare non-timing fields.

Source SHA check: `extension/experiments/e14_exact_small.py` Git blob `abfbe0589803e9d7f82b5f5beacd0337c0e6183a`, matching locally executed script. `extension/results/E14_RAW_COMPACT.csv` Git blob `ba93cf145f279bed379df09c01b82ba86a6a699d`, matching local 180-row projection.

`extension/results/E14_TEST_EXECUTION.json` records all eight original Python source blob hashes and test count. No GitHub Actions run was claimed. E13's paired 20-seed, bootstrap and Holm protocol is still PLANNED; do not treat this restricted E14 microbenchmark as executing that protocol.
