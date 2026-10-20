# E06 — Countermodels and proof obligations
Date: 2026-10-20.

## Adversarial failed claim
An initial attempt argued that repairing a monitor-access gate g enables an informative path probe, so an interleaving policy could repair one unknown service edge whereas sensing-first could not. **Counterpolicy:** with the same two-unit repair budget, sensing-first repairs both candidate service edges without repairing g, and achieves robust service. The originally proposed strict separation is FALSE. This counterexample is preserved in full in E06_REPAIR_DEPENDENT_OBSERVABILITY.md.

## Further countermodels
- C01: A fixed set of probes remains admissible under all repairs: no repair-dependent observability.
- C02: A repair changes only path UP/DOWN outcomes, not monitor access or routing rights: outcome change does not imply test-set expansion.
- C03: A previously inaccessible monitor becomes publicly available after a deterministic access repair: new probes can be admitted, but this alone does not prove an objective advantage.
- C04: A 'probe' whose route includes an uninstalled edge is not a DOWN observation; it is inadmissible.
- C05: Two-unit budget permits restoring both possible failed edges: sensing-first robustly succeeds without diagnosis.
- C06: One-unit budget prevents both access restoration and target restoration: interleaving cannot finish.
- C07: If gate repair succeeds with unknown probability, access feedback must be specified and repair still charged on failure.
- C08: If the post-gate test is secretly selected using theta-dependent feasibility, the model leaks hidden state.
- C09: If a terminal universal bypass is allowed, zero-probe repair can dominate interleaving.
- C10: A signed DOWN test cannot establish physical truth without a reliable sensor assumption.

## Required independent proof gates
1. Establish the service predicate before and after every candidate action, not only the informativeness of tests.
2. Enumerate all sensing-first repair sequences, including brute-force restoration of all candidates.
3. Charge enabling repairs and service repairs separately and never twice.
4. Compare worst-case cost and Bayesian cost under explicit distinct conventions.
5. Verify monitor access publicly changes and no probe uses an absent physical edge.
6. Prove a lower bound on *all* baseline policies, not a hand-picked diagnosis-first heuristic.
7. Check action ordering against published POMDP and multistage DDID.
8. Produce finite state exhaustive oracle in E09/E10; no executable test run claimed now.
9. Independent adversarial reviewer or checker must validate before E08 promotion.
10. Preserve failed theorems as falsification evidence.

## Verdict
P1: elementary semantics example; VALID under assumptions, not original.
P2: INVALID, explicitly retracted.
C1: UNPROVED.
