# Step 2 — corrected source metadata and deduplication gate (2026-10-21)

This is a verified **subset**, not a completed 64-reference audit. Original 64 registry records remain preserved.

## Corrected errors
- **E059** is Ma et al. (2015), *On optimal monitor placement for localizing node failures via network tomography*, Performance Evaluation 91:16–37, DOI 10.1016/j.peva.2015.06.003. Previous ledger incorrectly assigned the `Javdani2014` BibTeX key and Javdani authors to this record.
- **E060** is Ma et al. (2017), *Network Capability in Localizing Node Failures via End-to-End Path Measurements*, IEEE/ACM Transactions on Networking 25(1):434–450, DOI 10.1109/TNET.2016.2584544. Previous ledger incorrectly assigned `Ma2015` key to this distinct 2017 paper.
- **E063** is a 2020 technical-report companion containing proofs and evaluations for Ma et al. (2017), arXiv:2012.09959. Count as version-linked supporting material, not a new independent journal paper.
- **E040** is a genuine CAV 2019 publication, DOI 10.1007/978-3-030-25543-5_18. Its earlier quarantine should be lifted *as a publication-existence matter*; whether it belongs in the final manuscript depends on claim-specific relevance. E040 is already one of the 64 rows in the current GitHub ledger; do not claim it is absent from that ledger.
- **E017** is Smallwood and Sondik (1973), *The Optimal Control of Partially Observable Markov Processes over a Finite Horizon*, Operations Research 21(5):1071–1088, DOI 10.1287/opre.21.5.1071.
- **E009** is Astorga et al. (2025), PMLR 267:1864–1886. Valid publication but peripheral to repair-specific theory.
- Separate extra manuscript citation: Javdani et al. (2014), PMLR 33:430–438. It is NOT E059.
- **E065** Chen, Hassani and Krause (2017), PMLR 54:223–231; distinct from Javdani 2014.

## Scientific effect
The mistaken E059/E060 author/key mapping could corrupt both attribution and novelty analysis. Both Ma papers explicitly distinguish feasible network path measurement regimes, so they must be considered before claiming a novel physical-path observation model. The Smallwood–Sondik finite-horizon POMDP theory further limits claims of originality for belief-state dynamic programming.

## Next gate
Primary-check all remaining registry records, inspect E061/E062 as potential companion reports, reconcile the original source BibTeX and the registry at the work level, then produce a complete and relevant attributed bibliography. No artificial citation-count inflation; no final 64-citation PDF yet.

Sources: https://www.sciencedirect.com/science/article/pii/S0166531615000516 ; https://pure.psu.edu/en/publications/network-capability-in-localizing-node-failures-via-end-to-end-pat/ ; https://arxiv.org/abs/2012.09959 ; https://pubsonline.informs.org/doi/10.1287/opre.21.5.1071 ; https://link.springer.com/chapter/10.1007/978-3-030-25543-5_18 ; https://proceedings.mlr.press/v33/javdani14.html ; https://proceedings.mlr.press/v54/chen17b.html .

**STATUS: PARTIAL.**
