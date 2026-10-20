# FINAL RESEARCH AUDIT — Optimization Programme, Prompts 01–12
Date: 2026-10-20
Decision: **NO-GO for an original-theorem claim, journal submission, or manuscript drafting on the present formulation.** The research evidence supports narrower exploratory pivots, not publication readiness.

## 1. What was actually accomplished
- Twelve sequential research stages covering classical structural optimization, canine/robotic sensing, POMDPs and decision-dependent information, adaptive submodularity, stochastic probing, network augmentation/repair, proof certificates, recent competing literature, bibliographic checks, formal modeling and adversarial theorem tests.
- Cumulative registry: **55 unique IDs**, E001–E056 with E032 intentionally not assigned (a duplicate candidate removed during Prompt 05); **54 provisional retained, 1 quarantined (E040)**.
- Cumulative BibTeX: **55 distinct keys**, including a quarantine-marked traceability entry; not 55 fully verified, citeable publications.
- Formal model: theory/FORMAL_MODEL_PROMPT_10.md. Adversarial gate: theory/ADVERSARIAL_GATE_PROMPT_11.md.
- Four elementary baseline propositions P10.1–P10.4, four elementary adversarial constructions A11.1–A11.4, six counterexamples CEX-A–F. **No independently novel theorem proved.**
- No software, numerical experiments, empirical datasets, or manuscript produced.

## 2. Primary-source check performed at final gate
- E050 Omer, Poss, Rougier (2024), OJMO 5 article 5, DOI 10.5802/ojmo.33: publisher full abstract confirms robust two-stage decision-dependent information discovery, compact MILP *if* number of uncertainty-polytope constraints other than variable bounds is constant, and spanning-tree applications. It does not imply compactness for arbitrary POMDPs.
- E052 Dold et al. (2025), ICAPS 35(1):54–63, DOI 10.1609/icaps.v35i1.36101: primary proceedings and PDF confirm independent optimal planning lower-bound certificates and proof-logging A* with reported modest overhead; authors and metadata checked.
- E056 Traytel, Archive of Formal Proofs, **June 13, 2026**: primary archive confirms mechanized soundness of Dold et al.'s certificate format and A* case study. The archive itself notes AI-assisted formalization; independent checking of the Isabelle proofs was NOT performed here.
- Other key overlaps retained from earlier audits: E023 sensing-aware routing, E029 priced information before combinatorial construction, E038 stochastic structural repair, E039 repair interleaved with information gathering, E041–E044 SAT/MIP/PB certificates and proof complexity. These were not all reread in full at this final stage.

## 3. Strongest contradictory evidence
| Broad claim | Contrary literature | Status |
|---|---|---|
| New to choose information before building combinatorial structures | E029, E050 | Rejected |
| New to combine sensors and routing | E023 | Rejected |
| New to change graph structure under uncertain damage | E038 | Rejected |
| New to learn while repairing a network | E039 | Rejected |
| New to independently verify optimization/planning | E041–E044, E052, E056 | Rejected |
| Adaptive sensing always enjoys diminishing returns | E019, XOR counterexample | False generally |
| A valid witness for encoded graph proves physical hidden state | P10.2/A11.3 | False without attestation/robust semantics |
| A certificate automatically creates an original adaptivity gap | P10.4/A11.2 | False |

## 4. Mathematical audit and assumptions
- P10.1: OPT_adaptive <= OPT_nonadaptive only if the nonadaptive policies are a subset of admissible adaptive policies under the *same* resources, stopping rules and validity criterion.
- P10.2: an accepted witness is sound for its *encoded* predicate, not necessarily a hidden physical state; no blanket claim that certificate systems are unsound.
- P10.3: binary search versus N−1 fixed thresholds is a **classical** adaptivity advantage, conditional on deterministic threshold-only sensors, exact identification and authenticated transcripts; not a new graph-optimization theorem.
- P10.4: terminal edit and certificate costs cancel only when identical across compared policies; a constant per-witness cost alone does not suffice if witness counts differ.
- A11.1: finite history-based reduction to a partially observed decision process preserves expected cost and validity under specified finite-state/computable-cost assumptions. It does **not** yield a polynomial-sized encoding.
- A11.2: a two-sensor proof-cost reversal exists under explicitly different attestation expenses, but is ordinary cost reweighting; artificial sensor-label pricing does not show inherent certificate complexity.
- A11.3: observationally indistinguishable states with disjoint valid edits preclude zero-error robust solutions absent additional trusted observations.
- A11.4: a universal valid repair and robust witness permit zero sensing; no unconditional positive sensing lower bound.
- H10.1: no novel combined-cost separation shown. H10.2: trivial existential true, novelty no-go. H10.3: no new information lower bound shown.

