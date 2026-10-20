# E09 — Executable physical graph kernel
Date: 2026-10-20. Python 3.11, standard library only. Deterministic, no random seeds.

## Reproduce
From repository root:
```sh
python3.11 -m unittest discover -s extension/tests -p 'test_*.py' -v
```
No pip installation required. `extension/requirements.lock` records zero external dependencies.

## API
`extension/src/physical_graph.py` provides frozen typed Edge, Probe, Budget, State; `admissible` (monitor/path/route rights, independent of UP/DOWN); `outcome` (binary path status); `probe` (single budget debit and history); `restore` (one irrevocable restoration attempt, success/failure cost, optional public monitor/pair activation); `service` (all demand pairs connected by UP edges); `common_admissible` (no hidden-state feasibility oracle); deterministic `series_failure` and `gate_failure` fixtures.

## Explicit scope limitations
- Simplified CAP/CSP/UP rights; no actual routing protocol or packet delivery model.
- Installed undirected multigraph; no topology insertion or monitor relocation actions.
- `restore` accepts a controlled success flag for deterministic countermodels; stochastic repair distributions, Bayesian beliefs, noise and independent policy optimizer are NOT implemented.
- History is a physical event trace; policies must only receive authorized observations, not physical State. No end-user policy interface exists yet. Full information-flow noninterference is therefore UNVERIFIED.
- Tests are unit-level correctness contracts, not a field experiment or algorithm benchmark.
- A failed repair exposes SUCCESS/FAILED in the stored history; feedback rights are assumed public for this kernel.
- Probe time and repair time are nonnegative integers; repair cost is one unit per attempt, probe cost one unit per attempt.
- Repeated restoration of the same edge is disallowed even after a failed attempt.

## Research gate
Original-theorem novelty remains NO-GO after E08. E10 must implement a separate exact checker and independent transition enumeration. Passing kernel tests does not validate an original theorem.
