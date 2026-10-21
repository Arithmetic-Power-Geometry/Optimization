# P04 preregistered pilot protocol — 2026-10-21

**Status: LIMITED SYNTHETIC PILOT.** P03 and P02 are partial; this protocol does not claim the full P04 benchmark gate.

## Research questions
RQ1: Does exact finite-horizon adaptive repair outperform a myopic immediate-restoration policy when physical access gates informative probes?
RQ2: Does the advantage vanish when probes are uninformative or two service-edge repairs suffice?
RQ3: How sensitive is the gap to repair/probe budgets and number of possible failures?

## Model, matching and estimands
Uniform-prior finite-state synthetic worlds, deterministic UP/DOWN measurements, unit repair and probe budgets, physically gated path probes. Primary outcome: Bayesian probability of restoring all service edges within budgets. The exact oracle is optimal only under these assumptions. The comparator is a one-step greedy repair heuristic (not a published baseline). For each instance, policies see identical worlds, feasible actions, budgets and probes. Secondary: optimality gap, exact-oracle explored states, runtime; costs/downtime/noise and robust zero-error are NOT estimated by the P03 model.

## Frozen pilot design
- 30 deterministic pseudo-random synthetic instances with seeds 0–29, graph labels representing a service path of 3–5 edges, three distinct single-service-edge fault worlds plus one common failed gate, access via the gate. Repair budget 2, probe budget 2.
- Include negative controls: full-path uninformative probe; sufficient repair budget for all service edges; zero-probe budget; no-gate baseline.
- Report paired per-instance exact vs myopic success probability and descriptive bootstrap intervals from resampling instances. These are deterministic constructed scenarios, **not 30 independent real network outages**.
- Explicitly label structural access assumption; a probe on a service edge with gate access is a physical path only when monitor placement/graph connectivity realizes that path. The abstract P03 model checks declared access/measurement edge lists but does not verify graph adjacency or route continuity. Therefore this is a **formal probe abstraction pilot**, not topology-valid network simulation.

## Required later gates
Historical E14/E16/E17 source provenance and exact rerun; faithful HEC/decision-region baseline; strong VOI/probe-greedy and diagnosis-first comparators; graph-verified monitor paths; multiple/correlated failures; 1/2/5/10 budgets, cost heterogeneity, noisy tests, bootstrap/power, paired seeds and controlled ablations; diverse public GraphML topologies and licensing; clean-checkout run of exact committed P03 files; packet-level Mininet/ns-3 validation if available. These are **not satisfied** by the pilot.
