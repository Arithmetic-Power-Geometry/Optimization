# E08 — Fresh reconstruction and adversarial countermodel checks
Date: 2026-10-20. Independent analytical re-derivation by a second pass over stated assumptions; NOT an independent human referee and NOT an executable exhaustive oracle.

## 1. E05 lower bound re-derived
There are n candidate damaged branches j, each with two internal edge states z. Probe p_i reports DOWN iff j=i, independent of z. Exact edge identification is impossible because (j,L) and (j,R) induce identical full observation vectors. To select one branch-specific composite repair robustly, after k distinct UP results the surviving candidate branches number n-k. A single branch repair works for every remaining state only if n-k<=1; thus k>=n-1 along the all-UP adversarial history. Testing n-1 distinct branches achieves equality. This is a static DRD partition case, not a new theorem.

Expected probes for uniform j: P(T>=r)=(n-r+1)/n for 1<=r<=n-1, sum = (n-1)(n+2)/(2n). Small n: 2=>1; 3=>5/3; 4=>9/4. No simulator used.

## 2. E06 repair-gate countermodel
Hidden service fault L or R; access gate g is down in both. Interleaving spends 1 to restore g, tests one subpath, spends 1 to restore correct service edge. However sensing-first spends 2 to restore both service edges without ever repairing g or probing, yielding success in both hidden states. Same action rights and B_R=2. Therefore any 'adaptive feasible, sensing-first infeasible' assertion is false. With B_R=1, the exhibited adaptive plan is unaffordable, so simply lowering budget cannot repair the claim. No physical path probe may be treated as a direct edge oracle.

## 3. E07 proofs re-derived and assumptions tested
C1: guaranteed monotone repair of all possible failed service edges yields robust service; if a restoration may harm other service paths, conclusion can fail.
C2: identical pre-repair transcripts imply identical repair-only continuation, so its action plan must cover all indistinguishable states; if action outcomes produce feedback during repairs, repair-only phase could branch and the claim needs revision.
C3: minimum weighted set cover only under explicit union-of-coverage terminal semantics; for network service requiring simultaneous repairs of several edges, union coverage of *states* is insufficient. Example: one state with two failed serial edges; restoring either one alone does not restore service, yet naive coverage of that state by both singleton actions could incorrectly predict a one-action success. The E07 restriction is essential.
C4: equal likelihood factors preserve posterior odds; informative tests violate premise.
C5: under uniform prior, symmetric error epsilon, one MAP decision succeeds with probability 1-epsilon; epsilon=0 gives 1, epsilon=1/2 gives 1/2.
C6: when epsilon>0 both observations have positive likelihood under both states, so no one-test one-repair mapping guarantees service for every state/outcome. This is not the same as the Bayesian guarantee.

## 4. Unchecked obligations
No exhaustive finite-state action enumeration; no code, seeds, solver, CI, or simulator executed. No full-text proof-by-proof audit of all 64 original registry entries. No original manuscript source snapshot. A true independent software checker is a deliverable for E09/E10, not E08.

## 5. Falsification priority for E09
Check all 18 E04 contracts, E05 n=2..5 branch cases, E06 two-state gate with repair budgets 0..3, E07 symmetric noise epsilon=0,1/4,1/2, and repair-feedback counterexamples. Assert budget accounting, service feasibility and no hidden-state leakage.
