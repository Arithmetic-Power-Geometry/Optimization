# P03 proof and originality gate — 2026-10-21

## Frozen finite-state model
An instance has finite edges E, service edges S, equiprobable hidden failed-edge sets W, finite measurement paths P with physical access paths A, two independent integer budgets (repair actions r and probe actions q), deterministic UP/DOWN path outcomes, and irreversible edge repairs. A probe is admissible only if its *access path* is operational for every currently possible hidden state. This conservative admissibility rule is not equivalent to a generic edge oracle. An UP measurement means all measured path edges are operational; access-path feasibility is evaluated separately. The terminal objective is the **Bayesian probability** that every service edge is operational after chosen repairs. This is NOT the manuscript's robust minimax total-cost objective; the objectives must not be conflated.

## Exact oracle
For posterior state set B and repaired-edge set R, let T(B,R) be the fraction of B with all service edges operational. V(B,R,r,q) is max of T, V after every admissible repair, and sum over outcome branches p(o|B,R) V(B_o,R,r,q-1) for every admissible informative probe. Repairs decrease r, probes decrease q, so recursion terminates. Uniform prior and deterministic outcomes imply branch probabilities |B_o|/|B|. Finite exhaustive search returns the optimal Bayesian terminal success probability **for this model only**. Memoization avoids repeated subproblems but does not imply polynomial time; state space is exponential in |E| and |W|.

## Falsifiable gate example
Edges g,a,b,c. Service path (a,b,c). Worlds {g,a}, {g,b}, {g,c} each probability 1/3. Probes on path (a) and path (b) require physical access via g. Two repair actions and two probes permitted. Initial access g is down in every world, so probing is unavailable. Repair g, then test a; if a is DOWN, repair a. If a is UP, test b and repair b if DOWN, otherwise repair c. The exact success probability is 1. Without restoring g, any two service-edge repairs cover only 2/3 of the worlds. The myopic heuristic selects two service-edge repairs and succeeds with probability 2/3. Independent second implementation checked 1 and 1/3 when repair budget is reduced to one.

## Elementary bound and independent checker
For n service edges, one uniformly failed edge, only full-path probe (always DOWN), and one repair, any policy succeeds in exactly 1/n of the worlds. The independent checker reproduced n=2,...,8. This is a symmetry observation, not an original theorem.

## Counterexamples and restrictions
- A universal repair action (if allowed) may dominate all probing; no universal advantage to adaptivity follows.
- With two uncertain service edges and two repair actions, simply repair both: no gate-repair benefit.
- A physically feasible path measurement is not an arbitrary edge query; probes must obey explicit path and access assumptions.
- Repairing g can be interpreted as restoration of a separate access link; if g is not part of the service requirement, physical repair budgets still charge its cost.
- Gate example is deliberately constructed. It does not show asymptotic advantage, real outage validation, or improvement against matched Hyperedge Cutting, DDID, or POMDP baselines.
- Bayesian probability of success is not the zero-error robust stopping requirement; both must be evaluated separately in later work.

## Candidate heuristic
The implemented myopic_policy greedily selects a feasible repair maximizing *immediate* expected terminal success and stops when no improvement remains. Probes with no immediate restoration value are not chosen. Complexity per decision is O(|E| |W| |S|) ignoring sorting and model validation, with at most r repair steps. This heuristic is **not novel** and intentionally illustrates a failure mode of greedy immediate-restoration policies.

## Prior-art decision
Javdani et al. (2014) already give decision-region determination and HEC with guarantees; decision-dependent information discovery and POMDPs encompass many forms of action-dependent observation. Thus **NO-GO for original algorithm or new theorem**. The gate example is an informative pedagogical separation from a *myopic comparator only*. Stronger novelty and fair algorithm comparisons remain P04 and P05 gates.

## Execution verification
A separate, locally executed independent_checker.py evaluated seven n-path bounds and four additional examples: **11 assertions passed**. The committed GitHub unit-test file and main kernel have **not** been executed byte-for-byte from a clean GitHub checkout in this run. Do not represent the independent checker as a clean-checkout test of the committed code. GitHub code was independently re-fetched and compared with the content supplied to GitHub.
