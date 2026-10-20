# E12 — Primary literature collision and provenance
Date 2026-10-20

1. Javdani, Chen, Karbasi, Krause, Bagnell & Srinivasa (2014), *Near Optimal Bayesian Active Learning for Decision Making*, AISTATS/PMLR 33:430–438, https://proceedings.mlr.press/v33/javdani14.html . Published overlapping decision-region sufficiency and HEC with approximation guarantees. E12 decision-sufficiency stopping is not new. The extended CMU technical report https://publications.ri.cmu.edu/near-optimal-bayesian-active-learning-for-decision-making is explicitly an extended version of the same work, not an independent second paper.
2. Existing E10 exact_oracle.py: memoized finite-horizon dynamic program over probe partitions and restoration actions, exact rational Bayesian success and robust feasibility. Candidate C is an exact restatement of this already-committed algorithm.
3. Existing E11 baselines.py: diagnosis-first, repair-first, random, unit-cost greedy and DRD-inspired pairwise region surrogate. Candidate B repeats already-committed rules, not published HEC.
4. E08 theorem originality decision: no original theorem survived E05–E07; E06 interleaving feasibility separation was false.

## Independent implementation provenance
E12 corrected E11 terminal-horizon success accounting: E11 previously returned when remaining<=0 without recording success after the final repair. New tests explicitly cover terminal repair success and partial success. This is a software bug fix, not a scientific discovery.

## Literature limits
PMLR primary publication and CMU author-hosted report checked for decision-region claims. No full exhaustive 64-work proof audit; no claim of global priority search or novelty.
