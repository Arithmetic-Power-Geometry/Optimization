# E03 — Explicit reductions, boundaries and countermodels
Date 2026-10-20. Original derivations below are straightforward reductions, not independently new theorems.

## Reduction A: static repair selection is overlapping DRD
Assume finite hidden-state set H, fixed test alphabet T with deterministic outcomes o_t(h), tests do not modify physical state, and finite candidate repairs A. Let R_a={h in H: repair a satisfies service predicate in h}. For history S, define V(S)={h in H: every observed test agrees with o_t(h)}. A robust repair is available exactly when there exists a in A with V(S) subset R_a. This is exactly the DRD termination predicate of Javdani et al. 2014, even if R_a overlap. Hence the predicate and overlapping-region interpretation cannot be claimed original. If repair costs are unequal, standard DRD sensing-only cost guarantees cannot automatically be transferred to a joint total-cost objective; difference of objective alone is not originality.

## Reduction B: finite sequential repair/probing embeds in POMDP
Let state s=(physical graph configuration, hidden failure configuration, remaining budget, monitor availability). For each feasible test/repair action u, define a transition kernel P(s'|s,u) and observation kernel Z(o|s',u). Costs and service success are rewards/terminal conditions. This is a finite POMDP if all sets are finite and the full physical state and resource counters are included. Therefore an ordinary belief-state Bellman recursion and action-dependent sensing are not themselves new algorithms. Robust belief-set recursion is a set-valued worst-case analogue. To establish novelty one needs nontrivial network-specific structure, computational guarantees, lower bounds or reproducible empirical superiority under matched comparator rights.

## Reduction C: full-path tomography subcase
Fix the physical graph and monitors, prohibit repairs during sensing, and let test outcome be a binary end-to-end path state. Distinguishability of failures reduces to path-signature injectivity over admissible paths, which is the established network tomography subject studied by Ma et al. (2015/2017). Distinguishing two failures only by direct inspection is invalid when the test alphabet is restricted to end-to-end paths.

## Countermodel 1: repair-independent tests
If every allowed repair leaves the feasible test set and all observation outcomes invariant, 'repair-dependent observability' is absent. Any proposed universal advantage theorem requiring it is false without a structural assumption.

## Countermodel 2: universal affordable repair
If some admissible repair restores service for every surviving hidden state within budget, a zero-probe robust policy exists. There can be no universal strictly positive minimum sensing requirement.

## Countermodel 3: two failures on a series path
With exactly one unknown failed edge on a series s-t path and only full-path UP/DOWN tests, all pre-repair observations are DOWN. A single irrevocable restoration cannot guarantee robust success for n>=2; under a uniform failed-edge prior the best probability is 1/n. After a successful restoration, service can be verified; verification does not retroactively identify which restoration should have been chosen. The proof is elementary and is not a novelty claim.

## Countermodel 4: free repair or unequal rights
A claimed separation between diagnosis-first and repair-first can be arbitrarily manufactured if only one comparator is granted additional probes, repair attempts, budgets or information. Therefore a valid comparison must match information and intervention rights, cost convention and success guarantee.

## Countermodel 5: hidden physical truth versus signed log
An authenticated probe record verifies provenance and integrity of the record but does not establish sensor accuracy or physical path state. Do not infer physical correctness from cryptographic attestation alone.

## Candidate distinctive question, NOT a result
Can a restricted family of monitor-constrained networks with irreversible interventions exhibit a provable separation in robust service restoration cost between policies that may interleave repair and path tests and policies that must finish sensing before any repair, even when both classes have identical budgets, repair/test rights and final service criteria? Before claiming a new theorem, compare directly to progressive stochastic recovery and general POMDP models, and demonstrate a family-specific tight bound rather than mere model embedding.
