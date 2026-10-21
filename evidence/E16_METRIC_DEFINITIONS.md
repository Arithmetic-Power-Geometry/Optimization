# E16 metric definitions and frozen feasibility contract
Date: 2026-10-21. **Real historical topology; injected failures synthetic.**

## Frozen before final matched run
Topologies: three E15 source-verified Zoo graphs. Fixed deterministic route: the first longest BFS shortest path found by scanning sources in increasing node ID, BFS neighbors in increasing node ID, retaining first longest path. Each graph contributes one path, not a representative sample of all source-destination pairs: Abilene 0-1-10-7-6-3 (5 edges); Geant2012 11-13-12-15-9-8-7-34-33 (8); Arpanet19728 1-10-4-7-20-19-6-28-0-26 (9).

Each episode has one synthetic failed edge on this fixed route, no other failed edges. Monitor rights only at route endpoints, one end-to-end CSP probe permitted, but all evaluated policies perform **zero probes**. Full-path DOWN would not distinguish which edge failed; no privileged truth-state access. Available actions: restore one named path edge, unit repair cost; budgets r in {1,2}, probe budget 1, total time budget r+1. Distinct repairs only. Same failure, budgets, path and service predicate for every policy.

Primary endpoint `service_success`: indicator (0 or 1) that the repaired set contains the injected failed edge, thus restores the selected **fixed path**. This is NOT whole-network reachability or actual field restoration. `oracle_expected_success` is the uniform-prior theoretical ceiling min(r,L)/L when the failed edge is unknown and no informative observation is taken. The column `exact_uniform_oracle` is a feasible predetermined policy that selects the first r path edges; it is **not a hindsight oracle** and can have lower/higher finite-sample realized success than other policies. No policy observes the injected fault index before acting.

Policy labels are **restricted E16 adaptations**, not executions of the E11 `baselines.py` algorithm on full graphs:
- exact_uniform_oracle: first r route edges (uniform-prior optimal expected value; all r-subsets tie);
- repair_first: lexicographically ascending endpoint-labeled edges;
- diagnosis_first: lexicographically descending endpoint-labeled edges (no diagnostic probe taken);
- cost_sensitive_greedy: descending sum of endpoint degrees;
- drd_region_greedy: ascending sum of endpoint degrees (**not published DRD/HEC**);
- random: deterministic seeded Fisher-Yates shuffle using specified 32-bit LCG.

Seed list: 20 E13 preregistered integers. Fault schedule is `(seed_index + topology_index) % route_length`, where seed_index is 0..19, and topology_index is 0..2. **This is deliberately balanced deterministic enumeration, not independent random failure sampling.** Random policy uses `seed` to choose a permutation; failure position is not drawn from that seed. An earlier unbalanced modular formula was rejected during E16 exploratory work because it produced degenerate failure frequencies; the final committed raw results use the balanced schedule.

## CI and interpretation
Paired difference per seed = mean service_success across budgets 1 and 2 for policy minus the same mean for the feasible exact_uniform_oracle policy. Per-topology 20 paired seeds, 2,000 percentile bootstrap resamples, fixed LCG seed 20261021 restarted per comparison; interval endpoints are empirical quantiles indexed 49 and 1949 of 2000 sorted bootstrap means. This bootstrap is **descriptive only**, because the balanced fault schedule is deterministic and the 20 seeds are not independent random network/failure draws. No p-values, Holm-adjusted significance, cross-topology generalization or network-level confidence claims.

The GitHub-fetched raw files and cleaned CSVs were checked against E15 manifest and GraphML-derived content through the GitHub connector; the Python E15 validator and Python E16 reproducer are committed but were NOT executed locally. The 720 episodes and 15 paired bootstrap comparisons were **executed in JavaScript** against actual fetched topology edge tables; they are not Python runner logs.
