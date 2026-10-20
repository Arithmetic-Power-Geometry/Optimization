# E01 — Falsifiable research question register
Date: 2026-10-20. All research targets below are **UNPROVED HYPOTHESES**, not manuscript contributions.

## Primary research question
Under physically feasible end-to-end path probes, irrevocable interventions and limited repair budgets, when does an adaptive repair policy exploit intervention-dependent observability to achieve a verifiable cost/success advantage over diagnosis-first and overlapping decision-region baselines under identical information and intervention rights?

## RQ1: Decision sufficiency versus full diagnosis
Define Q_D(G) as minimum feasible path-probe cost for exact state identification and Q_R(G) as minimum cost to identify a robustly valid repair, holding the same admissible path set, initial uncertainty, intervention budget and validity guarantee. Search natural graph families with a tight, nontrivial gap, and test whether it is a direct corollary of published decision-region determination. Counterexample gate: universal repair, uninformative probes, no common action, infeasible diagnosis.

## RQ2: Repair-induced observability
Let physical edits alter the graph and/or monitor access, so future probes may become feasible or informative. Quantify the benefit of interleaving over fixed sensing-first policies with identical edit rights and budgets. Disprove novelty if it reduces to known decision-dependent information/POMDP without a distinct graph-family theorem.

## RQ3: Irreversible repair budget
Derive tight robust or chance-constrained impossibility bounds under limited interventions, explicitly distinguishing a failed attempt, restoration and probing after restoration. Avoid confusing one-repair impossibility with a two-repair universal fix.

## RQ4: Algorithm and validation
Only after E08 proof/originality gate, specify a candidate algorithm and matched baselines. Use exhaustive oracle for small cases and independent state-transition checker; no claimed speedups before actual reproducible runs.

## RQ5: Application
Test telecom backbone graph restoration with documented synthetic failures on public graph topologies; optionally validate virtual connectivity in Mininet and packet behavior in ns-3. Neither is a field repair experiment.

## Mandatory falsification and prior art
HEC/DRD Javdani et al. 2014; EC2 Golovin/Krause/Ray 2010; ECED Chen/Hassani/Krause 2017; Ma et al. tomography 2015/2017; Tootaghaj et al. uncertain recovery; Omer/Poss/Rougier 2024 DDID. No new theorem claim until the E08 adversarial gate explicitly passes.
