# E05 — Independent proof obligations and adversarial checks
Date 2026-10-20. Status: analytic audit; no independently executed oracle.

| ID | Obligation | Analytic result | Residual risk |
|---|---|---|---|
| O1 | Every p_i installed and testable in failed state | Yes: admissibility independent of edge-UP, terminal monitors present | Assumes reliable DOWN reporting |
| O2 | Hidden states (j,L) and (j,R) have identical full test signatures | Yes: vector all UP except coordinate j | Adding internal monitors invalidates |
| O3 | Group repair a_i restores both candidate edge failures | Yes by explicit indivisible two-edge action | Not valid if repairs are edge-specific |
| O4 | Service demands require all branches UP | Yes, D includes every terminal pair | Changing to any-branch success collapses |
| O5 | Worst-case lower bound n-1 | Yes: all-UP transcript preserves every untested branch; a_i only one branch | Only for deterministic, noiseless, pre-repair probes |
| O6 | Upper bound n-1 | Yes: sequentially test n-1 branches and repair first DOWN or last | Probe/repair budget must allow n-1 probes and one edit |
| O7 | Expected-cost formula | Yes: n=2 ->1; n=3 ->5/3; n=4 ->9/4; closed form (n-1)(n+2)/(2n) | Only uniform branch prior, unit test cost |
| O8 | No direct inspection | Yes: u_i not a monitor; only p_i permitted | Access policy must be enforced |
| O9 | No hidden-state leakage | Yes: all p_i are commonly admissible before repair | Changed access policy requires re-audit |
| O10 | Novelty | **FAIL**: static partition DRD and tomography | Cannot promote P1/P2 as original |
| O11 | Executable oracle | NOT EXECUTED in E05 | Required E09/E10 |
| O12 | Post-repair observation and interleaving | NOT STUDIED in E05 | Required E06 |

## Independent audit note
The proof was adversarially checked by explicitly testing the assumptions above, but no separate independent human referee or software enumeration has been performed. Do not describe it as independently verified originality.
