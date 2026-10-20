# Prompt 17 — independent adversarial research audit
Date: 2026-10-20

## Strict decision
**NO-GO: original-theorem proof gate failed.** No nontrivial original theorem, complexity separation, minimax bound, or approximation guarantee was established. Prior-art overlap is substantive, not merely terminological. Continue only for targeted falsification/reframing with explicit user authorization.

## Primary literature verified
- E064 Golovin, Krause, Ray (2010), NeurIPS 23, full publisher PDF inspected at problem definition, EC2 approximation theorem and decision-theoretic section. It already connects test acquisition to identifying the decision rather than the full hidden state; cost-sensitive noisy observations included.
- E065 Chen, S. Hamed Hassani, Krause (2017), AISTATS/PMLR 54:223–231, publisher proceedings paper inspected; addresses noisy correlated tests and target-variable/decision determination (ECED). Corrected authorship against publisher metadata after detecting an erroneous initial author list. There is also a longer Electronic Journal of Statistics 2017 publication; do not count the versions as independent evidence without publication-level deduplication.
- E059–E063: publication and proof-companion links independently established in preceding prompts, but full theorem-by-theorem checking of these papers remains incomplete. No claim of complete verification.

## Mathematical countermodels
T17.1: with exactly one of two series edges failed and only an s–t end-to-end probe, both states return DOWN; repeated observation-only probes cannot distinguish which single-edge repair is needed. Repair-before-probe policies may circumvent this; the model must freeze action ordering.
T17.2: overlapping regions {a,b} and {b,c} do not form a partition, since sharing a repair is not transitive.
T17.3: unequal repair costs yield a cost-sensitive terminal action, directly representable by finite-horizon belief-state optimization.
All are elementary, NOT new theorems. Complete reasoning is in theory/PROOF_GATE_PROMPT_17.md.

## Status of evidence and bibliography
Appended E065 with publisher-verified authors and proceedings metadata; BibTeX updated with a unique key. E040 remains quarantined. Earlier unresolved entries remain. This is a targeted literature audit, not a systematic review; proof audit for E059–E063 and forward citations remains incomplete.

## Prompt 18 purpose
Only if authorized: forensic negative-results audit, test whether any restricted path-topology model yields a *nontrivial* result, and evaluate alternate publishable outputs without falsely claiming theorem novelty. Do not draft software, experiments or manuscript.
