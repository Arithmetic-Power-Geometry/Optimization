# Prompt 06 — Network augmentation, repair, endogenous design and validity
Date: 2026-10-20

## Method and inspection limits
Targeted primary publisher and institutional discovery; seven newly retained sources E034–E040, 39 cumulative records. Inspected publisher abstracts/accessible excerpts and cross-checked several bibliographic identifiers. This is not a systematic full-text review. E038 complete authors, E039 DOI/venue, E040 authors/venue remain unresolved and are explicitly flagged in BibTeX. Existing E023 (joint sensing/routing), E029 (priced probing and spanning trees) and E021-E025 (endogenous information) are key direct comparators.

## Findings
E034 Jain: survivable network creation already has factor-2 approximation guarantees.
E035 Dhamdhere-Ravi-Singh: stochastic spanning-tree design has algorithms and hardness.
E036 Wood: bilevel network interdiction and mixed-integer formulations predate this proposal.
E037 Cormican-Morton-Wood: stochastic adversarial network flow decisions already studied.
E038 Rysz et al.: explicit *vertex addition/removal after observed random edge changes* to restore structural graph properties. This is direct contradictory evidence to claiming new feasibility creation under uncertainty.
E039 Tootaghaj et al.: progressive network repair under uncertain damage *interleaves repair decisions and information gathering*. This is a particularly strong counterexample to any claim that sensing-then-repair or interleaving is novel.
E040 Origami fault-tolerance verification: formal verification of network behavior under faults predates this programme. Do not assert that all verification of created structures is new.

## Novelty implications
REJECT: creating network nodes/edges to recover feasibility is new; sensing and network repair interleaving is new; stochastic design with uncertain topology is new; network fault verification is new.
UNVERIFIED: a new *joint information / construction / certificate-complexity bound* under a sharply specified model with independently checkable transformation witnesses, including matched policy baselines. Existing network repair plus formal verification may already cover some application-level combinations; avoid novelty claims until Prompt 07.

## Explicit adversarial counterexamples
1. Simple network with disconnected terminals s,t: adding a bridge restores connectivity. This is classic network augmentation, not a new theory.
2. Network damage is unknown: probing a candidate edge and then repairing another based on the result is already captured by stochastic probing (E029) and progressive repair (E039).
3. A verifier checks k-edge-connectivity of a repaired graph: this is a polynomial graph property, so calling it a certificate does not automatically yield a new complexity barrier.
4. Any finite-horizon belief-state action policy can be expressed by an augmented POMDP; novelty must be in proven succinctness, complexity or cost separations, not expressiveness.

## Surviving theory question
Choose an explicit certificate relation R(theta,tau,w), independent verifier V, observation channel P(y|theta,s), and costs c_s,c_tau,c_V. Prove an upper/lower bound for the optimal policy subject to an actual witness-validity condition. Ensure certificates do not magically reveal hidden theta. Distinguish posterior confidence from proof of universal or state-specific correctness.

## Next research gate
Prompt 07: proof logging, formal methods, optimization certificates, proof complexity, robust validity and the boundary between statistical confidence and mathematical certification. No code, experiments or manuscript.
