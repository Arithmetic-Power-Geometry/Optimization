# P04 pilot reproduction — 2026-10-21

**PARTIAL, NOT SUBMISSION-READY.**

A local reconstruction of P03's ten unit-test contracts passed. This was not a clean checkout of byte-identical GitHub source. A 30-seed deterministic pilot generated 30 abstract-world gate cases. All cases used one common failed access gate, three alternative service faults, two repair actions and two probes. Exact oracle success was 1 and myopic heuristic success was 2/3 in each case. These are related synthetic cases, not independent network outages or distinct network mechanisms. The degenerate descriptive bootstrap interval is [1/3,1/3], and does not imply generalization.

Negative controls: uninformative full-path tests gave 1/n for n=2,3,5,8; disabling probes gave 2/3 in the gate example; sufficient repairs without probing gave 1. The P03 model does not check physical route connectivity or monitor placement. No real graph data, historical E14/E16/E17 rerun, packet simulation, cost/noise study, or published Hyperedge Cutting comparison was completed. The local environment lacked ns-3 and Mininet. The oracle optimizes Bayesian terminal success, not the manuscript's robust minimax total cost.

GitHub includes a reproducible pilot script, normalized 30-row CSV and summary JSON. Reproduction commands:
`PYTHONPATH=latest/src python -m unittest discover -s latest/tests -p test_p03.py -v`
`PYTHONPATH=latest/src python latest/src/p04_pilot.py`
These commands remain to be executed on a clean GitHub checkout. The generated output schema differs from the normalized committed CSV, so compare substantive results rather than file hashes.

**P04 is only a pilot. STOP BEFORE P05.**
