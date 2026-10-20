# Prompt 04 research report — 2026-10-20

## Scope
Primary research on POMDPs, Bayesian value-of-information, knowledge-gradient sampling, decision-dependent information discovery, stochastic network sensing, and endogenous uncertainty. E017-E026 added (10 records; 26 cumulative). Publisher/institutional abstracts and bibliographic metadata checked; E025 literature section inspected. No exhaustive full-text proof audit or computational experiments.

## Key primary findings
- E017 Smallwood-Sondik: finite-horizon POMDP value functions and belief-state policy optimization.
- E018 Kaelbling et al.: offline POMDP solution methods and finite-memory policies.
- E019 Krause-Guestrin: optimal observation plans, and hardness results for decision-theoretic information value.
- E020 Frazier et al.: sequential knowledge-gradient information collection, with special-case optimality and suboptimality bounds.
- E021 Jonsbraten et al.: decision-dependent random elements and information discovery.
- E022 Goel-Grossmann: decisions control when uncertainty is revealed.
- E023 Paradiso et al.: exact and approximate schemes for decision-dependent information discovery, including *joint sensor placement and routing* (critical direct contradiction).
- E024 Vayanos et al.: dynamic multistage robust information discovery via exploratory investments.
- E025 Pantuso-Hewitt: exact L-shaped decomposition for discrete decision-dependent distributions.
- E026 Zhou-List: sensor location optimized for network demand estimation.

## Strong negative novelty evidence
The proposed framework's broad features—partial observations, cost-aware sensing, adaptive decisions, endogenous information revelation, and joint sensing/network decisions—are covered by existing work. Finite-horizon sensory-creation policies can be encoded as POMDP/stochastic policy trees with actions for sensing, model transformation, and checking. This is a *representation observation*, not a complexity equivalence for all encodings.

## Surviving falsifiable hypothesis
A formally specified class of information-limited structural transformations may admit a new trade-off between (a) sensing/sample complexity, (b) transformation/repair cost, and (c) independently checkable proof cost. To count as new, the proposed theorem must exceed known POMDP and information-complexity results under explicit computational restrictions. Distinguish posterior confidence from proof-validity certificates. Seek counterexamples before proving guarantees.

## Open adversarial questions
1. Can a known POMDP/robust program reproduce the entire claimed mechanism with polynomial-size encoding?
2. Do sensing and creation decisions satisfy any adaptive-submodular condition, or do complementarities destroy it?
3. Is certificate checking deterministic conditional on true state, or is the claim merely a chance constraint?
4. Can E023's cooptimized sensing/routing directly instantiate our proposed application?
5. Are the desired lower bounds immediate corollaries of Fano/Le Cam or standard proof complexity?

## Bibliography QA
E023 online 2024 versus issue 2025; E024 online 2025 versus issue 2026. These are not duplicate publications. Diacritics are transliterated in CSV/BibTeX; normalize at bibliography freeze. E016 prior incomplete authorship remains open. Sources not fully read are marked accordingly.

## Gate decision
NO novelty confirmation. Continue to Prompt 05 (adaptive submodularity, probing, information lower bounds), then certification audit. Do not implement or write paper.
