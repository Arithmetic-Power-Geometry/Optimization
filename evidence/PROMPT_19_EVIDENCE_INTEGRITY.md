# Prompt 19 — Independent evidence-integrity and negative-results audit
Date: 2026-10-20. Status: **NO-GO** for novel-theorem claims or manuscript submission.

## Coverage and methodology
Read committed Prompt 19, Prompt 18 report, Prompt 17 proof-gate, Prompt 16 model, original Prompt 12 final audit, registry, BibTeX, novelty matrix and progress. Rechecked E064 and E065 against original publisher proceedings and PDF (NeurIPS 2010 and PMLR 2017). Examined available citation metadata for E059–E063 as recorded in previous stages. This is a targeted forensic audit, **not** a complete independent source-by-source verification of all 64 records or line-by-line reproduction of all proofs.

## Primary-source cross-check
- E064 Golovin, Krause, Ray (2010), *Near-Optimal Bayesian Active Learning with Noisy Observations*, NeurIPS 23. Original publisher abstract confirms nonuniform test costs, correlated noise, EC2 and approximation guarantees. Publisher PDF includes equivalence-class and minimum-risk decision formulation. BibTeX inspection note was stale (said abstract only) and is corrected to selected full-text inspection, NOT complete proof reproduction.
- E065 Chen, Hassani, Krause (2017), *Near-optimal Bayesian Active Learning with Correlated and Noisy Tests*, PMLR 54:223–231. Publisher lists three authors, 2017, title and ECED. Extended *Electronic Journal of Statistics* version DOI 10.1214/17-EJS1336SI already linked, not separately counted. PMLR paper and its journal version should not be treated as two independent discoveries.
- E060 2015 arXiv preprint / 2017 IEEE/ACM Transactions on Networking article: one research work. E063 its proof companion; E059 and E061 are journal/proof companion; E062 is proof companion to earlier 2014 work. These relationships were documented previously, but independent full-proof auditing E059–E063 is incomplete.
- E040 remains quarantined due to unresolved DOI/title/author association. E016/E030/E043 metadata gaps remain; not silently corrected.
- New distinct sources this stage: **zero**. Do not inflate evidence counts.

## Counterexample audit: explicit premises
1. C15.1 universal repair requires permitted reliable new bypass; otherwise no zero-sensing conclusion.
2. E16.1/E16.2 local edge inspection is stronger than restricted end-to-end path observation. Their upper bounds do not transfer to path-only probes.
3. T17.1 applies to observation-only policy before any repair. F18.1 strengthens the result when an initial irreversible repair exhausts a one-repair budget. With two repairs a universal repair exists.
4. Repair success is physical s–t connectivity; a certificate of a declared graph or signed but false sensor report cannot substitute for it.
5. Overlapping valid-action regions can fail transitivity but remain finite decision-region / cost-sensitive planning instances.
6. Asymmetric repair costs and attestation overhead alone do not establish a new minimax lower bound or complexity separation.
7. Chance guarantees require an explicit prior/kernel; robust zero-error guarantees require quantification over all consistent states and allowable sensor faults.

## Claim-to-evidence verdict
| Claim | Grounding | Verdict |
|---|---|---|
| Fault tomography identifiability is novel | E059–E063 | REJECTED |
| Probabilistic probing or uncertain recovery is novel | E057–E058, E039 | REJECTED |
| Decision-sufficient sensing is new | E064–E065 | REJECTED as broad claim |
| Overlapping repair regions force a new theory | T17.2, finite POMDP baseline | NOT ESTABLISHED |
| Authenticated readings establish physical truth | C15.3 | FALSE absent sensor-trust assumptions |
| Original theorem / complexity separation | No complete proof | NO-GO |
| Original application-specific graph-family result | No proved separation | UNPROVED; NO-GO for submission |

## Possible future outputs, NOT authorized for drafting
(A) Critical perspective: must demonstrate distinct synthesis and editorial fit; not automatically a novel theory contribution.
(B) Structured/systematic review: needs reproducible search strategy, deduplication by research work, screening, inclusion/exclusion, source-by-source extraction, and citation metadata cleanup.
(C) Methods/benchmark paper: requires a sharply distinct practical question, legitimate implementation, baselines, datasets and independent reproducibility checks, with user authorization.
(D) Original theorem paper: **NO-GO** unless a genuinely new, nontrivial, completely proved result survives primary prior art.

## Final blockers for Prompt 20
No original theorem; incomplete full-proof audit E059–E063; incomplete bibliography and systematic forward-citation audit; E040 quarantined and E016/E030/E043 gaps; no physical attestation oracle or feasible path-probe family yielding a nontrivial novel bound. Preserve negative result and close without manuscript. No software, experiments or manuscript.