## 5. Bibliography and evidence-integrity ledger
- Registry IDs unique; BibTeX keys unique; E032 was an aborted duplicate and must not be counted as a source.
- E040 is **QUARANTINED**: DOI/title/author association unresolved; its BibTeX entry remains solely for traceability and must be excluded from a submitted bibliography.
- E016 complete author metadata remains incomplete; E030 journal metadata, E043 detailed claims and some early entries require publisher-level review; many entries have abstract-level inspection only.
- E053 online date (2025) differs from issue year (2026); choose and document a consistent citation convention.
- E056 publication date confirmed from the primary Archive of Formal Proofs as 2026-06-13; source notes AI-assisted formalization, not evidence of unsoundness.
- **Do not describe 54 provisional retained items as 54 fully verified primary papers.** No exhaustive systematic search, forward-citation graph, DOI-resolution audit, or independent proof checking was completed.
- No new records added at Prompt 12: primary source check strengthened E050/E052/E056, rather than padding the count.

## 6. Reproducibility and submission-readiness checklist
| Requirement | State |
|---|---|
| Prompt-by-prompt committed research trail | Present |
| Stable source IDs and cumulative bibliography | Present, with metadata gaps |
| Explicit adversarial novelty matrix | Present |
| Formal state/action/certificate model | Present, finite and exploratory |
| Baseline propositions and counterexamples | Present, elementary |
| Novel, non-reducible theorem with full proof | **Absent** |
| Independently validated lower and upper bounds | **Absent** |
| Experimental implementation and results | **Not undertaken by instruction** |
| Systematic literature review and complete DOI checks | **Absent** |
| Independently checked proof artifacts | **Absent** |
| Manuscript submission readiness | **NO** |

## 7. Three falsifiable alternative research pivots — none claimed novel
### Pivot A — Certificate-sensitive sensing under a natural proof language
Fix a concrete network failure family, rational sensor channel, and an established checker such as a specified pseudo-Boolean proof format. **Question:** Is there a family where charging actual certificate generation/verification operations changes the optimal sensing policy by an asymptotically nonconstant factor compared with an otherwise identical model using a constant certificate overhead? Falsify by reducing proof costs to state/action cost or proving a uniform polynomial/constant overhead. Need independent prior-art search on proof-aware active planning and realistic uniform proof-generation costs. Avoid artificial sensor labels.

### Pivot B — Attested versus unattested physical graph repair
Fix two hidden graph-state classes, explicit trusted attestation semantics, and a restricted edge/vertex repair family. **Question:** Under a specified risk criterion and nonzero costs, can one establish a *tight* minimax sensing/attestation/repair lower bound not implied by ordinary binary hypothesis testing or stochastic probing? Falsify by Le Cam/Fano-style reduction, a universal valid repair, or an information-equivalent policy. Distinguish true physical correctness from acceptance of an encoded graph witness.

### Pivot C — Succinctness of proof-producing adaptive graph policies
Fix an explicit representation for policy DAGs, graph edits and proof logs. **Question:** Does a natural graph family admit a polynomial-size proof-producing adaptive policy but require superpolynomial size in a **specified** nonadaptive policy representation, after controlling for known binary-search gaps and the choice of proof system? Falsify by polynomial compilation into DDID MILP/POMDP policy representation or by a short nonadaptive certificate. Encoding and proof-language dependence must be explicit.

**Research recommendation:** Pivot A is closest to the original motivation but may collapse to ordinary cost-aware planning; Pivot B is conceptually cleanest for separating physical truth from mathematical verification; Pivot C is most mathematically demanding. None is approved as novel without new primary prior-art verification and a theorem.

## 8. Final decision and stop rule
**NO-GO** for drafting or submitting a paper on the existing hypothesis. The twelve-prompt programme is completed as a *negative/diagnostic research audit*, not a successful proof of a new theory. Further work requires a newly authorized programme with one pivot, explicit counterexample gates, and no predetermined originality conclusion. STOP.
