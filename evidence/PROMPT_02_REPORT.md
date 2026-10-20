# Prompt 02 — classical optimization and structural creation audit
Date: 2026-10-20

## Scope and method
Targeted searches for foundational and recent papers on column generation, decomposition, extended formulations, representation complexity, bilevel optimization and automated formulation. Seven sources E004-E010 retained after checking publisher/archival metadata and abstracts. No full-text theorem-by-theorem verification claimed.

## Key results
1. Dantzig-Wolfe (E004) creates columns within an existing mathematical model.
2. Benders (E005) and its later survey (E010) establish decomposed design/operation decisions.
3. Yannakakis (E006) studies adding variables and constraints to represent polytopes; Rothvoss (E007) proves exponential extension complexity for perfect matching.
4. Bilevel optimization (E008) already jointly handles upper/lower decision levels.
5. Autoformulation (E009) already searches alternative solver-ready mathematical formulations.

## Reduction challenge
For finite hidden states, observations, actions and time horizon, a sensory-creation policy can be represented by a policy tree or occupancy-measure formulation in a stochastic optimization model. Costs of sensing, creating and verification can be assigned to transitions/terminal decisions. Thus *ability to encode the problem* is not novel. A meaningful theorem must concern succinctness, complexity, informational restrictions, certificate generation or algorithmic performance under explicit assumptions. Extension-complexity lower bounds for LPs cannot be generalized to all computation models.

## Precise research questions
Q1. Under which specified sensor kernels and model families is the best certificate-valid transformation identifiable with fewer observations than any nonadaptive policy?
Q2. Does independent certification of a chosen structural change introduce a measurable separation between expected reward maximization and verified decision making?
Q3. Can we establish matched upper and lower bounds counting sensing, creation, and certificate cost, while allowing the baseline the same primitive actions?

## Next work
Prompt 03: canine olfaction, infotaxis, plume tracking and noisy multimodal sensing. Do not implement algorithms, run experiments, or draft manuscript.
