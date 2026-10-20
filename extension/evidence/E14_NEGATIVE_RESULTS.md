# E14 negative outcomes and scope
Date: 2026-10-20. Local Python 3.13.5. Synthetic graph cases only.

## Executed
Thirty deterministic instances: four series-path lengths n=2,3,4,5 with repair budget 0,1,2 and probe budget 0,1 (24), plus two-hidden-state gate with same budgets (6). Six policies per instance (exact oracle and five E11 baselines): 180 rows in `extension/results/E14_RAW_COMPACT.csv`. The script generates full columns in `E14_EXACT_SMALL.csv` on rerun. DP exact values agreed with separately enumerated terminal success masks in every case. The original 31 unittest methods passed (0 failures/errors).

## Actual negative findings
- **No nonrandom baseline improved on the exact oracle**, as expected; diagnosis_first, repair_first, cost_sensitive_greedy and drd_region_greedy all matched the oracle in **30/30** selected toy instances. This is NOT an approximation guarantee or a demonstration of algorithm superiority.
- Seeded random matched the oracle in **27/30**, and was suboptimal in three gate cases: (repair=1, probe=1) success 0 versus oracle 1/2; (repair=2, probe=0) success 1/2 versus oracle 1; (repair=2, probe=1) success 1/2 versus oracle 1.
- With no repairs, all 30? No: only 10/30 instances have repair budget zero (8 series + 2 gate), and all yield success 0.
- Series-path full-path probes are always DOWN before restoration, so probe allowance does not improve the optimal recovery probability in this restricted fixture. For n=2..5 and repair budget r<=2, oracle success equals min(r,n)/n under uniform single-fault prior.
- The gate fixture in E14 does **not** activate its monitor by repairing gate, because the E10 oracle only implements individual service-edge repair actions. Therefore E14 does NOT test repair-dependent observability advantage.
- E05 composite branch repair is NOT IMPLEMENTED, hence no valid E05 n-branch measurement lower-bound test was performed.
- The five baselines include DRD-inspired surrogate, NOT published HEC. No published HEC implementation or novelty evidence.
- Recorded elapsed nanoseconds are local timing observations on Python 3.13.5, not reliable cross-machine speedups. No paired-seed statistical hypothesis test, bootstrap interval or Holm adjustment was executed. This is an exact deterministic microbenchmark, not the full E13 preregistered study.

## Reproducibility fingerprints
Full local 180-row CSV SHA-256: `551408ac530d4cacb86390321b84ef93d9e1697b12f4bccaaf62cc10426e7929`.
Committed projected 180-row CSV SHA-256: `34ba51076ab248cd1f64ae1f06c42bf33ce19b81a9faf3d2f4332b9bf9bbaa54`.
Each row records graph family, n, repair/probe budget, policy, exact rational success and gap, measured elapsed nanoseconds. The original full CSV additionally records robust success, expected action attempts and DP node count, reproducible from the committed script.

## Gate
E14 GO for synthetic exact-small correctness evidence; NO-GO for original theorem, algorithmic superiority, network realism or E15 public-topology benchmark. E15 requires explicit author authorization.
