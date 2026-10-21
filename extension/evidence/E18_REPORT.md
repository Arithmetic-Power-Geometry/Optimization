# E18 — Mininet prototype and validation gate
Date: 2026-10-21.

## Executed environment inspection
Local container inspected: Linux 6.18.55 x86_64, Python 3.13.5, euid 0; no `mn`, `ovs-vsctl`, `ovs-ofctl` binaries, and no importable Mininet Python module. `ip` and `ping` exist. GitHub DNS resolution failed with `[Errno -3] Temporary failure in name resolution`. Mininet and OVS not available. These are actual observed environment facts, not estimated package versions.

## Earlier reproduction gates
E15, E16 and E17 Python reproduction scripts remain **NOT EXECUTED** because original GitHub-fetched files are not mounted into this container and DNS blocks repository checkout. GitHub connector previously confirmed source GraphML and cleaned-file content, but that does not satisfy Python runtime verification. E18 does not claim to have resolved this gate.

## Committed E18 artifacts
Guarded Linux Mininet+OVS demonstration in `extension/mininet/e18_mininet.py`, standard-library dependency preflight in `extension/mininet/e18_preflight.py`, precise host blocker JSON, setup/reproduction protocol, and this report. The Mininet demonstration was **NOT EXECUTED**. Its repair step uses hidden failure identity, so it is a diagnostic oracle, NOT a valid hidden-state-blind research policy. It reports endpoint ping reachability, not the E16 fixed-route service predicate; those are different metrics. No measurements, simulated outage results or benchmark superiority claimed.

## Scientific decision
**E18 NO-GO for Mininet validation and ns-3 readiness.** Only the environment inspection was executed; prototype and reproducibility instructions are committed as PROPOSED. The original E08 theorem originality NO-GO, manuscript source BLOCKED, CAIDA access BLOCKED, inactive GitHub CI and E15–E17 Python gate remain open. E19 requires separate author authorization and an actually available ns-3 environment; no E19 execution started.
