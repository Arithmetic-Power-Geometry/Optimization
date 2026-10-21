# E16 — Matched comparative topology experiments
Date: 2026-10-21.

## Data gate
Fetched E15 topology manifest, three original GraphML files and six cleaned CSVs through the GitHub connector. Independently compared all three raw Git blob SHA-1s and six cleaned blob SHA-1s against the frozen manifest, parsed GraphML node/edge structures and confirmed byte-exact regenerated cleaned tables. All three passed. **Python E15 validator was NOT executed** (GitHub DNS unavailable to local container). This distinction is important.

## Executed study
JavaScript execution over verified acquired graph tables produced **720 raw policy-episode rows**: 3 historical topologies × 20 paired seeds × 2 budgets × 6 policy labels. All faults were synthetically injected on one fixed longest-shortest route per topology. One route edge was failed per episode; no real failures. Six policy labels are restricted route-edge ordering comparators, NOT direct executions of E11 Python baseline policies. Full-path probe right was available but unused by all policies. Results are exact 0/1 indicators for fixed-path restoration. Uniform-prior theoretical optimal expectation min(r,L)/L, with no distinguishing probe.

## Executed descriptive uncertainty
Computed 15 per-topology paired comparisons (five policies versus a feasible first-r uniform-prior-optimal ordering), each with 20 paired seed units and 2,000 deterministic percentile bootstrap resamples. Stored raw paired differences and 95% descriptive intervals in E16_PAIRED_BOOTSTRAP.json. Intervals do NOT justify statistical generalization because failures were deliberately balanced, not iid.

## Negative and scientific decision
Theoretical expected success is identical for any fixed r-edge restoration order. Differences in the 720 deterministic observed indicators do not demonstrate improvement, novelty or superiority. E16 is **PARTIAL GO** for reproducible, source-verified historical-topology synthetic-fault comparison; **NO-GO** for claims of a superior algorithm, real-world network validation, statistically significant improvement or published HEC comparison. Python E15/E16 scripts remain UNEXECUTED; CI remains inactive; CAIDA remains BLOCKED; original eight-page manuscript byte snapshot remains BLOCKED. E17 requires explicit author approval and must test alternative routing, genuinely informative feasible probes, and sensitivity to priors/fault regimes before stronger claims.
