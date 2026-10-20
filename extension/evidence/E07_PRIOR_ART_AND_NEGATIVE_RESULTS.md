# E07 — Prior art and negative-results memo
Date 2026-10-20

## Primary source checks
1. Vayanos, Georghiou & Yu, Robust Optimization with Decision-Dependent Information Discovery, Management Science, online 2025, volume 72(2):1509–1528 (2026), DOI 10.1287/mnsc.2021.00160, https://pubsonline.informs.org/doi/10.1287/mnsc.2021.00160. Explicitly covers two- and multistage costly strategic information revelation, correctness and finite reformulations. Preprint arXiv:2004.08490 is same work, not a second study.
2. Paradiso, Georghiou, Dabia & Tönissen, Exact and Approximate Schemes for Robust Optimization Problems with Decision-Dependent Information Discovery, INFORMS Journal on Computing 37(6):1457–1477 (2025), online 2024, DOI 10.1287/ijoc.2023.0290, https://pubsonline.informs.org/doi/10.1287/ijoc.2023.0290. Exact algorithm, K-adaptability, orienteering and shortest-path benchmarks. Reproducibility snapshot https://github.com/INFORMSJoC/2023.0290 not executed here.
3. Jin, Georghiou, Vayanos & Hanasusanto, Distributionally Robust Optimization with Decision-Dependent Information Discovery, Mathematical Programming, published online 20 Apr 2026, DOI 10.1007/s10107-026-02346-0, https://experts.illinois.edu/en/publications/distributionally-robust-optimization-with-decision-dependent-info/. Its arXiv:2404.05900 preprint is a version, not an independent study.
4. Javdani et al. 2014, PMLR https://proceedings.mlr.press/v33/javdani14.html: overlapping decision regions and stopping when a decision suffices.
5. Classical weighted set cover and binary hypothesis testing are standard mathematical baselines, not new hardness/probability results.

## Negative novelty verdict
- Budget-sensitive restoration can be formulated with covering constraints in restricted cases, but this is classical.
- A noisy observation can improve Bayesian success without providing robust success, a classical distinction.
- Irreversible cost constraints and information acquisition are already central to DDID and related sequential decision theory.
- No nontrivial novel graph-family lower bound, new complexity class separation, approximation ratio or robustness theorem survived E07.
- E06 false separation remains retracted and must not be revived by changing baselines or hiding repair costs.

## Audit limits
Publisher/institutional abstracts and bibliographic metadata were inspected for the cited direct predecessors; no exhaustive full-proof prior-art audit, no 64-record systematic search, no independent numerical implementation, no simulated performance or new reference-registry mutation.
