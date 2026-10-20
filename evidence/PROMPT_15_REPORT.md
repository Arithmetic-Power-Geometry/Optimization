# Prompt 15 report — adversarial falsification and publication audit
Date: 2026-10-20. Decision: **NO-GO for Q14 as a broad novel formulation; conditional GO only for a further restricted theorem-search, not a manuscript.**

## Evidence and corrections
- E059: Publisher article *On optimal monitor placement for localizing node failures via network tomography*, Performance Evaluation 91:16–37 (2015), DOI 10.1016/j.peva.2015.06.003. Abstract explicitly states minimum monitor placement and CAP/CSP/UP identifiability results. Full individual proof verification **not completed**.
- E060: 2015 preprint arXiv:1509.06333 corresponds to published *IEEE/ACM Transactions on Networking* 25(1):434–450 (2017), DOI 10.1109/TNET.2016.2584544. Corrected registry and BibTeX in place; preprint is NOT a separate study.
- E061 arXiv:2012.09381 explicitly states it supplies all proofs for E059; E062 arXiv:2012.09964 explicitly states it supplies all proofs for 2014 precursor. They are technical companions, not separate independent results.
- NEW E063 arXiv:2012.09959 *Failure Localization Capability: Theorem Proof and Evaluation*, technical companion to E060 journal work. Added registry and BibTeX; not an independent study.
- E040 stays quarantined. Unresolved earlier metadata E016,E030,E043 remain.
- Primary publisher/author metadata and selected abstracts inspected. **Not achieved:** exhaustive full-text proof-by-proof verification, comprehensive forward citation audit, and direct cryptographic-attestation literature comparison. These limitations are research blockers, not silently completed tasks.

## Six adversarial tests
See theory/ADVERSARIAL_TESTS_PROMPT_15.md for explicit assumptions and countermodels:
1. Universal replacement edge makes zero sensing optimal.
2. Repair can succeed without identifying which hidden failure occurred.
3. Valid sensor signature can authenticate an incorrect physical reading.
4. Public fixed signature checking cost collapses to ordinary priced POMDP sensing.
5. Matched nonadaptive policies must retain observation-dependent terminal repair.
6. Sets sharing a feasible repair are not automatically an equivalence partition.

## Theorem status and competing prior art
E059–E063 occupy substantial failure identifiability and monitor-placement theory; E057 probabilistic diagnosis; E039/E058 progressive recovery; E050 DDID; E029 priced information; E052/E056 verified planning. None of C15.1–C15.6 is claimed new. No proof of a new minimax bound or policy separation. Any bound must separate *action sufficiency* from *state identification* and not merely reprice authenticated observations.

## Falsifiable narrow candidate for Prompt 16
Fix a sparse graph family, fixed permitted edits **without a universal repair**, authenticated path tests with an explicit sensor-fault model, and at least two hidden failure states requiring incompatible edits. Ask whether optimal robust repair cost admits a tight combinatorial characterization strictly weaker than unique fault identification and not reducible to known active diagnosis / POMDP policy optimization. Test a minimal graph family first. **Unproved, novelty unverified**.

## Research integrity
Evidence records: 62 total, 61 provisional retained, one quarantined; 62 unique BibTeX keys including quarantined E040. One new E063 proof companion added; one E060 journal correction. This does NOT equal 62 independent primary studies. No software, numerical experiments or manuscript.
