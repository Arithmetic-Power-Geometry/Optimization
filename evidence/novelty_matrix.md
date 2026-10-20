# Novelty matrix — Prompt 02, 2026-10-20

| Candidate claim | Prior art | Status | Evidence |
|---|---|---|---|
| Dynamically introducing variables/activities | Dantzig-Wolfe column generation | Established | E004 |
| Decomposing design and operational decisions | Benders | Established | E005,E010 |
| Adding variables to improve mathematical representations | Extended formulations | Established | E006 |
| Exponential separation among representation classes | Extension complexity | Established in important cases | E006,E007 |
| Joint upper/lower level design | Bilevel optimization | Established | E008 |
| Automatically exploring optimization formulations | Autoformulation | Established | E009 |
| Sensing before selecting network changes | Adjacent stochastic/network design | Unresolved; requires Prompts 04-06 | pending |
| Certified sensory-creation representation separation | Adjacent extension complexity and proof systems | Unverified research hypothesis | E006,E007; pending |

## Contradictory evidence
- Adding variables or structural elements is not new (E004,E006).
- Changing a design and optimizing its operations is not new (E005,E008,E010).
- Automatically discovering solver formulations is not new (E009).
- An unrestricted classical optimizer can encode finite sensing/creation policies as an augmented stochastic program; no universal impossibility claim is justified.
- Representation lower bounds for restricted linear formulations (E006,E007) do not establish lower bounds for arbitrary adaptive algorithms.

## Candidate research gap
Specify a restricted information/computation model, sensing kernel, transformation family, independent certificate relation, and total-cost accounting. Then attempt a separation or impossibility result against a rigorously matched baseline. Novelty not verified.

## Limitations
Seven added sources were inspected at publisher/archival abstract and metadata level, not systematically read in full. This is a targeted foundational audit, not an exhaustive review. Network-augmentation and endogenous-information primary papers remain for Prompts 04-06. A review article (E010) provides context but cannot substitute for primary theorem verification.
