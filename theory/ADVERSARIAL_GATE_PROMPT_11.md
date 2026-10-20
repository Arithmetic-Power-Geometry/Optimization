# Prompt 11 — Adversarial theorem gate
Date: 2026-10-20. **No original theorem established.**

## Corrected formal assumptions
Fix a finite horizon H, rational hidden-state prior and observation kernels, explicit action/edit sets, and finite candidate witnesses with a deterministic verifier. All witness-generation/checking costs must be *computable from the public state, action, and chosen witness*; they cannot depend on an unavailable hidden theta. Where the verifier is deterministic and its input finite, it can be modeled as a terminal deterministic transition with cost. Unbounded witness search or arbitrary complexity functions require a separate uniform computational model, not a finite-state assertion. Treat hard-invalid outcomes as forbidden or a terminal penalty. Authenticated sensing, if used, is an explicit priced action.

## A11.1: finite-horizon reduction to belief-state planning (elementary)
**Statement.** For a fixed finite instance with finite witness candidates and public computable certificate costs, minimizing expected total sensing, editing, witness generation and checking cost is a finite-horizon partially observed decision problem.
**Construction.** Hidden state is theta augmented with physical graph state and any finite resource counters; public actions are sensing, edit, certificate choice and halt; observations use K; transitions implement edits; terminal reward equals negative verifier/witness cost or a penalty for invalidity. A belief over augmented hidden states and public history suffices to compute expected continuation value; dynamic programming over histories gives the same optimal value. The reduction is finite but may be exponentially large and does NOT establish a compact representation or efficient algorithm.
**Proof.** There is a bijection between admissible finite histories and policy decision nodes in the constructed process. Corresponding action choices have identical observation probabilities, graph transitions, validity outcomes and accumulated costs. Induction backward over remaining horizon equates every policy's expected cost, hence the optima.
**Consequence.** H10.1's mere *combined objective* and H10.2's sensor-policy dependence are instances of standard decision-theoretic optimization. This does not rule out a novel restricted-class complexity bound.

## A11.2: certificate-induced sensor reversal is elementary, not novel
**Constructed two-sensor example.** Hidden theta is a fair bit. Sensor A reveals theta perfectly for cost 2; sensor B reveals theta perfectly for cost 1. The final state-specific edit costs zero; its encoded feasibility witness can be generated and checked at cost 0 if an authenticated A observation is supplied, or cost 3 if a B observation is supplied (e.g. a deliberately more expensive attestation route). Without certificate costs B is strictly optimal (1 < 2). With costs, A is strictly optimal (2 < 1+3=4). The same terminal validity and edit are available under both; a witness is assumed sound for the authenticated input.
**Proof.** Compare the two deterministic total costs directly. This is a valid *existence* example only under the stipulated, asymmetric proof/attestation pricing. It does not establish intrinsic certificate complexity, nor a non-artificial graph family. Moreover, adding the attestation/proof expense to each action's effective cost reproduces the reversal as an ordinary cost-aware sensing problem. H10.2 is **TRUE as a trivial existential statement under flexible costs, but fails the novelty gate**.
**Important caveat.** If A and B produce the *same publicly authenticated transcript* and the same admissible witness language, the verifier cannot assign different minimum certificate costs merely from their arbitrary labels unless the encoding or generation algorithm legitimately differs. An unjustified label-dependent cost would be artificial.

## A11.3: indistinguishability lower bound (elementary)
**Statement.** Let theta0,theta1 have positive prior masses and require mutually exclusive final edits for validity. If every available sensing action has identical observation laws in both states at every common public history, and edits do not themselves reveal theta, no policy can satisfy robust zero-error validity for both states.
**Proof.** Induction on history length shows that the complete observable transcript has the same law in theta0 and theta1. Therefore the policy's final edit distribution is identical in both. Since the sets of valid edits are disjoint, no common distribution can place probability one on each. Contradiction. Certificate verification of a declared instance cannot break the observational equivalence. 
**Generalization.** With noisy but distinguishable observations, quantitative lower bounds require a specified divergence, risk criterion and sampling protocol; ordinary hypothesis-testing inequalities already apply. H10.3 does not establish a new bound beyond standard information theory.

## A11.4: universal repair counterexample
If there is a single edit tau* such that L(theta,tau*)=1 for every theta in the uncertainty set and a sound robust witness w* exists, the zero-sensing policy (tau*,w*) is robustly valid. Any assertion that *robust certification always requires positive sensing* is false. If tau* is prohibitively costly, a sensing policy may be cheaper, but that is a cost tradeoff, not an impossibility theorem.

## Audit of Prompt 10 baseline
P10.1 containment valid only when adaptive class permits every fixed schedule, with identical termination and resource rules.
P10.2 valid as a counterexample to physical truth inference, but does not imply all encoded witnesses are unsound; the checker may be perfectly sound for its **encoded** predicate.
P10.3 threshold lower bound valid for worst-case **fixed schedules** and exact identification with threshold-only sensors. Its proposed witness must authenticate responses and must be checked against a public transcript. With zero-error randomized nonadaptive schedules, each schedule in support must separate every adjacent pair. This is classical binary search.
P10.4 cancellation requires identical edit and certificate costs across the compared policies; if different terminal actions are chosen, constant-per-witness alone is not enough.

## H10.1-H10.3 verdicts
| Hypothesis | Adversarial result | Gate |
|---|---|---|
| H10.1 nontrivial combined-cost separation | Finite-state reduction A11.1; certificate constant-overhead cancellation P10.4; existing DDID E050, priced probes E029, planning proof logs E052 | **NO-GO as presently formulated**. New restricted complexity separation not shown. |
| H10.2 certificate changes optimal sensor | Constructive 2-sensor example A11.2, but equivalent to ordinary sensor cost change | **EXISTENCE TRUE, NOVELTY NO-GO** |
| H10.3 new robust-certification information lower bound | A11.3 standard indistinguishability; A11.4 zero-sensing universal edit | **NO-GO as general novelty claim** |

## Primary-source constraints and reductions
- E050 Omer/Poss/Rougier (OJMO 2024 DOI 10.5802/ojmo.33): robust two-stage DDID for combinatorial problems including spanning trees; compact MILP when number of non-bound constraints describing uncertainty polytope is constant. It does **not** imply all finite-horizon POMDPs have compact MILPs.
- E052 Dold et al. (ICAPS 2025 DOI 10.1609/icaps.v35i1.36101): independently checkable lower-bound proof logs for optimal planning, including A*. It does **not** prove a general cost theorem for sensing-dependent graph edits.
- E056 Traytel (AFP 2026): mechanized soundness of the lower-bound certificate format, not a sensing-cost separation.
- E029 priced information and combinatorial optimization, E023 joint sensing/routing, E038 stochastic graph repair, E039 repair under uncertain damage: adjacent and overlapping models, not proven polynomial reductions in every case.
- POMDP equivalence A11.1 is an explicit semantic reduction for **finite** instances; it does not show that all specialized structural models are computationally trivial.

## Decision
**NO-GO for claiming an original theorem or submitting a manuscript on the current hypotheses.** A conditional exploratory path could fix a natural verifier/proof language and prove an asymptotic lower/upper bound under explicit resource restrictions; no such result exists yet. Prompt 12 should produce a transparent final research audit and possible pivots, not manufacture a paper.
