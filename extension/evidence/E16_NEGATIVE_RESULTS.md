# E16 negative results and validity threats
Date: 2026-10-21.

- No unique superior repair algorithm emerged. Under the uniform single-fault, no-informative-probe model, **every fixed choice of r distinct path edges has identical theoretical expected success min(r,L)/L**. This follows by counting r favorable equally likely failure positions out of L. Observed finite-schedule differences cannot establish algorithmic superiority.
- Across 40 paired budget episodes per graph, feasible first-r oracle successes: Abilene 12, Geant2012 7, Arpanet19728 6. Other policy realized counts differ because of deterministic balanced fault ordering; these are not unbiased random samples.
- The E11 implementation was not invoked on the full Zoo graphs; the E16 policies are restricted, documented adaptations. Diagnosis-first performs zero diagnostic probes, so it is a reversed-order comparator, not an active diagnosis benchmark. No HEC reproduction or DRD theorem.
- All policies use the same actual source and destination monitors and zero probes, so probe admissibility is vacuous; this experiment **does not validate network measurement feasibility beyond the model**. No packet simulation, no link weights, no alternate-route recovery, no composite repairs, no monitor-enabling repairs.
- E15 Python validator could not be executed because local runtime lacked mounted GitHub bytes and direct GitHub DNS failed. Equivalent original GraphML-to-cleaned-table content checks were executed via the GitHub connector. Python reproducibility scripts remain unexecuted.
- No CAIDA ITDK data, live outages or physical repair events were used. Real historical topology + **synthetic injected failure** is not a real outage experiment.
- The bootstrap intervals are descriptive under deterministic fault enumeration, not statistical inference to arbitrary networks or failures.
- An initial modular fault-sampling expression caused degenerate distributions; it was rejected and replaced before freezing the final CSV. This failed exploratory design is retained in this negative-results record.
- Originality and manuscript-source gates remain NO-GO/BLOCKED.
