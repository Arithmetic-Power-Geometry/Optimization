# E05 — Prior-art collision and negative findings
Date: 2026-10-20

## Primary comparison
Javdani et al. 2014, https://proceedings.mlr.press/v33/javdani14.pdf, Section 3: remaining version space contained in one decision region is sufficient to stop; the algorithm covers overlapping regions and therefore also partition special cases. The E05 branch family uses partition regions R_i and adds no new DRD principle.

Golovin, Krause and Ray 2010, https://proceedings.neurips.cc/paper/2010/hash/1e6e0a04d20f50967c64dac2d639a577-Abstract.html: equivalence-class active learning is the relevant earlier case.

Ma et al. 2015, https://www.sciencedirect.com/science/article/pii/S0166531615000516: path signature indistinguishability and monitor-placement conditions are established. The E05 failure-edge pairs have identical binary end-to-end path signatures.

## Candidate claims rejected
1. 'Decision-sufficient repair is more efficient than exact diagnosis' without qualification: already a classical DRD/ECD phenomenon.
2. 'n-1 probes identify a faulty group among n' as a new theorem: elementary linear search.
3. 'Exact edge diagnosis is impossible under restricted probes' as a new theorem: basic network-tomography identifiability.
4. 'A branch-level maintenance repair restores either edge' as a physical edge repair: false unless explicitly modeled as a composite maintenance action.

## Scientific value of the negative result
The explicit family is a correctness fixture for future exact-oracle tests and reveals how easily a supposed novelty result can arise from action granularity and monitor placement. The family establishes NO new original theorem and does not test repair-induced observability. E06 must address dynamic feasible measurements and distinguish physical intervention effects from generic POMDP dynamics.
