# E17 — Ablation failure modes and distribution shift
Date: 2026-10-21.

**Execution:** 960 rows produced and checked using JavaScript in the GitHub connector environment. 3 verified historical Topology Zoo graphs, 20 E13 seed identifiers, 2 repair budgets, 8 scenarios. All failures are SYNTHETIC. E15/E16 Python validators remain **UNEXECUTED**; E17 Python reproduction script also **UNEXECUTED**. Source content checks via connector passed, but they are not Python runtime validation.

## Scope and non-effects
The original E16 fixed-path comparator never executes probes. Consequently:
- `no_adaptive_probes` is identical to baseline by construction, NOT evidence adaptive probes are useless in the general model.
- `no_post_repair_probes` is identical to baseline by construction, NOT evidence post-repair sensing is useless.
- `no_decision_sufficiency` is a **placeholder no-op**: there is no implemented decision-sufficiency algorithm to ablate. These rows cannot support a decision-sufficiency finding.
- `noisy_full_path` flips a synthetic observation indicator on seed-index multiples of five, but no policy observes or reacts to it. Identical outcomes are a **negative test of experimental sensitivity**, not noise robustness.

## Actual model changes
- `heterogeneous_costs`: repairs on even path positions cost 2 and odd positions cost 1; total repair budget unchanged; first affordable edge greedy ordering. Changes the physical cost model and selected repair set; not a pure policy ablation.
- `correlated_failures`: adjacent path-edge pair failed together; all failed edges must be repaired to restore fixed path. Changes the fault model, not just the policy. No independent distribution estimation.
- `shifted_prior`: first edge failed for 16 of 20 seed-index episodes, otherwise one of the remaining positions. This is a **deterministic severe distribution shift**, not iid sampling; the baseline repairs edge 0 first, so the high observed success is a design artifact and must not be presented as a generalizable gain.

## Observed aggregate success (out of 40 budget episodes per graph)
| Network | Baseline | Heterogeneous costs | Correlated failures | Shifted prior |
|---|---:|---:|---:|---:|
| Abilene | 12 | 8 | 4 | 33 |
| Geant2012 | 7 | 5 | 2 | 32 |
| Arpanet19728 | 6 | 4 | 2 | 33 |

## Scientific gate
No informative feasible probe, alternative route, dynamic repair, full E11 policy, independent Python execution, measurement-noise robustness or real-network fault was demonstrated. The fixed-path model is insensitive to several nominal ablations. Novel algorithm and theorem remain NO-GO. E18 simulator eligibility is not established.
