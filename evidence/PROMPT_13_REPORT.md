# Prompt 13 — Attested physical network repair: primary literature and falsification gate
Date: 2026-10-20. This is the first stage of a **new eight-prompt exploratory programme (13–20)**, not a reversal of Prompt 12's NO-GO.

## Research question
Under an explicit physical-failure model, trusted measurement semantics and a fixed certificate verifier, can sensing/attestation/repair costs yield a new **tight minimax or complexity result** not implied by ordinary fault diagnosis, network tomography, stochastic recovery, DDID or hypothesis testing?

## Primary literature newly checked
- **E057** Qi, Li, Wang, Liu (2021), *Probabilistic probe selection algorithm for fault diagnosis in communication networks*, Computer Networks 198, 108365, DOI 10.1016/j.comnet.2021.108365. Publisher abstract: probabilistic probe selection for fault localization in noisy/nondeterministic environments. Inspection: abstract and bibliographic metadata, not full proof.
- **E058** Tootaghaj, Bartolini, Khamfroush, La Porta (2019), *On Progressive Network Recovery from Massive Failures under Uncertainty*, IEEE TNSM 16(1), 113–126, DOI 10.1109/TNSM.2018.2880155. Institutional bibliography/abstract: progressive repair with uncertain damage; a strong direct collision beyond 2017 E039.
- **E059** Ma, He, Swami, Towsley, Leung (2015), *On optimal monitor placement for localizing node failures via network tomography*, Performance Evaluation 91, 16–37, DOI 10.1016/j.peva.2015.06.003. Publisher abstract: monitor-placement identifiability from path status observations; strong collision for any novel sensor placement/diagnostic identifiability claim.

All three appended as E057–E059 with matching BibTeX keys. Source-level verification does **not** constitute full-text theorem verification.

## Contradiction matrix
| Tempting claim | Direct evidence | Verdict |
|---|---|---|
| Probabilistic fault probing is new | E057 | Rejected |
| Progressive repair with unknown damage is new | E039,E058 | Rejected |
| Network failure identifiability via monitor placement is new | E059 | Rejected |
| Joint sensing, graph modification and certification is a novel paradigm | E023,E029,E050,E052 and Prompt 11 | Rejected |
| Trusted physical attestation creates a new minimax bound | No theorem or separation shown | Unproved |
| Proof checking can establish physical truth without authenticated measurements | P10.2, A11.3 | False |

## Minimal adversarial tests to be performed before novelty claim
1. **Universal repair:** if a single edit works for all hidden states, sensing may be unnecessary.
2. **Indistinguishable states:** if two physical states produce identical authenticated observation laws and require disjoint repairs, robust zero-error repair is impossible.
3. **Attestation equivalence:** if authenticated observations can be represented as ordinary noisy channels with additional costs, a purported new model may collapse to POMDP/DDID.
4. **Verifier collapse:** if the certificate only verifies a declared graph, it adds no physical correctness beyond the trusted measurement model.
5. **Existing identifiability:** compare any bound with monitor-placement E059 and stochastic fault diagnosis E057 before claiming novelty.

## Formal next-stage candidate (not a theorem)
Let G(theta) be a finite physical graph, Theta a specified failure family, S a set of authenticated tests with rational observation kernels and explicit cost, T finite repair edits, and V a fixed checker. Require the *physical* target predicate to hold for every theta consistent with a transcript (robust), or with declared failure probability delta (chance). Compare policies with and without trusted attestation under matched resources and cost. Seek a sharp minimax bound or impossibility frontier that survives reduction to E057–E059, E029/E050 and classical hypothesis testing. **No novel result is asserted.**

## Bibliographic and methodological limitations
E040 remains quarantined. E016/E030/E043 and other early metadata gaps remain. This is targeted deepening of a pivot, not a completed systematic review; only three new sources checked at abstract/bibliographic level. Full-text theorem checks, recent forward citations, and additional foundational tomography/active diagnosis papers are required at Prompt 14. Existing 12-prompt negative gate remains in force.

## Outcome
**CONDITIONAL GO for defining a sharply restricted problem at Prompt 14; NO-GO for manuscript drafting or novelty claims.** No software, experiments or manuscript produced. STOP and request permission for Prompt 14.
