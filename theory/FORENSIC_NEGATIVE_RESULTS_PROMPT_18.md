# Prompt 18 — forensic model and negative-results audit (2026-10-20)
**Status: NO-GO for an original theorem.** The following are elementary, fully specified deductions and model repairs; none is asserted novel.

## F18.1 — repair-before-probe does not automatically overcome a one-repair budget
Graph: series path s--u--t, exactly one of e1,e2 failed. Only permitted probe is end-to-end s--t status. Each repair restores exactly one edge and **irreversibly consumes one of at most one allowed repairs**. Before repair, both states give DOWN. If policy repairs e1 then probes, UP identifies F1 and yields success, but DOWN identifies F2 after the entire repair budget has been spent, so physical s--t connectivity cannot be restored. The symmetric policy repairing e2 fails for F1. Therefore allowing a probe after a repair does **not** permit a zero-error policy for both states under this strict budget. Proof: first meaningful choice must be a repair of e1 or e2; adversary selects opposite failed edge; one budget spent, target false. Randomization cannot guarantee probability 1. If budget is two, repairing both edges is a universal repair with no sensing; if repair cost is not a hard cardinality budget, a different cost-sensitive dynamic program applies. This corrects a misleading possibility noted in Prompt 17, without claiming new mathematics.

## F18.2 — terminal decision regions and overlap
For each edit sequence a, define R_a={theta: physically valid s--t connection after a}. Robust terminal success for transcript h requires B(h) subseteq R_a. The sets may overlap and are not necessarily a partition. If two states are indistinguishable under all permitted actions and probes and no common valid edit exists, zero-error repair is impossible. The criterion is a direct consequence of the definition; it does not prove a new complexity bound.

## F18.3 — restricted end-to-end probing matters
A local edge oracle distinguishing e1 and e2 (Prompt 16) is **not** implementable from a single fixed end-to-end series path without extra monitor placement, topology, or intervention. Therefore E16.1's one-probe sufficiency cannot be transferred to end-to-end tomography. The 2017 Ma et al. journal article E060 already explicitly separates probing models with different path control; no novelty is gained by suppressing probe feasibility.

## F18.4 — asymmetric costs
With repair costs r1 != r2 and a prior over states, the choice between repair, probe and stop is a finite-horizon belief-state policy with state-dependent terminal loss and positive action costs. Without an explicit complexity/approximation separation under graph constraints, asymmetric costs alone do not establish originality.

## Primary-theorem collision and precise verification
E064 Golovin, Krause, Ray (NeurIPS 2010) publisher full text, Sections 2–4: Theorem 1 states a self-certifying adaptive-submodular greedy approximation; Proposition 2 asserts EC objective is strongly adaptive monotone/submodular (proof deferred to long version); Theorem 3 gives EC2 cost at most (2 ln(1/p_min)+1) times optimal ECD policy for rational priors. Section 4 defines optimal minimum-risk decision under loss and reduction to decision classes. **This is a verified reading of theorem statements and reductions, not an independent line-by-line reproduction of all proofs.**
E065 Chen, Hassani, Krause (AISTATS 2017) publisher PDF: correlated noisy test target-variable learning with ECED, not EC2. Author's publication list and ETH bibliography identify extended *Electronic Journal of Statistics* 11(2):4969–5017 (2017), DOI 10.1214/17-EJS1336SI; this is the same contribution, not an additional independent evidence item.
E060 Ma et al. IEEE/ACM ToN 25(1):434–450 (2017) journal and 2015 arXiv version correspond; E063 is its proof/evaluation companion. E059 2015 Performance Evaluation and E061 proof companion; E062 companion to earlier 2014 work. **Theorems E059–E063 have not been individually reproduced or exhaustively checked**.

## Decision
No nontrivial original graph-family lower bound, approximation ratio or complexity separation survived. Continue only with a final forensic audit and explicit alternative-output assessment if authorized; theorem-based manuscript NO-GO. No software, experiments or manuscript.
