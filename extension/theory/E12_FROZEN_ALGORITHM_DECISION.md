# E12 — Candidate-policy freeze and rejection record
Date: 2026-10-20. Gate: NO-GO for a technically distinct new decision-sufficient algorithm.

## Examined candidates
**Candidate A — decision-sufficient stopping.** Stop as soon as all hypotheses in the public belief satisfy the service predicate. This is already the stopping rule in E10's exact oracle and E11's policy evaluator, and is the same conceptual sufficiency condition as classical DRD, with service success in place of decision-region containment. **REJECT as duplicate, not new algorithm.**

**Candidate B — greedy repair-or-probe with action-budget screening.** At each belief state choose a common-admissible probe maximizing separation or a repair maximizing immediate service-success mass, respecting remaining time/repair/probe budgets. This is already implemented as E11's cost_sensitive_greedy and drd_region_greedy; E11's pairwise surrogate is not original HEC. **REJECT as duplicate.**

**Candidate C — optimal finite-horizon robust/Bayesian planning.** Enumerate legal actions, partition belief on observed probe outcomes, optimize success by Bellman recursion. This is E10's exact oracle and a classical finite-state sequential decision formulation. **REJECT as duplicate.**

## Frozen reference procedure (NOT an original contribution)
Input: finite E10 Problem, normalized prior, initial common belief, horizon h.
1. If h=0, evaluate terminal service in every live hypothesis and stop.
2. If service holds in every live hypothesis, stop with robust success.
3. Construct common-admissible probes and repair actions; reject any action that exceeds a resource budget.
4. Evaluate each repair continuation under its public outcome and each probe continuation by grouping hypotheses by public UP/DOWN observation.
5. Select the action with best exact Bayesian success (or robust feasibility under the separate robust objective), tie-breaking by declared input order.
6. Decrement time and action budgets exactly once; recurse.
This is **the existing E10 exact oracle**, restated as a specification only. No additional implementation is warranted without a demonstrated technical distinction.

## Termination and complexity (classical)
Under a nonnegative integer horizon h, every recursive transition decreases h by one. Thus recursion terminates by induction. Every action is screened against every live hypothesis; each action charges one time unit and one action-budget unit, so no action can exceed the finite resource vector. Let A=number of available action names and O=2 binary probe outcomes. A loose bound on a naive un-memoized policy-tree expansion is O((A O)^h) action/outcome branches, excluding per-node graph service/admissibility cost. E10 memoization can reduce repeated subproblems but does not supply a polynomial-time worst-case bound. **No novel complexity theorem is claimed.**

## Important qualification
Correctness of the mathematical recurrence assumes deterministic outcomes, shared public configurations, truthful physical graph kernel and no hidden action rights. Passing finite synthetic tests does not establish a new decision-sufficient method or approximation guarantee.

## Scientific freeze
E12 freezes the **negative candidate-selection decision**, not a new method. No unique new algorithm identifier, superiority claim, or novel theorem is authorized for manuscript insertion.
