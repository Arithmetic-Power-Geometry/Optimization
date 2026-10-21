# E20 independent replication and evidence freeze — 2026-10-21

## Exact prompt and preservation
Read E20.md, extension README and progress; inspected E14–E19 source evidence, raw datasets, outcome summaries and protocol. All E20 commits restricted to extension/. Original 20-stage NO-GO preserved.

## Actually executed independent audits
Fetched E14 (180 rows), E16 (720 rows), E17 (960 rows) raw files from the connected GitHub repository. Independently parsed them and recomputed E14 fractional success and positive oracle gaps (3 random-policy negative cases); E16 service success from failed/repaired edges, repair budget, matched six-policy groups (120 groups), and 15 paired seed mean differences against feasible reference; E17 all 960 success indicators, repair-cost constraints and 24 group summaries. **Zero CSV integrity errors and zero paired mean discrepancies found.** Frozen recomputed outcome matrix committed at E20_FROZEN_OUTCOME_MATRIX.json. This was JavaScript arithmetic over independently fetched frozen GitHub content, not fresh Python execution.

## Not independently replicated
E09–E12 31 tests passed during E14, but E20 did NOT run them in a clean Python checkout. E15 GraphML Python validator, E16 and E17 Python reproducers NOT EXECUTED; E16 Python/JS lexicographic ordering discrepancy remains OPEN. E16 bootstrap interval bounds NOT independently regenerated (paired means only). No figures were rendered from local Python; E20 chart data table was derived from raw CSV and committed. E13 full 10k-resample/Holm plan NOT EXECUTED; GitHub Actions inactive. E18 Mininet and E19 ns-3 not installed; no packet simulations or actual repair measurements.

## Independent evidence/novelty gate
Primary Javdani et al. 2014 PMLR AISTATS DRD/HEC publication directly establishes decision-region identification with overlapping regions and greedy HEC; these cannot be represented as new here. Network tomography and DDID remain collision risks. E06 false theorem retracted; E08 originality NO-GO remains. E12 algorithm duplicate, E14 nonrandom ties, E16 uniform-prior ordering equivalence, E17 no-op ablations and prior shift confounding remain negative evidence.

## Freeze verdict
**E20 PARTIAL evidence freeze / NO-GO for full independent replication and manuscript submission.** Frozen matrix, claim ledger, reproducible chart data and blocker register committed. The original eight-page manuscript bytes still absent; do not proceed with E21 manuscript integration without recovering exact original source. STOP before E21.
