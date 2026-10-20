# Novelty matrix — Prompt 07 (2026-10-20)
| Claim | Prior art | Status | IDs |
|---|---|---|---|
| Adaptive scent and belief-state search | Infotaxis, POMDPs | Established | E001,E017-E018 |
| Priced information before network construction | Stochastic probing, price of information | Established | E027-E029 |
| Network repair and progressive information collection | Stochastic network repair | Established | E038-E039 |
| Independent SAT proof checking | DRAT-trim | Established | E041 |
| Independently checkable MIP optimization certificates | VIPR | Established | E042 |
| Practically feasible PB optimization proof logging | VeriPB/CakePB | Established | E043 |
| Proof length/verification complexity as mathematical resource | Cook-Reckhow | Established | E044 |
| Static formal network safety checks | Header Space Analysis; NetKAT | Established | E045,E048 |
| Algebraic mixed-integer infeasibility witnesses | Andersen et al. | Established | E046 |
| More expressive certificate systems for SDP | Klep-Schweighofer | Established | E047 |
| Formally specified MILP certificate checker | SMT VIPR checker | Established | E049 |
| Joint sensing, structural creation, and **proof-system-specific** minimum certificate cost | Strong adjacent prior art | **Unverified candidate; no theorem** | E029,E038-E049 |

## Contradictions
- A certificate for a proposed graph's connectivity can be just a path or spanning tree; independent verification is not new.
- A SAT/ILP proof log can already certify feasibility or optimality in suitable encodings (E041-E043,E046,E049). Adding a verifier to a sensing policy does not constitute novelty.
- Proof length depends on the proof system and encoding (E044). No representation-independent certificate lower bound may be inferred.
- Bayesian posterior confidence in hidden theta is not a formal witness that a property holds in the true hidden theta.
- LP Farkas-style infeasibility certificates do not transfer without conditions to semidefinite settings (E047).
- Checking a network property after change (E045,E048) does not necessarily certify the entire stochastic decision process.

## Remaining narrow question
Formalize V(x,tau,w)=1 and distinguish (i) certificate of correctness for the **observed/encoded instance**, (ii) certificate for **all theta in an uncertainty set**, and (iii) probabilistic reliability. Seek a matched lower/upper bound on total observation, transformation, witness generation and checking cost. The candidate may collapse to standard stochastic optimization with proof logging; adversarial reductions required.
