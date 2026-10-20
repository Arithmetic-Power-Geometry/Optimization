# E07 — Independent audit obligations and falsification register
Date 2026-10-20. Status: analytic checking only; no executed oracle or independent referee.

| ID | Obligation | Finding |
|---|---|---|
| B01 | Match repair action rights | E06 sensing-first can restore both candidate service edges; separation false. |
| B02 | Count failed repair attempts | Must debit even on failure; E04 rule. |
| B03 | Distinguish admissible from successful probes | Failed installed paths can return DOWN; absent paths inadmissible. |
| B04 | Include zero-probe universal restoration | C1 prevents unconditional positive sensing lower bounds. |
| B05 | Lower bound over all baseline policies | C2 uses identical transcripts and common repair plan; no heuristic-only baseline. |
| B06 | Weighted cover reduction scope | C3 only for union-of-coverage monotone commuting repairs; not arbitrary graph connectivity. |
| B07 | Equal-likelihood Bayes ceiling | C4 depends on identical observation likelihoods and no intervention feedback. |
| B08 | Noisy-test chance guarantee | C5 exactly 1-epsilon for one symmetric test and uniform prior. |
| B09 | Robust vs Bayesian | C6 robust impossibility can coexist with high chance success. |
| B10 | Time/horizon feasibility | Must check enabling, testing and terminal repair durations and action slots. |
| B11 | Heterogeneous cost | Equal-unit examples do not imply heterogeneous optimality. |
| B12 | Stochastic repair | Worst-case success requires all permitted repair outcomes; deterministic assumption flagged. |
| B13 | Prior-art novelty | Set cover, binary testing, DRD, DDID and POMDP subsume broad claims. |
| B14 | Executable independent enumeration | NOT EXECUTED; E09/E10 gate. |
| B15 | External independent proof audit | NOT PERFORMED; E08 cannot claim independently verified original theorem. |

## Edge-case matrix
- R0: B_R=0, already functioning service => zero repair/probe sufficient.
- R1: B_R=0, failed service and no alternative => robust infeasible.
- R2: E06 B_R=1, two possible failed service edges => sensing-first and gate-first interleaving infeasible for robust recovery.
- R3: E06 B_R=2 => sensing-first restores both; gate-first interleaving restores gate plus targeted edge.
- R4: E06 B_R>=3 => both classes feasible; no feasibility separation.
- R5: Symmetric test epsilon=0 => one test perfectly identifies state.
- R6: Symmetric test epsilon=1/2 => no information; success ceiling 1/2.
- R7: epsilon in (0,1/2), alpha=1 => one test cannot guarantee robust success.
- R8: Cost of gate exceeds budget after reserving service restoration => gate-first strategy infeasible.
- R9: Composite universal bypass affordable => zero-probe solution dominates any mandatory-sensing assertion.

All are derived contract expectations, NOT results of software test execution.
