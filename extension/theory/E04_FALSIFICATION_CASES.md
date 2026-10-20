# E04 — Minimal falsification and semantic test cases
Date: 2026-10-20. Status: mathematical thought-experiment specifications; NOT executed software tests.

| Case | Graph/state | Proposed action | Required model verdict |
|---|---|---|---|
| F01 failed-but-testable | V={s,t}, installed edge e failed, monitors s,t, CAP | probe walk s-e-t | Admissible; observation DOWN. Never conflate DOWN with action inadmissibility. |
| F02 absent physical link | V={s,t}, e not installed | probe walk s-e-t | Inadmissible; no DOWN observation unless failed-attempt feedback explicitly modeled. |
| F03 inaccessible endpoint | V={s,t}, installed edge e, monitor set {s} | probe s-e-t | Inadmissible despite e being UP. |
| F04 routing control | triangle s-u-t with direct s-t; UP mode route fixed s-t | probe s-u-t | Inadmissible under UP, possibly admissible under CSP. |
| F05 state-hidden feasibility | theta1 permits p; theta2 prohibits p; controller cannot distinguish | select p | Forbidden by common-feasible rule; no hidden oracle. |
| F06 restorative probe access | damaged monitor access link e; restore e | then probe p | Probe availability may change only via explicit public access-state transition; no automatic access from unknown repair success. |
| F07 universal bypass | any failures of path edges, permitted affordable bypass s-t | install bypass | Zero prior probes can suffice; no universal positive sensing lower bound. |
| F08 n-edge series | exactly one failed edge, only full-path probe; budget one repair | choose restore(e_i) | Robust success impossible n>=2; uniform prior best 1/n; later verification does not recover failed choice. |
| F09 two repairs | two-edge series path, one failed, two repair units | restore both | Robust service possible; invalidates any unrestricted one-repair impossibility claim. |
| F10 unsuccessful repair | failed edge repair attempt with probabilistic failure | attempt restore(e) | Repair unit charged even if failure; posterior includes unsuccessful state. |
| F11 topology edit | install new s-t bypass | compare to restore existing e | Distinct action class; different cost/permissions and E_x transition. |
| F12 noise | one edge UP, test may falsely DOWN | observe DOWN | Posterior update uses likelihood, not hard elimination. |
| F13 terminal double count | one repair already executed, stop after verification | terminal decision | Do not charge repair twice. |
| F14 signed wrong sensor | signed DOWN on physically UP path | accept record | Signature proves provenance, not physical truth; sensor model governs correctness. |
| F15 vector budgets | b=(1 repair,1 probe), probe then two repairs | plan | Reject second repair; nonnegative componentwise accounting. |
| F16 no operational path | two installed routes both contain failed edge | service predicate | Service false even if route is selectable and DOWN observable. |
| F17 zero-probability observation | posterior assigns zero likelihood to observed outcome | Bayes update | Undefined conditional posterior: flag model inconsistency; no arbitrary normalization. |
| F18 monitor relocation | move monitor under allowed action | re-evaluate probe set | Availability changes only if access policy/monitor transition specifies it. |

## Execution and novelty status
All F01–F18 are model-contract examples and expected outputs, not measured test passes. E09/E10 must implement executable versions and preserve failed cases. These examples do not establish novelty.
