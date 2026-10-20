# E10 — Reproducibility and evidence boundaries
Date: 2026-10-20. Status: EXECUTED locally; independently GitHub-refetched code verified against Git blob hashes.

## Run from repository root
```sh
python -m unittest discover -s extension/tests -p 'test_*.py' -v
```
Python 3.11+; standard library only, no installation or random seeds. The E09 original two files were reconstructed byte-for-byte in the local execution environment and checked using Git blob SHA-1 against GitHub (physical_graph.py e26f6e758ce22f162fb4afd0935f94601a3ba826; test_physical_graph.py b0f4bfe5cdd46aea4a8ede97b4514e3f900145f3). The three E10 source/test files were also locally executed before committing; verify the committed blob hashes against local byte-identical versions.

## Executed tests
12 E09 regression tests passed, followed by 8 E10 golden test methods; combined run 20 tests, 0 failures, 0 errors. E10 loops cover n=2,3,4,5 for the n-edge 1/n case, n=2,3,4 for exhaustive repair, and both E06 gate states. No CI run is claimed. Runtime is an execution-environment observation, not a network benchmark.

## Independent validation method
`exact_oracle.solve` is a memoized finite-horizon dynamic program over hypothesis-labeled states, taking AND over possible probe outcomes for robust feasibility and sum over branches for Bayesian success. `independent_checker.check` enumerates attainable terminal success bitmasks of full contingent action trees without Bellman value maximization; tests compare exact fractions and robust feasibility. Both intentionally share the E09 transition kernel; therefore this is **algorithmically independent enumeration**, NOT independent physical transition implementation or external referee validation.

## Critical scope restrictions
- Finite deterministic noiseless observations and deterministic guaranteed-success edge restorations; no noisy or stochastic repair outcome branches.
- Only individual existing-edge repairs; no composite maintenance action, bypass installation or monitor enabling action in the oracle.
- Repair feedback is modeled as publicly deterministic SUCCESS; no hidden-state dependent failure feedback.
- Hypotheses must have the same initial public budget. The oracle does not separately prove that all other public configuration is indistinguishable: **caller must ensure a valid common information pattern**.
- Probe admissibility checked across all live hypotheses, so no hidden feasibility oracle. Branching on binary UP/DOWN only.
- All probes and repairs have unit resource and time costs; horizon finite; no heterogeneous costs or continuous time.
- `nodes` is the count of memoized DP states visited, not graph vertices, policy complexity or measured speedup.
- Exhaustive policy enumeration scales exponentially. No large-graph results, novelty, accuracy generalization or field measurements.
- This is not a POMDP solver with arbitrary stochastic transitions.
