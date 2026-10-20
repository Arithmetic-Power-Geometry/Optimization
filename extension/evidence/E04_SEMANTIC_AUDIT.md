# E04 — Semantic audit and prior-art boundary
Date: 2026-10-20

## Audited assumptions
- Distinct installed edge versus operational edge.
- Test admissibility versus observed UP/DOWN.
- Monitor access and CAP/CSP/UP routing rights.
- Public information versus hidden physical truth; common-feasible action rule avoids information leakage.
- Edge restoration versus topology installation, monitor relocation, route changes.
- Irreversible resource debits, horizon and cost vector.
- Robust universal service guarantee versus posterior probability guarantee.
- Signed record integrity versus sensor correctness.

## Important caveats
1. In deployed networks, whether a probe can be launched and whether its full route is known may be partially observable. v1.0 selects a strict common-feasible default; a future attempted-probe failure model must explicitly charge and return feedback.
2. CAP/CSP/UP nomenclature and binary path tomography are established (Ma et al., Performance Evaluation 2015; IEEE/ACM Transactions on Networking 2017). See https://www.sciencedirect.com/science/article/pii/S0166531615000516 and https://pure.psu.edu/en/publications/network-capability-in-localizing-node-failures-via-end-to-end-pat/.
3. The robust stopping predicate under static tests is established DRD (Javdani et al., AISTATS 2014): https://proceedings.mlr.press/v33/javdani14.html.
4. State-dependent sensing, physical repair and belief recursion are not automatically original relative to POMDP/DDID/progressive recovery.
5. An edge restoration with uncertain outcomes requires explicit success/failure observation kernels, and public resource counters must be consistently observed. No implicit free feedback.
6. All cost budgets require a common convention for comparison; a nonnegative vector budget can forbid a repair even when scalar total cost remains low.
7. This is a **formal specification**, not a completed executable implementation or a proof of nontrivial novel graph-family separation.

## E05 admissibility gate
Any theorem candidate must instantiate the finite graph, monitors, probe alphabet, admissibility predicate, initial hidden-state family, repair preconditions, transition kernels, resource budget, success criterion and comparator rights. Missing any component is a proof-blocking gap.
