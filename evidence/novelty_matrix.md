# Novelty matrix — Prompt 08 (2026-10-20)

| Proposed claim | Closest prior evidence | Verdict | IDs |
|---|---|---|---|
| Scent search and belief-state planning | Infotaxis; POMDPs | Established | E001,E017-E018 |
| Network creation and stochastic repair | Network design and repair | Established | E034-E039 |
| Priced sensing before combinatorial construction | Price of information | Established | E029 |
| Decision-dependent observation plus spanning tree optimization | Omer-Poss-Rougier | **Direct prior-art collision**; compact MILP under stated assumptions | E050 |
| Joint sensor placement and routing | Paradiso et al. | **Direct prior-art collision** | E023 |
| Distributionally robust optimization with costly information acquisition | Jin et al. preprint | Established research direction; publication status pending | E054 |
| Approximation schemes for adaptive/nonadaptive probing | Segev-Singla | Established for studied classes | E055 |
| Exact valid cutting planes with proof encoding and checking | Eifler-Gleixner | Established | E051 |
| Independent optimality certificates for planning | Dold et al. | **Direct challenge to proof-aware planning novelty** | E052 |
| Formalized soundness of planning certificates | Traytel | Established | E056 |
| Learning safety/reachability certificates from data with PAC guarantees | Rickard et al. | **Direct challenge to data-driven certificate novelty** | E053 |
| A genuinely new bound on joint sensing/creation/witness/checking cost for restricted transformation families | Above competing frameworks | **UNVERIFIED; no theorem or novelty approval** | pending |

## Counterclaims, limitations and required tests
1. **Expressibility counterclaim:** finite sensing, transformation and verification policies may be encoded in a POMDP or decision-dependent information optimization; representation alone is not novel.
2. **Compactness counterclaim:** E050 gives compact MILP under stated polyhedral uncertainty conditions, so claims of inherently exponential formulations need explicit restrictions.
3. **Proof-aware planning counterclaim:** E052 and E056 establish independent optimality certificates and mechanized soundness; attaching a verifier is not a contribution.
4. **Statistical certificate distinction:** E053's PAC generalization guarantee is not a deterministic assertion about every hidden state. Conversely, an encoded-instance witness need not certify an unknown physical world.
5. **Certificate cost counterclaim:** E051 discusses valid cuts, their encoding lengths, and practical verification; counting proof cost alone is not new.
6. **Adaptive guarantee caveat:** E055 concerns specific stochastic probing classes, not universal adaptive superiority.
7. No unrestricted complexity separation can be asserted; must fix sensor likelihood, allowed structural edits, verifier/proof language, uncertainty semantics, computational budget, and matched baseline.

## Citation chasing and quality control
Backward links from E050 include uncertainty reduction and robust combinatorial optimization; E051 cites exact MIP certification; E056 formalizes E052. This is targeted backward/forward chaining, not a comprehensive citation graph. Existing E033 year corrected 2023 to **2024** using SIAM primary publication metadata. E054 is a preprint; E055 has online-first issue status. No new theorem proved.
