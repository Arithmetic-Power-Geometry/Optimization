# E19 — ns-3 setup and execution prerequisites
Date: 2026-10-21. Status **BLOCKED: ns-3 absent**.

Official primary guide: https://www.nsnam.org/docs/installation/singlehtml/ . Install a supported release from https://www.nsnam.org/releases/ in an isolated non-root Linux workspace, with compiler, Python, CMake and Ninja. Record the exact release tag, Git commit, OS/kernel, compiler, CMake and runtime versions.

From the ns-3 source root:
```sh
./ns3 configure --enable-examples --enable-tests
./ns3 build
./test.py
./ns3 run first
```
All four commands are **PROPOSED, NOT EXECUTED** here. The ns-3 project uses a CMake-backed `./ns3` launcher for builds and runs. A working compiler alone is not ns-3. Do not run ns-3 source builds as root unnecessarily.

From the complete Optimization checkout, independently execute the open Python gates:
```sh
python3 extension/data/e15_validate.py
python3 extension/experiments/e16_matched.py
python3 extension/experiments/e17_ablation.py
python3 extension/ns3/e19_preflight.py
```
The first three remain **NOT EXECUTED** in this session. GitHub connector SHA verification is not Python execution. E16 may contain JS/Python lexical-order mismatches; resolve by comparison, not rewriting frozen raw results.

## Conditional study plan
E19_EXPERIMENT_CONFIG.json is a **PROPOSED** manifest, not a run log. First validate a two-node point-to-point packet flow; then verify one Zoo topology at a time and freeze source/destination, link capacities/delays, traffic rates, failure/repair times, budget, seeds, monitor access and actual policy implementations. Match all comparators on identical synthetic faults. Export per-packet traces and packet counters, document service loss and recovery definitions, and rerun independent seeds. If using static GlobalRouting, **do not label any metric routing convergence** without explicitly implemented dynamic routing or triggered recomputation. Do not infer physical repair from software link recovery.

## Actual E19 blocker
On inspected host: Linux 6.18.55 x86_64, Python 3.13.5; `cmake`, `ninja`, `g++` and `git` available; no `ns3`, `ns-3`, `waf`, ns-3 source in inspected standard locations, or importable `ns`, `ns3`, `cppyy`. DNS lookup for github.com failed. No simulator downloaded, configured, built or executed; no packet measurements or ns-3 trace files produced.
