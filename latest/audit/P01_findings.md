# P01 findings — 2026-10-21

**Result: PARTIAL PASS (local), GitHub source archive BLOCKED; manuscript NO-GO.**

The user-attached 12-page PDF SHA256 is `8bd9ec57ad5efd50f32168581b685bc2e6bb079d5afe1b2ded66dda3f28acc4b`. Original LaTeX ZIP SHA256 is `aa8a9e88193ee1380fd00ce6bbcb60dd5a64f4af88aae8304d7748aee2d6b61d`. Original ZIP PDF SHA256 is `c61775ec1e523160b01fa958fcfbf7841e13d94012f307558a09c5412eca8f94`; it is NOT byte-identical to standalone attached PDF. Both are preserved in the downloadable local archive. ZIP path-safety check passed.

Local revised source main.tex SHA256 `de244de9d09234d66b7b1af9632080b50ff6eea3b74f158fb30dc94b37d85670`; references.bib SHA256 `4c568ed76ddefad4bc11f90ccf5a4e3ad85ab0e9b837cbc296f4ffe690aa705e`. Revised 12-page PDF SHA256 `703744fb952933582cf7e6b069904b4caa43cf04999c15fccf14dec49873b478`.

## Changes and evidence
- Page 2, Figure 1: corrected TikZ node spacing and optional interleaving arrow, visually inspected.
- Page 4, Table 2: adjusted column widths and shortened dangling-edge inspection row.
- Page 5, Equation (3): inspected already mathematically correct aligned sum; no new result claimed.
- Page 6, Equation (5): changed aligned math layout to a single numbered equation with clear minimum branches, preserving its robust worst-case semantics; visually inspected.
- Page 6, Figure 4: inspected existing overlapping-region ellipses; kept mathematically correct figure.
- Page 1: fixed ambiguous abstract pronoun.
- Pages 3 and 10–12: malformed author-year entries caused by provisional evidence-registry metadata remain UNRESOLVED; P02 must validate original publisher/author metadata, not fabricate it.
- Pages 8–9: preserved synthetic-failure findings and negative controls without overstating superiority.

## Build
Local commands: `pdflatex -interaction=nonstopmode -halt-on-error main.tex`; `/usr/bin/bibtex.original main`; three final pdflatex passes. The `bibtex` command symlink is broken but the real executable works. Final PDF: 12 pages; no undefined citation/reference warnings. Remaining harmless `Underfull \hbox (badness 1137)` around line 248. All pages visually checked in a 12-page contact sheet, with detailed views of pages 2 and 6. Independent clean-checkout reproduction remains OPEN.

## Scientific boundary
Robust stopping criterion is inherited decision-region theory. The 1/n bound is elementary under uniform prior and restricted sensing. Exact finite-horizon recursion is an exhaustive specification, not a new scalable algorithm. No additional experiments or theorem novelty established.

## Blockers
The GitHub connector's text-file operations do not transfer attached binary PDF/ZIP files or directly access the local revised TeX. The originals, complete revised TeX, bibliography, source patch and compiled PDF are therefore available in the local downloadable P01 archive, **not uploaded as GitHub binaries or complete source**. Do not mark GitHub source freeze or manuscript submission complete. This audit is committed under latest/; P02 NOT EXECUTED.
