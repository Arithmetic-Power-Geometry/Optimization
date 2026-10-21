# E17 — Ablation, sensitivity, stress: restricted execution report
Date: 2026-10-21.

Prompt E17 read and applied. Preserved all prior source and data; only extension/ files created or updated.

### Validation gate
E15 source GraphML and cleaned tables were independently re-fetched from GitHub and checked for matching recorded SHA/content (3 topologies). Local container cannot resolve raw.githubusercontent.com and does not have these mounted files. Therefore `python extension/data/e15_validate.py` and `python extension/experiments/e16_matched.py` **have NOT been executed**. The user's first gate is still BLOCKED; it must not be marked resolved.

### Executed restricted tests
Computed 960 deterministic JS episode records across 3 licensed historical topologies × 20 E13 seed identifiers × 2 budgets × 8 scenarios. CSV and 24-cell descriptive summary committed. No live failures, packet simulation or new graph data. Baseline is the first-affordable fixed-route repair policy; the nominal ablations for probing/decision sufficiency are intentionally unchanged or placeholder, and hence scientifically inconclusive. Real model changes: heterogeneous repair costs, adjacent correlated failures, severe nonuniform failure distribution; noisy observation is generated but ignored by policy, so it does not test robustness.

### Negative outcomes
All three pure/no-op ablations and ignored-noise case match baseline exactly. Correlated two-edge failure reduces recovery. Heterogeneous cost changes feasible repairs. Shifted prior dramatically favors the first-edge policy by construction. These are negative/sensitivity demonstrations, **not evidence of a new algorithm or statistical significance**.

### Execution status
JS computations and connector-level data checks EXECUTED; Python validators/reproducers NOT EXECUTED; no CI run; no external packet simulator; no HEC implementation. E17 PARTIAL GO for restricted sensitivity logs, NO-GO for the mandatory Python gate and for simulator readiness. E18 requires explicit authorization; E17 does not start it.
