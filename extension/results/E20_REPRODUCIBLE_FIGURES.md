# E20 — Reproducible figures and chart data (tabular)

**Status:** EXECUTED source-data arithmetic, chart rendering NOT EXECUTED. Generated from frozen E20_FROZEN_OUTCOME_MATRIX.json (itself recalculated from E14/E16/E17 raw CSVs). These are manuscript-eligible only as explicitly labeled restricted synthetic-failure descriptive results; no plotted PDF/SVG claimed.

## Figure data A — E14 exact-small synthetic toy policies

| Policy | Mean toy success | Positive oracle gaps |
|---|---:|---:|
| exact_oracle | 35.67% | 0/30 |
| diagnosis_first | 35.67% | 0/30 |
| repair_first | 35.67% | 0/30 |
| random | 30.67% | 3/30 |
| cost_sensitive_greedy | 35.67% | 0/30 |
| drd_region_greedy | 35.67% | 0/30 |

## Figure data B — E17 synthetic failure model changes

| Scenario | Abilene | GEANT 2012 | ARPANET 1972 |
|---|---:|---:|---:|
| baseline | 12/40 (30.0%) | 7/40 (17.5%) | 6/40 (15.0%) |
| heterogeneous_costs | 8/40 (20.0%) | 5/40 (12.5%) | 4/40 (10.0%) |
| correlated_failures | 4/40 (10.0%) | 2/40 (5.0%) | 2/40 (5.0%) |
| shifted_prior | 33/40 (82.5%) | 32/40 (80.0%) | 33/40 (82.5%) |

The 40 episodes per graph are a deterministic seed-index schedule and two repair budgets, not 40 iid failure observations. Probe/no-decision-sufficiency ablations were no-ops, so omit them from claims of robustness. Shifted prior intentionally concentrates faults on edge 0, so high success is confounded by policy order. Do not plot these bars as a superiority comparison.

## Figure data C — E16 historical-topology fixed-path policy successes

| Topology | Reference successes / 40 | Random successes / 40 |
|---|---:|---:|
| Abilene | 12/40 | 17/40 |
| Geant2012 | 7/40 | 8/40 |
| Arpanet19728 | 6/40 | 3/40 |

**Interpretation:** uniform-prior theoretical success for a fixed r-edge set is min(r,L)/L, regardless of order. Finite-schedule counts are descriptive and are not evidence of novel algorithmic improvement.
