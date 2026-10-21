# Full 64-record bibliography reconciliation — 2026-10-21

## Output and decision
- All **64/64** original registry records retained and audited in `latest/audit/STEP2_64_RECORD_STATUS.csv`.
- **16** records received new author/venue/source checks in this expanded pass; **48** did not receive new primary checks. Earlier verified metadata are separate, not counted as new checks.
- Original 12-entry manuscript bibliography corrected and expanded to **27 complete attributable BibTeX entries**, of which **21 are actually cited** in a locally compiled 12-page A4 editorial paper. Unused or peripheral entries are not added as false citations.
- Separate four-page 64-item provenance inventory PDF and local full package prepared. Manuscript PDF SHA256: `366d6c61468b06ad83487ba945cfd6669121286293ff6395a69f6b98852486cb`.
- Final local LaTeX compilation: pdflatex, bibtex.original, pdflatex twice; 0 undefined citations, 0 undefined references, 0 final warnings.
- GitHub cannot ingest the local PDF and TeX bytes via the available text-only connector; **only the audit CSV and this report are remotely committed**. Source archive and revised manuscript are in the local downloadable package.

## Important corrections
- E029 Singla 2018 DOI `10.1137/1.9781611975031.161` (original manuscript had erroneous .164).
- E040 Giannarakis et al. 2019 is published CAV paper, not fabricated/quarantined.
- E059 Ma et al. 2015 and E060 Ma et al. 2017 are distinct papers; old ledger wrongly mapped E059 to Javdani 2014 and E060 to Ma 2015.
- E061, E062, E063 are technical-report companions, not three additional independent journal articles.
- E030 2009 arXiv preprint conflicts with 2016 registry year; exact published version remains unresolved.
- E045 publisher spelling **Kazemian**, not Kazemanian.
- A large portion of the original registry concerns sensing in unrelated domains, mathematical optimization background or proof systems. These are retained in the audit rather than cited as direct evidence of network-repair algorithm superiority.

## Submission decision
**NO-GO.** A 64-row bibliography registry is not equivalent to 64 publisher-verified independent relevant works. The current paper has 21 properly attributed in-text citations; comprehensive primary checking and work-level deduplication remain open, as do fair published algorithm comparisons and real network validation. No journal submission made.
