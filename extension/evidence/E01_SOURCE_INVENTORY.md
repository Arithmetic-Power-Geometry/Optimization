# E01 — Source freeze and immutable inventory
Date: 2026-10-20. Scope: inventory and preservation, not manuscript writing or empirical research.

## Audited baseline Git blobs (GitHub main)
| Source | Git blob SHA | Role |
|---|---|---|
| extension/README.md | 954ca1c621b5a244c15507c5760b03f14dac0cd1 | Extension contract |
| extension/PROGRESS.md (before E01) | ded247ccb536121439478ffcbf338c2145500810 | Initial extension state |
| evidence/FINAL_CLOSURE_PROMPT_20.md | 7aea3ec56887239849e374f4072ce4a067b94780 | Original 20-stage closure |
| evidence/novelty_matrix.md | c28d0e8dd372fb90927bc4e978523960359e5a63 | Novelty collision record |
| theory/PROOF_GATE_PROMPT_17.md | 0513a61ebf99fd142bf425bb9d8986e85743b251 | Strict proof gate |
| manuscript/REVISION_2026_10_20.md | 5f26a5d7847ffc0b1c98921d4b1a0179db17fb98 | Latest revision history |

GitHub recursive main-tree inspection (89 tree entries at inspection) found NO .tex, .pdf or .zip file in the repository, and no verbatim eight-page source manuscript. Only manuscript/REVISION_2026_10_20.md and manuscript/JAVDANI_2014_REFERENCE.bib exist under manuscript/. Therefore the required verbatim source freeze of the eight-page paper is **BLOCKED**. The revision history is not a replacement for the source. Previous conversation download paths are not GitHub file content and must not be silently reconstructed. E21 cannot begin before the exact LaTeX source is recovered and byte-hashed.

## Known bibliographic and scientific state
Original closure records 64 unique evidence IDs and 64 BibTeX keys, with E040 quarantined; these are not 64 independently verified distinct works. E016/E030/E043 metadata unresolved. Latest paper history reports 12 references; this is not proof of a 78-reference collection.
Original theorem-based publication status: NO-GO. The decision-sufficient stopping condition overlaps Javdani et al. (2014), Golovin et al. (2010), Chen et al. (2017). End-to-end probing overlaps Ma et al. (2015/2017); intervention and information discovery overlaps network recovery and DDID.

## Evidence-class register
- **Existing elementary deductions:** robust stopping if a surviving state set is contained in an action-valid region; two-edge and n-edge series-path indistinguishability under full-path-only observation and one irrevocable repair. Not independently novel.
- **Existing mathematical formulation:** finite robust planning under physical state transitions and matched budget. Semantic recursion, not an efficient novel algorithm.
- **Hypotheses only:** tight natural-family diagnosis/repair separation; repair-induced observability theorem; budget-sensitive nontrivial lower bound; efficient policy guarantee.
- **Software:** no executable research implementation found in inspected repository.
- **Experimental measurements:** none verified; no workflow-generated artifact, real outage or repair trace established.
- **Proposed work:** all E02–E22 tasks are not yet executed.

## Freeze requirements
Before E21, retrieve exact latest TeX, BibTeX, graphics and PDF as actual file bytes; store a verbatim immutable copy under extension/manuscript/original/ with SHA-256 and source provenance, and validate section headings against the PDF. Do not reconstruct from summary notes. No changes outside extension/ were made by E01.
