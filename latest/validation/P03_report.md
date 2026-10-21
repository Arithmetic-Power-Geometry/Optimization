# P03 validation and execution report — 2026-10-21

**Result: PARTIAL / CONDITIONAL RESEARCH NO-GO.** P03 produces executable model source, deterministic tests, independent checker evidence and a counterexample against a myopic heuristic, but **does not** deliver a novel algorithm, theorem, full independent GitHub clean-checkout reproduction or paper-ready comparison.

## Committed code
- latest/src/network_repair.py: finite-state model, access-constrained probes, irreversible repair, exact uniform-prior Bayesian oracle, non-novel myopic policy, examples and CLI.
- latest/tests/test_p03.py: 10 deterministic test functions, including path bound, gate availability, adaptive value, no-query universal repair, no-budget case, indistinguishability, one-repair restriction, negative control, world-permutation invariance, no-interleaving advantage.
- latest/requirements.txt: Python 3.11+ standard library; no third-party dependency.
- latest/theory/PROOF_GATE.md: definitions, argument, adversarial controls and novelty NO-GO.

## Independent execution
Local independent implementation: independent_checker.py (downloadable P03 package). Command: `python independent_checker.py`. Output: `INDEPENDENT CHECKER: PASS 11 assertions (7 path bounds + 4 cases)`. This independent checker does not exercise the exact committed kernel file; clean-checkout runtime gate remains OPEN.

## Measured exact values
- 3-world access-gate example, r=2, q=2: exact optimum = 1, myopic heuristic (by direct deterministic reasoning) = 2/3.
- Same example r=1, q=2: optimum = 1/3.
- One-fault n-edge path with uninformative full-path probe and one repair: optimum 1/n for n=2,...,8.
- Two-fault-alternative path, one repair: optimum 1/2.
- Two alternative faults, two repairs: optimum 1 without any probing.

## Scientific cautions
This code uses a uniform prior, noiseless observations, unit action budgets and terminal success, **not** the original paper's robust worst-case cost objective. No new complexity theorem, approximation guarantee, real topology experiment, ns-3 or Mininet execution. P02 remains partially incomplete: 59 registry items lack independent primary metadata verification. No revised manuscript PDF is claimed for P03. Full GitHub artifact binary/source freeze from P01 remains open.

## Reproduction
From GitHub checkout:
`PYTHONPATH=latest/src python -m unittest discover -s latest/tests -p 'test_p03.py' -v`
`PYTHONPATH=latest/src python latest/src/network_repair.py`
These commands are specified but have not been executed against a fresh checkout in this run. A later executor must run them, record actual output and fix any failures before P03 can be marked fully validated.

**STOP before P04.** Do not promote this example to an original-optimization claim.
