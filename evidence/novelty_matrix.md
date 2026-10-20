# Novelty matrix — Prompt 05 (2026-10-20)

| Candidate | Prior art | Verdict | Evidence |
|---|---|---|---|
| Canine olfaction, intermittency and Bayesian plume tracking | Infotaxis, robotics | Established | E001,E011-E016 |
| Column generation, model reformulation and network design | Classical optimization | Established | E003-E010 |
| Partial-observation policy optimization | POMDPs | Established | E017-E018 |
| Decision-dependent information discovery and sensing-aware routing | Stochastic/robust optimization | Established; direct overlap | E021-E026 |
| Adaptive greedy sensing guarantee | Adaptive submodularity | Established under assumptions | E002 |
| Stochastic probing with inner/outer constraints | Gupta et al. | Established | E027 |
| Adaptive/nonadaptive gaps for submodular/XOS probing | Gupta et al.; Asadpour-Nazerzadeh | Established under assumptions | E028,E030 |
| Paying to sense edge costs before network construction | Singla | **Direct contradiction of broad novelty** | E029 |
| Sequential tests with error constraints | Wald | Established | E031 |
| Universal submodularity of decision value of information | Krause-Guestrin | **False generally** | E019 |
| Increasing precision of stochastic probing | Hoefer et al. | Established; detailed comparison pending | E033 |
| Joint sensing/creation/proof cost under independent validity certificates | Adjacent probing and formal verification | **Unverified hypothesis** | E029; Prompt 07 |
| New information-certificate complexity separation | Existing information theory and proof complexity | **Unproved; may reduce to prior art** | pending |

## Contradictions and counterexamples
E029 already models priced information acquisition and combinatorial network construction, so any novelty claim based only on sensing+creation cost is rejected. E019 establishes that decision-theoretic information value need not be submodular, so a general adaptive-greedy theorem is untenable. E027-E030 bound adaptivity gaps for specified families; unrestricted adaptive superiority cannot be claimed.

Simple self-contained counterexample to submodularity: let two independent fair bits X1,X2 be observed at no cost, and reward 1 only if a final action guesses XOR(X1,X2) correctly. Baseline optimal success=1/2; observing either bit alone leaves optimal success=1/2; observing both gives 1. Thus marginal benefit of observing X2 rises from 0 (without X1) to 1/2 (with X1), violating diminishing returns. This is an illustrative derivation, not a new theorem.

## Outstanding research
The information-theoretic lower-bound literature (Fano, Le Cam, sequential design), formal certificates and certificate complexity need full primary-source verification in subsequent prompts. E019 is already listed as E019 under related value-of-information work but is a separate publication from E019; ensure exact title/DOI reconciliation at Prompt 09. E033 journal metadata is provisional. No novel theorem proven.
