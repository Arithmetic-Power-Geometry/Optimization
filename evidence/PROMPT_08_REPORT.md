# Prompt 08 — Adversarial 2023–2026 primary literature
Date: 2026-10-20

## Method
Verified primary publisher/proceedings/author institutional records for seven new items E050–E056, and corrected E033 year (2024, SIAM J Discrete Math 38(1):148-169). Cross-checked paper titles, author lists, DOI where available, publication status and abstract-level claims. Sources: OJMO, SIAM, ICAPS, Automatica, Optimization Online, INFORMS and Archive of Formal Proofs. Citation chaining: Omer-Poss-Rougier prior uncertainty-reduction references; VIPR/Eifler-Gleixner lineage; Dold et al. to Traytel formalization. The search is targeted, not systematic or exhaustive; full text and theorem proofs have not been independently audited.

## New critical competitors
E050 Omer-Poss-Rougier 2024: DDID with polyhedral uncertainty; compact MILP under a bounded-description assumption; examples include spanning trees. This is a **direct challenge** to claiming new information-guided combinatorial network design or necessarily huge policy encodings.
E051 Eifler-Gleixner 2024: exact mixed-integer cutting planes, verified certificates, controlled encoding lengths; solver-side proof cost already studied.
E052 Dold et al. 2025: pseudo-Boolean lower-bound certificates and independently verifiable A* planning optimality.
E053 Rickard-Abate-Margellos 2026: data-driven synthesis of reachability/safety certificates with PAC generalization bounds; do not equate PAC validity with absolute validity.
E054 Jin-Georghiou-Vayanos-Hanasusanto 2024 preprint (updated 2025): distributionally robust optimization with decision-dependent information discovery; peer-reviewed status unverified.
E055 Segev-Singla 2025: efficient approximation schemes for adaptive and nonadaptive stochastic probing classes.
E056 Traytel 2026: formalization of soundness for E052's planning certificate framework.
E033 correction: Hoefer-Schewior-Schmand published 2024 (not 2023), SIAM J Discrete Math 38(1):148-169.

## Novelty audit decision
NO broad novelty claim survives. Information acquisition plus structural design, proof-producing planning, exact certificate checking, and data-driven probabilistic certification all have close recent prior art. The remaining candidate is a *restricted-model theorem* linking observation complexity, edit cost and proof-system-specific certificate cost. No proof and no verified novelty yet.

## Unresolved issues
- Full text proof-by-proof inspection of E050/E052/E053 and any overlapping lower-bound results.
- Systematic forward-citation coverage and 2026 indexing latency.
- Bibliography cleanup from prior prompts (E016, E038-E040, E048); verify venue/author details.
- Clarify whether certificate proves an observed instance, all theta in uncertainty set, or a calibrated probability statement.
- Identify minimal formal examples where certificate production genuinely changes optimal sensing policy; avoid artificial overhead definitions.

## Scope gate
No software, experiments, manuscript or novel theorem. Prompt 09 should deduplicate, verify references and freeze candidate with explicit no-go alternatives.
