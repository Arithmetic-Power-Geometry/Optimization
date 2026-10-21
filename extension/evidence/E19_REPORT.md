# E19 — ns-3 packet-level validation
Date: 2026-10-21.

## Required execution gate — NO-GO
Read the exact E19 prompt, master README, progress and E18 blocker. Actually inspected the local Linux host. Python 3.13.5, kernel 6.18.55 x86_64; compiler, CMake and Ninja present, but ns-3 executable, Python bindings and source absent. DNS to github.com failed. No ns-3 installation was attempted and no simulator build, test, packet flow, routing convergence or link restoration was executed.

## Reproduction prerequisites
E15, E16 and E17 Python validation/reproduction remain **NOT EXECUTED** due to unavailable complete local checkout. Prior GitHub connector source-hash checks are not a substitute. ns-3 dependency and E15–E17 execution gates must pass before packet-level claims.

## Committed artifacts
Standard-library host preflight `extension/ns3/e19_preflight.py`; proposed, version-unfrozen experimental protocol `extension/ns3/E19_EXPERIMENT_CONFIG.json`; official installation and validation instructions `extension/validation/E19_NS3_SETUP.md`; observed host blocker JSON and this report. The protocol specifies historical graph topology with **synthetic injected failures**, matched seeds, budgets and prospective packet counters. All traces, packet metrics and simulated repairs are **NOT EXECUTED**; no synthetic outputs masquerade as measurements.

## Prior art and claims
DRD/HEC decision-region selection (Javdani et al. 2014), network tomography and DDID are existing methods. This stage provides no new comparison, novelty, packet-level evidence, or superior algorithm. Static routing must not be described as converging dynamically. Software recovery is not field repair.

## Scientific verdict
**E19 NO-GO for ns-3 packet-level validation**; host inspection EXECUTED, ns-3 study BLOCKED. The original E08 originality NO-GO, E01 manuscript-byte freeze BLOCKED, CAIDA acquisition BLOCKED, Mininet E18 NO-GO, inactive CI and E15–E17 Python gates persist. E20 requires explicit author authorization; E19 STOPS before E20.
