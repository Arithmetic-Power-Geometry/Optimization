# E18 — Mininet setup and gated execution
Date: 2026-10-21. Status: **BLOCKED in current environment**.

## Recommended isolated Linux environment
Use a disposable Ubuntu VM or isolated lab host with working Linux network namespaces and root/sudo, Mininet 2.3+ and Open vSwitch installed. Follow official Mininet installation: https://mininet.org/download/ . Confirm:
```sh
python3 --version
mn --version
ovs-vsctl --version
ovs-ofctl --version
sudo mn --switch ovsbr --test pingall
```
Record kernel, distribution, Mininet and OVS versions, Git commit, namespace capabilities, exact command exit codes and stdout/stderr. Run the last command only in a disposable environment where creating network namespaces/bridges is authorized. Never claim Mininet tests ran solely because root is available.

## Mandatory source/data gate
From a full, checksum-verified repository checkout:
```sh
python3 extension/data/e15_validate.py
python3 extension/experiments/e16_matched.py
python3 extension/experiments/e17_ablation.py
python3 extension/mininet/e18_preflight.py
```
These three E15–E17 Python commands **were not executed during E18**; their gate remains open. Existing connector-level content checks are not substitutes.

## Proposed prototype
```sh
sudo python3 extension/mininet/e18_mininet.py --topology Abilene --seed 101 --repair-budget 1 --output extension/results/E18_MININET_ACTUAL.json
```
This is a **diagnostic plumbing prototype**, not a fair decision-policy evaluation. It selects a failed edge using a synthetic seed and uses its identity to repair the exact failed link, a hidden-state oracle that must not be passed off as a deployable policy. `observe()` is a single endpoint ping; `verify()` measures end-to-end reachability, not a fixed selected path, because OVS can reroute. Probe-admissibility and matched budget checks require independent extension before a comparative experiment. No Mininet output file was generated in E18. Do not use the prototype for superiority or real-fault claims.

## Actual blocker
The execution host reported Python 3.13.5 on Linux 6.18.55 x86_64, euid 0, missing `mn`, `ovs-vsctl`, `ovs-ofctl` and Python `mininet` package. `ip` and `ping` are available; GitHub DNS resolution fails. Dependency installation was not attempted (unavailable network and system mutation not required). No actual OVS bridge, veth, packet loss or recovery measurement occurred.
