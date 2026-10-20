# Prompt 16 research report — 2026-10-20
## Verdict
**NO-GO for novelty based solely on action-sufficient repair.** One exact two-state minimax toy result, one three-state counterexample, and a finite decision-region predicate equivalence were derived (E16.1–E16.4). They are elementary and overlap established active learning/diagnosis frameworks. **No original theorem**.

## New primary evidence
E064: Golovin, Krause, Ray, *Near-Optimal Bayesian Active Learning with Noisy Observations*, NeurIPS 23 (2010), publisher proceedings abstract. EC2 addresses costly noisy tests, potentially correlated noise, and competitive Bayesian hypothesis identification; a major collision for action-targeted active diagnosis. The precise relation to overlapping repair-valid regions remains to be checked in full theorem text. Added unique registry ID and BibTeX key; no fabricated DOI.

## Formal results
- E16.1: series graph with exactly one of two edges failed, one-repair budget, edge inspection: exactly one test necessary/sufficient, cost c+1 excluding common fixed verification overhead.
- E16.2: third state differs by failure of irrelevant dangling edge: successful repair needs only action-region identification, not complete failure-state identification.
- E16.3: robust stopping iff posterior-support/version space lies within at least one repair-valid region R_tau. Regions can overlap and do not necessarily partition the state space.
- E16.4: full identification lower bounds can overestimate repair information requirements; singleton regions recover diagnosis.

## Adversarial limitations
- If both failed series edges can occur, one repair may be insufficient; states were restricted explicitly.
- If observations are noisy with full support, robust zero-error support does not shrink; bounded-error guarantees require separate risk semantics.
- If probes are not edge-level but restricted to end-to-end s–t path tests, the single-probe upper bound in E16.1 does NOT follow: the complete path fails in both states. The edge-level test is an explicit stronger oracle. A theorem for true end-to-end tomography must use feasible path routing, not silently substitute local inspections.
- If the repair budget permits both repairs, a universal action sequence eliminates sensing.
- Verification costs must be fixed or explicitly charged; signed incorrect readings do not prove physical truth.
- E064 proves no automatic novelty; its primary abstract was checked, not its complete theorem hypotheses.

## Literature verification honesty
E059–E063 technical reports and publication relationships remain grounded in primary metadata, but line-by-line theorem proof audit was not completed. The prompt's demand for independent full-theorem inspection remains an unmet gate, not a success. E040 remains quarantined; other metadata gaps remain. Total 63 registry records (62 provisional retained, 1 quarantined), 63 unique BibTeX keys, with multiple proof companions and non-independent versions.

## Next gate
Prompt 17 must investigate **overlapping action-valid decision regions and asymmetric repair costs with end-to-end-only path probes**, not local edge-inspection oracles; adversarially compare EC2/decision-region determination, stochastic probing, POMDP and tomography. A theorem requires explicit novel assumptions and full primary proof verification. No manuscript, experiments or software.
