# P02 decision-focused prior-art and originality gate (2026-10-21)

This matrix is a claim-collision audit, not a new-theorem certificate. The manuscript's 64-record registry contains provisional entries, not 64 independently verified publications. E040 is quarantined. The full 64-row status ledger is in reference_ledger.csv. Some P02 primary publisher records were checked; many registry-only items remain unverified.

| Candidate contribution | Closest verified prior art | Distinguishing assumptions still to prove | Decision |
|---|---|---|---|
| Stop testing once all remaining states share a successful action | Javdani et al., AISTATS/PMLR 33 (2014), overlapping decision regions and Hyperedge Cutting, https://proceedings.mlr.press/v33/javdani14.html | None for general set-inclusion stopping rule | **NO-GO as original theorem** |
| Sequential testing of decision regions under noise | Chen, Hassani, Krause, AISTATS/PMLR 54 (2017), https://proceedings.mlr.press/v54/chen17b.html; Golovin/Krause/Ray 2010 | Explicit physical probe admissibility and repair changes | **NO-GO for generic decision-region novelty** |
| Adaptive submodularity and greedy probing | Golovin & Krause, JAIR 42 (2011), DOI 10.1613/JAIR.3278 | Verify whether repair-changing feasible test sets preserve any adaptive-submodular guarantee | **CONDITIONAL research question; no guarantee** |
| End-to-end path measurements fail to identify all faults | Ma et al., Performance Evaluation 91 (2015), DOI 10.1016/j.peva.2015.06.003; Ma et al. IEEE/ACM ToN (2017) | Sharp bound for specified graph families and repair rights | **NO-GO for generic nonidentifiability** |
| Decision-dependent information discovery | Omer, Poss, Rougier, Open Journal of Mathematical Optimization 5 (2024), DOI 10.5802/ojmo.33 | Dynamic physical repairs and endogenous future probe feasibility; must compare also with multistage DDID and POMDP work | **CONDITIONAL model distinction only** |
| Network recovery under uncertain damages | Tootaghaj et al. 2017/2019 and Rysz et al. 2017 (original 12-entry bibliography; source-specific checks still required) | Matched information rights and exact repair/probe dynamics | **NO-GO for broad joint-recovery claim** |
| 1/n success for single failed edge on n-edge path with uninformative whole-path test and one repair | Elementary symmetry and indistinguishability | Natural nontrivial extension with sharp bounds | **NO-GO as nontrivial novel theorem** |
| Exhaustive finite-horizon minimax recursion | Classical belief-state dynamic programming / contingent planning | Scalable method or nontrivial complexity theorem | **NO-GO as new optimization algorithm** |
| Repair-induced path observability | Known decision-dependent information and sequential planning frameworks | New *specific* theorem or algorithm exploiting physically feasible post-repair paths, with counterexample and matched prior art | **CONDITIONAL only; P03 investigation** |

## Originality verdict
**NO-GO for a claim of a new theorem or optimization algorithm at P02.** A physically constrained network-repair application is a meaningful modeling focus but cannot alone establish a new algorithm. P03 may test a falsifiable candidate with independent proof and matched baselines. Do not infer that absence of an identical title implies novelty.

## Bibliography and version caveats
- Javdani et al. 2014 Carnegie Mellon technical report and AISTATS 2014 are versions of one contribution; CMU explicitly says cite the conference version.
- Chen et al. 2017 preprint and AISTATS version must not be counted as independent evidence.
- DOI/title, author, publisher, and full-text checking are not complete for the registry. Original P01 BibTeX included 52 provisional authorless records; merely compiling those entries does not verify them.
- Historical graph topologies with injected failures remain synthetic-failure experiments.

## Publisher records checked in this P02 pass
1. Javdani et al. (2014): https://proceedings.mlr.press/v33/javdani14.html
2. Omer, Poss & Rougier (2024): https://ojmo.centre-mersenne.org/articles/10.5802/ojmo.33/
3. Ma et al. (2015): https://www.sciencedirect.com/science/article/pii/S0166531615000516
4. Chen, Hassani & Krause (2017): https://proceedings.mlr.press/v54/chen17b.html (primary metadata already in earlier extension E02)
5. Golovin & Krause (2011): https://doi.org/10.1613/JAIR.3278 (original manuscript metadata, further publisher cross-check needed)

P02 remains **PARTIAL** because all 64 registry items were not independently publisher-verified or full-text inspected, and the revised manuscript sources cannot yet be uploaded as exact binaries through the connected interface.
