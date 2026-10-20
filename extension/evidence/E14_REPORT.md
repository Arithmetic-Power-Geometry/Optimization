# E14 — Exact-small graph experiments execution report
Date 2026-10-20

## Gate resolved
The container already contained a byte-verified E09/E10 checkout. Reconstructed the three E11/E12 Python files from GitHub and independently computed their exact Git blob SHA-1 values, matching all three fetched GitHub SHAs. The eight Python files together match GitHub source. Executed Python 3.13.5 unittest discovery: **31 tests ran in 0.037 seconds; zero failures and zero errors**. The prior E13 blocked test-execution gate is RESOLVED locally. No code fixes were required in E14.

## Exact-small experiment
Implemented and executed `extension/experiments/e14_exact_small.py`, Python standard library only. Thirty instances, 180 policy evaluations; exact oracle cross-checked against exhaustive policy-mask enumeration in all 30 instances. Baselines were checked against exact oracle upper bound and budget limits. The committed script matched the locally executed script by Git blob SHA-1. Committed `extension/results/E14_RAW_COMPACT.csv` matched the local projected raw CSV by Git blob SHA-1. Raw outcomes are observed synthetic microbenchmarks, not inferred or invented.

## Results
Four nonrandom heuristics matched exact optimum in 30/30 small cases; random matched in 27/30. Random had three strictly negative gate outcomes, each 1/2 below optimum. No novel algorithm, theorem, or improvement was established. See E14_NEGATIVE_RESULTS.md for restrictions. Local full CSV SHA-256 551408ac530d4cacb86390321b84ef93d9e1697b12f4bccaaf62cc10426e7929. Projected committed CSV SHA-256 34ba51076ab248cd1f64ae1f06c42bf33ce19b81a9faf3d2f4332b9bf9bbaa54.

## Important restrictions
Local runner Python 3.13.5 (not E13's proposed 3.11/3.12 CI matrix). The E13 GitHub Actions YAML remains staged under extension/ci and inactive. E13 full paired-seed manifest was NOT executed; no public graph, no repair-dependent probe activation, no E05 composite repair, no noisy observations, no real network. Original manuscript exact eight-page TeX source still BLOCKED.

## Scientific decision
E14 COMPLETE for this restricted deterministic synthetic-small experiment; CONDITIONAL GO for E15 acquisition only after explicit user authorization. Original-theorem and new-algorithm originality remain NO-GO. STOP before E15.
