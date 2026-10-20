# Novelty matrix — Prompt 06 (2026-10-20)
| Candidate claim | Closest prior art | Verdict | Evidence |
|---|---|---|---|
| Adding variables or structural design choices | Dantzig-Wolfe, Benders, extended formulations | Established | E004-E008 |
| Bayesian sensing and endogenous information | POMDPs and decision-dependent information | Established | E017-E025 |
| Priced probing before building a spanning tree | Singla | Direct overlap | E029 |
| Survivable network construction with approximation guarantee | Jain | Established | E034 |
| Two-stage stochastic network construction | Dhamdhere et al. | Established | E035 |
| Bilevel adversarial network structural decisions | Wood; Cormican et al. | Established | E036,E037 |
| Repair by adding/removing graph vertices after stochastic change | Rysz et al. | **Direct contradiction to broad possibility-creation novelty** | E038 |
| Repair decisions reveal damage information progressively | Tootaghaj et al. | **Direct contradiction to broad sensing-repair novelty** | E039 |
| Formal network fault-tolerance verification | Origami | Established adjacent work | E040 |
| Novel certificate-aware information/creation cost theorem | Stochastic repair, probing and formal verification | **Unverified; requires precise theorem and Prompt 07** | E029,E038-E040 |

## Contradictions
Network design, repair, and verification are all established individually. E038 already modifies graph structure after stochastic changes. E039 already interleaves repair and information gathering. The addition of formal validity checks does not itself establish novelty; simple connectivity and edge-connectivity are efficiently checkable. No universal superiority or asymptotic advantage can be inferred from these sources.

## Quality gate
Seven additions, publisher/institutional abstract/excerpt inspection; unresolved E038-E040 metadata flagged. No proof or experiment. The next stage must challenge even the narrowed certificate-aware claim.
