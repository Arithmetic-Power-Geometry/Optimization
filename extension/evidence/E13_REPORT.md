# E13 — Deterministic CI and experimental protocol report
Date: 2026-10-20

## Completed
Read E13 exact prompt, preservation contract, E12 report and regression context. Attempted `git clone` of the repository from isolated execution container; failed because `github.com` could not resolve. Therefore E11/E12 accumulated tests were **NOT EXECUTED** and no failure logs exist beyond the clone failure. Wrote staged GitHub Actions workflow under extension/ci (matrix Python 3.11/3.12, compile, unittest, manifest validation), preregistered synthetic experiment manifest, stdlib manifest validator, and reproducibility/activation instructions.

## Technical constraint
GitHub Actions workflows must live at `.github/workflows/` to be discovered. The user requires all E13 artifacts strictly inside `extension/`, so the committed workflow is **NOT ACTIVE**. No CI run was triggered or observed. The staged YAML was parsed locally with PyYAML 6.0.3 after quoting the YAML `on` key; parsing does not prove GitHub Actions runtime success.

## Scientific gate
E13 PARTIAL GO for protocol design; NO-GO for claims of executed CI, passing E11/E12 tests, comparative performance, novel algorithm or original theorem. E14 exact-small experiments must not be reported as completed until accumulated tests execute successfully and experiment prerequisites are satisfied. The original manuscript byte snapshot remains BLOCKED. E14 requires explicit user authorization.
