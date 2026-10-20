# E03 — Adversarial novelty collision matrix
Date 2026-10-20. Status: literature-based analytic mapping; NOT a claim of original theory.

| Proposed claim | Established predecessor and exact correspondence | Remaining difference (not proof of novelty) | Verdict |
|---|---|---|---|
| Stop sensing once one repair works for all consistent states | Javdani et al. (2014) DRD: hypotheses H, overlapping decision regions R_a={h:a valid}; stop iff V(S) subset R_a. Map a repair to a decision region. | Network-specific admissible paths and state-changing edits not in static test-only DRD reduction. | **NO-GO** for stopping condition, overlap, decision sufficiency alone. |
| Identify repair equivalence class instead of full failure | Golovin/Krause/Ray (2010) EC2, cost-sensitive noisy active testing; Chen/Hassani/Krause (2017) ECED correlated noisy target testing. | Sequential edits may change test access and state; full model comparison required. | **NO-GO** as broad diagnosis-vs-decision claim. |
| Failure distinguishability using physical paths | Ma et al. (2015, 2017) path measurement tomography with monitor access and path control constraints. | Post-intervention observation set might change; identifiability alone established. | **NO-GO** for path-based impossibility/localization novelty. |
| Select information before optimization | Omer/Poss/Rougier (2024) DDID: first-stage choose coefficients to reveal; second-stage robust solution. Multistage DDID also studied elsewhere. | Physical repair as a state transition that can change future feasible path probes and service feasibility. | **NO-GO** for DDID concept; proposed narrower distinction **UNPROVED**. |
| Iteratively repair and gather information | Zad Tootaghaj et al. (2017 conference, 2019 IEEE TNSM) progressive network recovery under uncertain damage; iterative repair plus information gathering. | Exact physical probe alphabet, one-repair budget, formal cost/observability separation may differ. | **STRONG COLLISION**; generic interleaving **NO-GO**. |
| Finite-state belief-set dynamic program | Finite-horizon POMDP and belief-MDP theory (Monahan 1982; later tutorials), including action-dependent transitions and observations. | Domain-specific compactness, structural algorithm or new bound not yet established. | **NO-GO** for Bellman recurrence or generic POMDP reduction. |
| n-edge series path, one restoration, only end-to-end UP/DOWN | Elementary indistinguishability and symmetry; special case of restricted-observation decision theory. | Exact 1/n analytical identity under uniform one-failure prior. | **VALID elementary instance, novelty UNPROVED**; not a new central theorem. |
| New graph-family theorem separating repair from diagnosis | No independent proof yet. Must beat DRD, tomography, progressive recovery and POMDP reductions. | Possible constrained family under fixed monitor rights and irreversible budgets. | **HYPOTHESIS; E04/E05**. |

## Primary URLs and evidence depth
- Javdani et al. 2014, PMLR publisher PDF https://proceedings.mlr.press/v33/javdani14.pdf : Section 3 explicit stopping condition V(S) subset r, equation (2), HEC.
- Golovin/Krause/Ray 2010 https://proceedings.neurips.cc/paper/2010/hash/1e6e0a04d20f50967c64dac2d639a577-Abstract.html : publisher abstract, cost/noise.
- Chen/Hassani/Krause 2017 https://proceedings.mlr.press/v54/chen17b.html : publisher abstract.
- Ma et al. 2017 https://pure.psu.edu/en/publications/network-capability-in-localizing-node-failures-via-end-to-end-pat/ : institutional publication record and abstract; DOI 10.1109/TNET.2016.2584544.
- Omer/Poss/Rougier 2024 https://ojmo.centre-mersenne.org/articles/10.5802/ojmo.33/ : journal publication abstract and scope; DOI 10.5802/ojmo.33.
- Zad Tootaghaj et al. 2019 https://scholars.uky.edu/en/publications/on-progressive-network-recovery-from-massive-failures-under-uncer/ : institutional record, abstract; DOI 10.1109/TNSM.2018.2880155.
- Monahan 1982 https://pubsonline.informs.org/doi/10.1287/mnsc.28.1.1 : publisher abstract; finite-state belief-POMDP model.
The source-depth distinction is deliberate. No exhaustive independent reconstruction of published proofs was performed.
