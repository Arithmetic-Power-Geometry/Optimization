# E08 — Adversarial theorem decision record (GO/NO-GO)
Date: 2026-10-20. Stage E08 only. **Submission-level originality: NO-GO.** No independent referee, exhaustive program or simulation.

| Claim | Proof audit | Novelty audit | Decision |
|---|---|---|---|
| E05.P1: n-branch diagnosis impossible, robust repair identification n-1 | Correct conditional on composite branch repair, fixed full-branch path tests, all-branch service | Direct DRD/equivalence-class identification plus tomography | RETAIN as elementary fixture; NO-GO as new theorem |
| E05.P2: uniform branch prior expected probes (n-1)(n+2)/(2n) | Direct survival-sum proof checked, n=2->1, n=3->5/3, n=4->9/4 | Elementary search calculation | RETAIN as fixture; NO-GO novelty |
| E06.P1: gate repair activates subpath probe | Correct with public deterministic monitor-access restoration; probe admissibility distinct from UP/DOWN | Decision-dependent information discovery and monitor access are established | RETAIN as semantics example; NO-GO novelty |
| E06.P2: interleaving robustly succeeds but sensing-first cannot | **FALSE**: sensing-first repairs both service edges with same two-unit budget | Irrelevant once false | RETRACTED; must not be cited |
| E06.C1: parameterized nontrivial interleaving cost advantage | No construction, no lower bound, no oracle | Strong POMDP/DDID/progressive recovery collision | UNPROVED; NO-GO |
| E07.C1 universal-restoration sufficiency | Valid if all actions guaranteed, feasible, monotone, affordable and fit time | Trivial constructive upper bound | RETAIN as guardrail |
| E07.C2 indistinguishable-state common-plan lower bound | Valid for deterministic pre-repair identical transcripts, fixed repair-only phase | Standard indistinguishability argument | RETAIN as guardrail |
| E07.C3 restricted weighted set-cover equivalence | Valid **only** when service success is stipulated equivalent to union coverage and repairs commute; not generic graph repair | Classical weighted set cover | RESTRICT; no hardness novelty |
| E07.C4 equal-likelihood posterior odds | Valid if observations equal-likelihood even adaptively and no repair feedback | Bayes' rule | RETAIN as guardrail |
| E07.C5 symmetric noisy one-test success 1-epsilon | Valid under uniform prior, one test, epsilon in [0,1/2], matching repair | Classical binary hypothesis testing | RETAIN as guardrail |
| E07.C6 chance != robust guarantee | Valid for positive error and disjoint matching repairs | Classical robust/Bayesian distinction | RETAIN as guardrail |

## Correction required before any promotion
The first heading of `extension/theory/E06_REPAIR_DEPENDENT_OBSERVABILITY.md` says **'elementary conditional separation PROVED'** even though its E06.P2 is explicitly retracted. The heading is internally contradictory and must be treated as superseded by this E08 decision record. The preservation contract forbids silent overwrites; a separate erratum is committed inside extension/. No E06 source file was altered.

## Global gate
No independently original theorem survives E05–E07. This does not preclude a later computational or applied paper, but an original-theorem submission is **NO-GO**. E09 may begin only with explicit author approval and should implement correctness contracts, not assume novelty or report measured performance.
