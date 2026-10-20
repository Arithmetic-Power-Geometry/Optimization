# Novelty matrix — Prompt 04 (2026-10-20)
| Claim | Closest prior art | Assessment | Evidence |
|---|---|---|---|
| Intermittent scent search | Infotaxis | Established | E001 |
| Adaptive sensing guarantees | Adaptive submodularity | Established with conditions | E002 |
| Structural design and reformulation | Network design, Dantzig-Wolfe, Benders, autoformulation | Established | E003-E010 |
| Biological bilateral sampling and plume tracking | Canine and robot studies | Established | E011-E016 |
| Hidden-state Bayesian policy optimization | Smallwood-Sondik; Kaelbling et al. | Established | E017,E018 |
| Optimal conditional sensing and information value | Krause-Guestrin; knowledge gradient | Established | E019,E020 |
| Decisions determine when information becomes available | Jonsbraten et al.; Goel-Grossmann | Established | E021,E022 |
| Joint sensor placement and routing | Paradiso et al.; Zhou-List | **Direct counterexample to broad joint-sensing/design novelty** | E023,E026 |
| Multistage exploratory investments before adaptive decisions | Vayanos et al. | Established | E024 |
| Decisions change probability distributions | Pantuso-Hewitt | Established | E025 |
| Independently certified *new structural model* chosen under information restrictions | POMDPs, endogenous information, verification still to audit | Unverified; narrow candidate | E017-E025 |
| Novel matched sensing/creation/certificate complexity lower bound | Information complexity, formal proof systems still to audit | Unproved hypothesis | pending |

## Contradictory evidence and limitations
E023 explicitly cooptimizes sensor placement and routing, invalidating an unqualified novelty claim for sensing-aware network decisions. E024 and E022 already model costly information revelation controlled by decisions. E019 proves severe computational hardness for value of information, so efficiency cannot be assumed. E025 shows existing exact decomposition for decision-dependent distributions. POMDPs (E017,E018) can encode finite sensory-creation policies by augmenting states and actions; an expressiveness-only novelty claim fails.

The candidate must state a specific transformation language, certificate relation, information restrictions, and cost model; test for reduction to existing stochastic/robust formulations. No theorem established, no novelty percentage warranted. Literature inspection mainly abstracts and one article section; not a comprehensive systematic review.
