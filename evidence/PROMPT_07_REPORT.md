# Prompt 07 — Proof logging, formal verification, proof complexity
Date: 2026-10-20

## Sources and inspection
E041-E049: nine primary publications added; 48 cumulative records. Publisher abstracts, proceedings metadata, institutional abstracts and primary project documentation inspected; no claim of exhaustive full-text proof checking. DOI metadata cross-check is incomplete for some author lists (notably E048); further bibliography audit needed.

## Direct evidence
E041 DRAT-trim: SAT proof-log checking.
E042 VIPR: rational mixed-integer branch-and-cut certificates.
E043 Koops et al. CP 2025: VeriPB/CakePB proof logging and formally verified checking for pseudo-Boolean optimization, with measured overhead.
E044 Cook-Reckhow: proof-system complexity, warning against proof-size claims without fixed proof language.
E045 Kazemian et al.: header-space static network checks.
E046 Andersen et al.: mixed-integer infeasibility certificates.
E047 Klep-Schweighofer: SDP certificates/duality differ from simple LP Farkas settings.
E048 NetKAT: network policy semantics and formal reasoning.
E049 Wood et al.: SMT characterization of VIPR checker semantics.

## Adversarial counterexamples
(1) Graph bridge: certificate for s-t connectivity is a path, checkable in polynomial time; a sensing-first path-selection procedure does not create a new certification mechanism.
(2) Hidden edge failure: a certificate for a graph inferred from noisy measurements may be valid for the *wrong graph*. The checker cannot infer true edge state from the witness alone. Either certify for every state in a known uncertainty set or state a calibrated probabilistic guarantee; neither is equivalent to observing truth.
(3) Proof-system dependence: an exponential lower bound for resolution proof length does not imply the same lower bound for arbitrary proof systems or algorithms. Encoding matters.
(4) Optimization objective: a feasible solution is not automatically a certificate of global optimality; lower bounds, duality or proof logs may be required.

## Candidate model — NOT A THEOREM
Let theta be unknown physical/network state; sensing policy pi collects Y; transformation tau changes encoded structure; witness w is checked by a deterministic polynomial-time V(I,tau,w). Costs: sensing C_s, construction C_tau, witness-generation C_w and checking C_V. Require explicit quantifier: for all theta in U, or with probability at least 1-delta, or only for a revealed instance. These are different research questions. Unrestricted finite policy trees remain expressible as POMDPs; only a *restricted-model* separation or bound could be new.

## Novelty gate
Broad certification novelty REJECTED. Narrow joint information/creation/proof-system cost bound remains a hypothesis. Prompt 08 should search 2023–2026 advances in certified optimization, adaptive verification, stochastic network design and decision-dependent information, including direct counterclaims. Do not write software or manuscript.

## Sources
Primary source URLs and DOIs are in evidence/literature_registry.csv. Some entries remain abstract-level and must not be represented as fully audited.
