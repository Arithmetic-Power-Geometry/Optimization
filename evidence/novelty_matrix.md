# Prompt 09 novelty freeze — 2026-10-20

## Decision: NO-GO broad paradigm; CONDITIONAL GO restricted theorem-search programme
| Claim | Primary competing evidence | Verdict |
|---|---|---|
| Structural creation is absent from optimization | Dantzig-Wolfe, Benders, Jain, Rysz et al. | REJECT |
| Costly sensing followed by network construction is new | Singla E029; Omer-Poss-Rougier E050 | REJECT |
| Joint information discovery and routing is new | Paradiso et al. E023 | REJECT |
| Sensing and network repair cannot be cooptimized | Tootaghaj et al. E039 | REJECT |
| Decision-theoretic value of information is always submodular | Krause-Guestrin E019; XOR example | FALSE |
| Adding independent proof certificates is new | VIPR E042, planning certificates E052, proof complexity E044 | REJECT |
| Universal certificate size lower bound independent of proof language | Cook-Reckhow E044 | NOT JUSTIFIED |
| Joint sensing/edit/proof-generation/checking complexity separation in a fixed restricted model | E023,E029,E038,E039,E050,E052 | CONDITIONAL QUESTION ONLY; NOT A RESULT |

## Frozen question (hypothesis, not established novelty)
For a *specified* finite family of graph-edit transformations, hidden-state observation channel, costed sensing actions, fixed proof system and independent verifier, does an adaptive sensing-and-editing policy have a provable total-cost or proof-length separation from an explicitly matched nonadaptive policy that is not implied by existing stochastic probing, DDID, or planning certificate theorems?

### Required preconditions for any GO
1. Give a complete finite instance family and cost model, including proof generation and checking.
2. Distinguish certificate of encoded instance, universal uncertainty-set validity, and chance guarantee.
3. Prove a nontrivial bound and test for reduction to E029/E050/E052; trivial path certificates are insufficient.
4. State encoding length and proof-system dependence; quantify algorithmic resources.
5. Produce minimal counterexamples to all tempting universal claims.
6. If all claims reduce to known theorems, record NO-GO and pivot; do not force novelty.

## Bibliographic audit
55 unique registry IDs, including E040 QUARANTINED, so 54 retained for provisional citation. Bibliography still contains E040 as a quarantine-marked entry for traceability, not as an approved reference. E038 author list verified via Wiley; E039 venue and DOI via Penn State; E048 authors via Princeton; E009 PMLR metadata confirmed; E050 OJMO primary bibliographic export confirmed. E053 issue year 2026 versus online date 2025-11-19. Other entries have heterogeneous inspection levels, not all DOI/metadata or theorem statements have been independently verified. Do not label bibliography fully validated.

## Unresolved
E016 full authors; E040 title/DOI; E030 journal metadata; E043 full authors/claims; E053 publication-year style; all abstract-level entries need proof-specific inspection before theorem citation.
