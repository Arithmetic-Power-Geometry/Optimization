# Prompt 17 — strict proof and originality gate (2026-10-20)

## Verdict: NO-GO for original theorem
No new nontrivial complexity/approximation/minimax theorem has been proved. The proposed decision-sufficient repair criterion is already closely related to classical equivalence-class determination (Golovin–Krause–Ray 2010 E064) and decision-target noisy active learning (Chen–Hassani–Krause 2017 E065). Do not treat the following elementary constructions as original discoveries.

## T17.1: end-to-end-only non-identifiability counterexample (complete proof)
Physical graph is the path s—u—t with edges e1=(s,u),e2=(u,t). Exactly one of e1,e2 is failed, and the only allowed probe is the full designated s–t path, returning UP iff both edges function. Each probe is authenticated, noiseless, and costs c>0. At most one edge can be repaired; no bypass edges may be installed. Both states F1={e1} and F2={e2} yield DOWN to every permitted probe before repair. Therefore no observation-only policy (regardless of the number of repeated probes) can choose a correct single repair in both states. Proof: induction on observation history: the first outcome is DOWN in both states; identical histories imply identical next probe and outcome, so terminal repair choice is the same. It cannot fix both distinct states. If repairs themselves may be made before further probes, this impossibility does NOT apply: repairing e1 then probing may distinguish the states; any theorem must specify repair-before-probe rights, budget, and whether unsuccessful repair can be undone. This is an elementary indistinguishability result, not novel.

## T17.2: overlapping valid-action regions are not equivalence classes (complete proof)
Let Theta={a,b,c} and terminal repair regions R1={a,b}, R2={b,c}, with no region containing all three. Then a and b share R1, and b and c share R2, while a and c share no region. Hence the binary relation 'shares a feasible repair' is not transitive. Thus these action-valid regions cannot be represented as the equivalence classes of that relation. This does NOT imply they evade established decision-region determination, set-cover stopping or POMDP formulations; it only blocks an invalid partition argument.

## T17.3: asymmetric repair cost does not create a novel sensing theorem
If repair R1 costs 1 and R2 costs 2 in T17.2, after observations the robust optimal terminal action is argmin over actions whose region contains the surviving state set. This is a finite cost-sensitive terminal decision, representable in POMDP dynamic programming with costs. It does not itself prove a new policy-size gap or complexity class separation.

## Explicit baseline
For finite Theta and finite horizon H, let B(h) be the set of physical failure states consistent with authenticated transcript h. For each repair action a, R_a={theta:L(theta,a)}. Terminal robust feasibility is B(h) subseteq R_a; terminal cost is min_{a:B(h) subseteq R_a} c(a). Recursion over feasible path probes, outcomes, and admissible edits is a finite-horizon minimax decision tree / belief-state dynamic program. No efficient-size representation or novel lower bound follows automatically.

## Literature gate
E064 original NeurIPS 2010 full PDF explicitly defines equivalence-class determination and proves a competitive approximation theorem for EC2 under a rational prior; its decision-theoretic section maps testing to selection of an optimal action under loss. E065 Chen–Hassani–Krause AISTATS 2017 full text addresses noisy correlated tests and decision-target learning, with ECED. These are direct originality collisions. E059–E063 technical-proof companions were identified and linked, but no exhaustive line-by-line audit of every theorem was completed. Thus strict proof gate fails both originality and full-audit requirements.

## Future test
Only consider a distinct **physically constrained path-probe** theorem with overlapping valid repair regions and an explicit model for repairs-before-sensing if a nontrivial bound survives published prior art. Current result: NO-GO for drafting theorem paper. No software, experiments or manuscript.
