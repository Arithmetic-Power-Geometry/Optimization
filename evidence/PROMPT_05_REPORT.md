# Prompt 05 — adaptive submodularity, stochastic probing and information lower bounds
Date: 2026-10-20

## Evidence additions
E027-E033 (seven new records, 33 total). Publisher primary abstracts: E027-E029; preprint abstract E030; archival bibliographic metadata E031; article excerpt E032; publisher metadata/bibliography E033. Existing E002 (Golovin-Krause) and E019 (Krause-Guestrin) revisited. This is a targeted prior-art audit, not exhaustive full-text theorem verification.

## Major finding
Singla (2018), E029, studies paying to learn uncertain edge costs before constructing a spanning tree. This invalidates broad claims that paid sensing followed by network construction is new. Gupta-Nagarajan-Singla (2016/2017), E027-E028, prove adaptivity gap results for constrained stochastic probing. Asadpour-Nazerzadeh E030 gives bounded adaptivity gaps for a different stochastic submodular class. Adaptive submodularity E002 guarantees greedy policies only under its hypotheses.

## Negative results and counterexample
Krause-Guestrin E032 explicitly shows decision-theoretic value of information need not be submodular. Independent-bit XOR example: knowing one bit has no decision benefit, but knowing both completely resolves the target. This exhibits complementarity and invalidates an unrestricted diminishing-returns theorem.

## Lower-bound evidence
Wald E031 provides foundational sequential testing; no new sequential testing claim justified. Fano and Le Cam bounds were identified as relevant but not added as fully verified primary entries because this pass did not establish primary bibliographic records and exact applicable theorem statements. Do not treat a survey as an original theorem source.

## Surviving research question
Can we define a structural transformation validity relation with independently checkable certificates and derive a nontrivial matched lower/upper bound on total sensing, creation and verification cost that is NOT a corollary of existing stochastic probing or information-theoretic results? Need to define certificate semantics and proof system, adversarial sensing, exact baseline and computational model. This remains unproved.

## Adversarial restrictions
1. Policy-tree POMDP encoding can express finite sensing/creation policies; do not claim general expressive novelty.
2. Singla's priced probing already covers sensor cost plus network design.
3. Adaptivity gap may be bounded for important submodular families; no universal asymptotic gain.
4. Greedy information selection may fail with complementarity (XOR).
5. Certificates are not the same as Bayesian confidence; proof system and verifier must be explicit.

## Next prompt
Prompt 06: network augmentation, repair, bilevel and endogenous structural decisions. Investigate priced information network design and formal validity requirements before claiming novelty. No software or manuscript.
