# E11 — Matched baselines and limitations matrix
Date: 2026-10-20. Implemented code; executable tests committed but NOT YET EXECUTED in this stage.

| Baseline | Rule | Admissibility and budgets | Main limitation |
|---|---|---|---|
| diagnosis_first | Maximize weighted Gini partition reduction until probe rights exhausted; then repair with maximum immediate weighted success | Common E09 admissibility; unit-cost repair/probe/time | Can waste probes on zero-information paths; not a published optimal diagnosis algorithm |
| repair_first | Restore edge maximizing current one-step service probability; probe only when no repair affordable | Identical rights and budgets | Can repair wrong edge and waste scarce budget |
| random | Uniform seeded random choice among common feasible probes and restorations | Identical rights and budgets | RNG draw order depends on belief-tree traversal; seed 20261020 default |
| cost_sensitive_greedy | Compare one-step repair-success mass and normalized Gini gain per unit action cost | Identical unit costs; no heterogeneous action costs | Heuristic incomparable surrogate quantities; **not a proven cost approximation** |
| drd_region_greedy | Probe to reduce weighted pair conflicts between hypotheses lacking a common successful one-edge repair; otherwise greedy repair | Identical rights and budgets | **DRD-inspired only, NOT HEC**; no hyperedge construction, no HEC objective, no HEC guarantee |

## Crucial distinctions from published HEC
Javdani et al. (2014) optimize expected cut hyperedge weight for overlapping decision regions. E11's `drd_region_greedy` instead counts weighted incompatible hypothesis pairs and restricts decision-region semantics to successful *single-edge* repairs. Pairwise conflict reduction is not generally equivalent to HEC for overlapping regions. No reproduction of the authors' original HEC software, approximation factor or theorem is claimed.

Primary source: https://proceedings.mlr.press/v33/javdani14.html ; extended paper https://publications.ri.cmu.edu/storage/publications/pub_files/2014/4/javdani14hec_extended.pdf . Same 2014 research work, not two distinct studies.

## Fairness and methodological restrictions
All five baselines receive the same `Problem` object, initial state hypotheses, service predicate, probe list, repair list, time horizon, resource budgets and prior. They act on belief sets, not the true hypothesis ID. Physical probe outcomes are used only to partition hypotheses after taking the probe; no inadmissible probe is treated as DOWN. Every action debits budget once using E09 kernel. Tie breaks follow fixed candidate order except random.

**Critical policy-information limitation:** baseline scores simulate outcomes of each possible hidden state within the belief set; this is planning over a known model, not disclosure of the true state. However public configuration consistency beyond common budgets is not validated by E10 `Problem`, so callers must supply a genuinely common information state.

**Critical measurement limitation:** success probability is terminal service probability, not identification accuracy. Report probe and repair attempts separately. No runtime or performance advantage measured. The DP oracle is a ceiling on achievable Bayesian success under its deterministic assumptions, not an empirical benchmark of real network repair.

**Other exclusions:** no repair-dependent monitor activation policy, no composite repairs, no stochastic failures, no noisy measurements, no heterogeneous costs, no externally verified published HEC implementation, no topology insertion. Original theorem novelty remains NO-GO.
