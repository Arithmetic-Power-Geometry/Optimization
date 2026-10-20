# E12 — Candidate policy and complexity audit
Date: 2026-10-20

## Work done
Read E12 prompt, existing E10 oracle, E11 baseline implementation and tests, preservation/progress contracts. Attempted to clone the GitHub repository into the isolated Python container to run E11 tests; network resolution failed (github.com could not resolve). **No E11 tests were executed in E12.** Static audit found a concrete E11 defect: the evaluator returned immediately at remaining==0 without recording service restored on the final action. Corrected extension/src/baselines.py and committed four new E12 regression methods in extension/tests/test_e12_candidate_gate.py. The correction remains unexecuted in the current environment.

## Algorithm gate
Compared three proposed candidate classes: decision-sufficient stopping, budget-aware greedy probe/repair selection and exact finite-horizon belief planning. All duplicate E10/E11 methods or classical DRD/POMDP formulations. Frozen rejection record documents termination and a loose exponential naive search-tree bound; **no technically distinct algorithm has been established**.

## Evidence classification
- EXECUTED: GitHub repository reads and commits, static source audit, failed local git-clone attempt, publisher original/CMU bibliographic check.
- NOT EXECUTED: E11/E12 unit tests; no 27/31 passing claim, no runtime benchmark, no measured improvement.
- ANALYTIC: finite horizon decreases by one per action; E10 model uses shared budgets and admissibility.
- NO-GO: novel E12 algorithm, approximation guarantee, original theorem.
- BLOCKED: original manuscript exact source snapshot.

## E13 entry gate
E13 can design CI/test protocol after explicit authorization, but it must execute the E11 and E12 suites in a network-accessible Python 3.11 runner, fix any remaining failures, record logs and pin environment before experimental claims. STOP before E13.
