# When Does Information Help Network Repair? Decision Sufficiency, Physical Path Probes, and the Limits of Diagnosis

**Mohammad Amir Khusru Akhtar**  
Usha Martin University, Ranchi, India  
ORCID: [0000-0002-3432-4199](https://orcid.org/0000-0002-3432-4199)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23533208.svg)](https://doi.org/10.5281/zenodo.23533208)

This repository provides the computational records, experimental implementations, historical topology inputs, and verification materials underlying the 2026 study. The paper is available as **Version V1** on [Zenodo](https://doi.org/10.5281/zenodo.23533208).

## Research question

When can observations support a feasible network repair without identifying every failed component? The study examines overlapping repair-validity regions, physically admissible path probes, limited repair budgets, and the difference between formal graph verification and physical restoration.

## Analytical results

A terminal repair is robustly sufficient when one admissible action succeeds in every physical state consistent with the observation history. Under the restricted model of an n-edge series path, one failed edge, only an uninformative full-path measurement, a uniform failure prior, and one irreversible edge restoration, the optimal success probability is exactly **1/n**. This bound is specific to those assumptions, not a general network-restoration guarantee.

## Completed computational results

| Study | Design | Reported result |
| --- | --- | --- |
| E14 | 30 deterministic finite-state toy instances; 180 policy records | Exact Bayesian-success oracle and four deterministic comparators: mean 0.3567; seeded random comparator: 0.3067, suboptimal on three instances |
| E15 | Historical topology acquisition and cleaning | Abilene: 11 vertices/14 edges; GEANT 2012: 40/61; ARPANET 1972: 29/32 |
| E16 | Six fixed-route orderings, 20 deterministic seed identifiers, budgets 1 and 2 | 720 matched synthetic-failure policy episodes; baseline restoration: Abilene 12/40, GEANT 2012 7/40, ARPANET 1972 6/40 |
| E17 | Eight fixed-route sensitivity scenarios | 960 synthetic-failure episodes; heterogeneous costs and correlated failures reduced observed restoration |

E16 baseline results are conditional on deterministic fault schedules. Under the uniform single-failure model, any fixed set of r distinct repaired route edges on a route of L edges has expected success **min(r,L)/L**. Differences among deterministic orderings do not establish general superiority.

E17 counts (Abilene / GEANT 2012 / ARPANET 1972): heterogeneous costs **8 / 5 / 4**, correlated failures **4 / 2 / 2**, shifted fault positions **33 / 32 / 33**. The shifted condition deliberately favors the first repaired edge.

## Reproduction workflow

1. Use the frozen inputs in `data/E15_raw/`, cleaned graph tables in `data/E15_clean/`, and provenance manifest `data/E15_TOPOLOGY_MANIFEST.json`.
2. Inspect the finite-state implementation in `src/` and execute the tests in `tests/` with the environment dependencies documented in `requirements.lock`.
3. Run `experiments/e14_exact_small.py`, `experiments/e16_matched.py`, and `experiments/e17_ablation.py` using the configuration and input assumptions documented in the corresponding validation files.
4. Compare outputs with the frozen records in `results/`, including E14 raw records, E16 matched episodes, E17 ablations, and the E20 outcome matrix.
5. Use the `validation/` documentation and `evidence/` claim–evidence ledger to distinguish completed checks from outstanding independent replication.

The paper's reported analysis corresponds to source commit [`c28305923695af8646446f3495d0fa89a0dccf75`](https://github.com/Arithmetic-Power-Geometry/Optimization/tree/c28305923695af8646446f3495d0fa89a0dccf75).

## Verification status and scope

An independent arithmetic audit examined 180 E14, 720 E16, and 960 E17 records and found no arithmetic discrepancies in the quantities checked. E16 bootstrap interval endpoints have not been independently regenerated. E15 validation and E16–E17 cross-language reproduction have not been independently confirmed in a clean checkout. A 10,000-resample multiplicity-adjusted analysis remains outstanding.

The E16 and E17 fixed-route policies **do not use informative adaptive probes**. The experimental label `drd-region-greedy` is a deterministic edge-ordering comparator, **not** the published hyperedge-cutting algorithm of Javdani et al. (2014). No packet-level, latency, convergence, real-outage, or field-reliability claim follows from these experiments. Mininet and ns-3 validation was not completed.

## Citation

Akhtar, M. A. K. (2026). *When Does Information Help Network Repair? Decision Sufficiency, Physical Path Probes, and the Limits of Diagnosis* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23533208

Citation metadata is provided in [CITATION.cff](CITATION.cff) and [CITATION.bib](CITATION.bib).

## Rights

Copyright © 2026 Mohammad Amir Khusru Akhtar. Original repository code and documentation are distributed under the Apache License, Version 2.0; see [LICENSE](LICENSE). Historical topology inputs and third-party material retain their respective source terms and attribution, as recorded in the provenance documentation. The separately published manuscript is not relicensed by this repository license.
