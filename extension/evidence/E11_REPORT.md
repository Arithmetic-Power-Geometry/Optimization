# E11 — Baseline implementation and fairness audit report
Date 2026-10-20

## Executed work
Read E11 prompt, extension preservation contract, progress and E10 report, reviewed E09/E10 kernel and oracle interfaces. Implemented five deterministic/seeded policy heuristics under shared E10 `Problem` semantics: diagnosis-first, repair-first, random, unit-cost greedy, DRD-inspired pair-conflict greedy. Added seven test methods, a fairness/limitations matrix and a reproduction plan. Publisher PMLR primary paper and CMU extended report inspected for original HEC distinction; the CMU report is an extended version of the same research work.

## Verification classification
**COMMITTED CODE / NOT EXECUTED in E11.** No actual baseline performance numbers or pass counts are asserted. Tests encode expected correctness properties but require execution. The prior E10 20/20 tests are historical and do not validate the new E11 code. No original HEC implementation, no simulation, no field measurements, no statistical comparison.

## Scientific gate
E11 PARTIAL GO: baseline implementations exist and share rights, but test execution and independent comparison remain mandatory before E12 experimental-policy development. E08 originality NO-GO unchanged. Eight-page original manuscript byte snapshot remains BLOCKED. STOP before E12.
