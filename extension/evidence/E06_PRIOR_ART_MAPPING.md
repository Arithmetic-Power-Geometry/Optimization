# E06 — Prior-art collision: intervention-dependent observability
Date: 2026-10-20.

| Established work | Source | Collision with E06 |
|---|---|---|
| Omer, Poss & Rougier (2024), two-stage combinatorial robust DDID | https://numdam.org/articles/10.5802/ojmo.33/ | Decisions control what uncertain information is revealed. E06's physical access-gate is a specific intervention and not a new information-discovery paradigm. |
| Paradiso, Georghiou, Dabia & Tönissen (2024 online; journal volume 2025), exact and approximate robust DDID | https://pubsonline.informs.org/doi/10.1287/ijoc.2023.0290 | Exact algorithms, sensor-placement/orienteering and shortest-path DDID benchmarks already exist, with reproducibility repository https://github.com/INFORMSJoC/2023.0290. This is a particularly close computational comparator. |
| Robust Optimization with Decision-Dependent Information Discovery (Management Science, online 2025) | https://pubsonline.informs.org/doi/10.1287/mnsc.2021.00160 | Two- and multistage decisions control timing of information revelation. Generic 'intervention unlocks later information' is explicitly established. |
| Ma et al. (2015/2017), network tomography | https://www.sciencedirect.com/science/article/pii/S0166531615000516 | Monitor placements and path measurement rights constrain what can be distinguished. |
| Javdani et al. (2014), overlapping decision regions | https://proceedings.mlr.press/v33/javdani14.html | A common sufficient repair across a belief set is an established decision-region termination criterion. |
| Progressive network recovery under uncertain damage | https://scholars.uky.edu/en/publications/on-progressive-network-recovery-from-massive-failures-under-uncer/ | Restoration and information collection can interact in network repair; direct theorem-level comparison still required. |

## Primary-source verification depth
Journal/publisher metadata and abstracts were checked for the DDID papers; full line-by-line proof audit and systematic citation search were NOT performed. Paradiso et al. software repository is external prior art, not executed by E06. All cited papers are separate works, not new registry records automatically added to the original bibliography.

## Originality decision
NO-GO for novelty of decision-dependent sensing or multistage information revelation. NO-GO for the failed G_gate robust feasibility separation. Narrow graph-family structural bound remains unproved.
