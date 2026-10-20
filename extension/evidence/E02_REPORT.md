# E02 — Primary literature and work-level deduplication audit
Date: 2026-10-20

## Actions executed
- Retrieved and parsed `evidence/literature_registry.csv` from GitHub; enumerated every one of its 64 records (E001–E065 with E032 absent). Preserved original fields, inspection depth, URLs and status in a new 64-row extension ledger. No original record changed or deleted.
- Verified publisher/institutional bibliographic metadata and abstract-level novelty collisions for Javdani et al. 2014, Golovin et al. 2010, Chen et al. 2017, Ma et al. 2015/2017 and Omer et al. 2024.
- Recorded known journal/preprint/proof-companion clusters, quarantined E040, and flagged E016/E030/E043 metadata gaps. No global unique-work count claimed.
- Distinguished primary source evidence from technical companions and existing original-repository proof checks.

## Exact registry findings
64 distinct IDs; 63 status=retained; 1 status=quarantined (E040); 10 missing DOI fields (absence not evidence of invalidity). E032 intentionally absent. E061 supports E059; E063 supports E060; E062 supports earlier 2014 research pending canonical mapping. E064 and E065 have preprint/extended versions that are not separate contributions. The Javdani 2014 PMLR publication was not counted as a new registry ID because this extension does not mutate the original registry.

## Primary source checks
- https://proceedings.mlr.press/v33/javdani14.html (overlapping decision regions, HEC; PMLR 33:430–438).
- https://publications.ri.cmu.edu/near-optimal-bayesian-active-learning-for-decision-making (CMU technical version, explicitly says cite AISTATS).
- https://proceedings.neurips.cc/paper/2010/hash/1e6e0a04d20f50967c64dac2d639a577-Abstract.html (EC2).
- https://proceedings.mlr.press/v54/chen17b.html (ECED; PMLR 54:223–231).
- https://www.sciencedirect.com/science/article/pii/S0166531615000516 (Ma 2015; DOI 10.1016/j.peva.2015.06.003).
- https://pure.psu.edu/en/publications/network-capability-in-localizing-node-failures-via-end-to-end-pat/ (Ma 2017; DOI 10.1109/TNET.2016.2584544).
- https://ojmo.centre-mersenne.org/articles/OJMO_2024__5__A5_0/ (Omer et al. 2024 DDID).

## Stop/go
**E02 PARTIAL GO for E03 adversarial prior-art collision analysis.** All 64 registry entries were inventoried, but full-text primary-source verification of all 64 and exhaustive forward/backward citation mining remain OPEN. Existing NO-GO for new theorem paper remains. E03 not authorized until author approval. No software, simulations, manuscript or PDF were produced.
