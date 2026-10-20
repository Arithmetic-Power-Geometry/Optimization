# E05 — Theorem Discovery I: exact information-separation family
Date: 2026-10-20. **Proved elementary construction; originality NO-GO (static DRD/tomography specialization).**

## Formal construction B(n), n>=2
Take n vertex-disjoint two-edge branches with terminals (s_i,t_i), internal unmonitored vertex u_i, edges e_i^L=(s_i,u_i), e_i^R=(u_i,t_i). Monitor only s_i,t_i; the only permitted path test on branch i is p_i=s_i-u_i-t_i (CAP/CSP; no local inspection). The graph may be disconnected; if connected topology is required, attach branches to a hub through *unmonitored* extra always-UP edges and prohibit cross-branch tests by the explicit monitor-access policy L. For the main proof use the disjoint, fully specified multi-demand graph. Service demands D={(s_i,t_i):1<=i<=n} require ALL n branches operational.

Hidden state theta=(j,z), j in {1,...,n}, z in {L,R}, exactly e_j^z is failed and every other edge UP. Initially each p_i is admissible (even when DOWN), with O(theta,p_i)=DOWN iff i=j. A repair a_i is an *authorized restoration of both existing edges* of branch i as one indivisible, unit-cost maintenance operation, not an individual edge restoration and not a topology bypass. Its effect restores any failed edge in branch i; all other branches remain unchanged. Repair budget is exactly one such action. There are no direct inspections, no noisy probes, no route edits, and no probe feedback after the terminal repair. Every p_i costs one probe unit. The policy must first select tests then choose one a_i; compare to exact identification of theta using exactly the same tests and without any repair before identification.

## Proposition E05.P1 — strict information separation (elementary)
For n>=2, (a) exact failure-edge diagnosis is impossible using any finite number of admissible pre-repair probes; (b) identifying a repair guaranteed to restore all demands requires exactly n-1 tests in the worst case; (c) a successful repair costs one intervention unit. In particular Q_D(n)=infinity while Q_R(n)=n-1.

**Proof.** For each j, states (j,L) and (j,R) produce the same outcome on every admissible test: p_j returns DOWN and p_i for i!=j returns UP. Hence they cannot be distinguished by any adaptive test sequence, proving (a). For (b), probe p_1,...,p_{n-1} sequentially. If any p_j is DOWN choose a_j; otherwise choose a_n. Exactly one branch is damaged, and its group action restores either edge, so every demand becomes UP. This uses at most n-1 tests. For the lower bound, along a history of UP outcomes on distinct tested branches, every untested branch is a possible damaged branch, and no single a_i can restore two different candidate branches. Therefore a robustly valid a_i requires at most one untested branch. A worst-case adversary answers UP for the first n-1 distinct branch probes, forcing >=n-1 tests. Repeated probes convey no new information. Part (c) follows from the repair action definition. QED.

## Proposition E05.P2 — tight expected cost under a uniform prior
If j is uniform on n branches, z arbitrary, tests deterministic and unit-cost, and only one repair is allowed, an optimal sequential testing policy has expected number of probes
E[T]=sum_{k=0}^{n-2}(n-k)/n = (n-1)(n+2)/(2n).
For n=2, E[T]=1; for n=3, E[T]=5/3.

**Proof.** By symmetry, test any untested branch. A DOWN outcome identifies j; an UP outcome removes one candidate. The last branch needs no test. Probability of reaching probe k+1 (zero-based k=0,...,n-2) is (n-k)/n, so summing yields the formula. Any correct policy must continue while at least two branches remain and only an untested branch test can distinguish them, proving optimality. QED.

## Why P1 and P2 are NOT claimed new
The repair-valid decision regions are R_i={(i,L),(i,R)}, which form a partition; a decision-sufficient test identifies the region rather than the exact state. This is a classical equivalence-class/decision-region determination instance (Golovin et al. 2010; Javdani et al. 2014), combined with elementary path-signature nonidentifiability from network tomography (Ma et al. 2015). The group-repair action is deliberately specified and is not the same as a single-edge repair. A result with infinite diagnosis cost is less persuasive than a finite, nontrivial quantitative separation. It does not prove repair-dependent observability or a new graph theorem.

## Tightness, boundary and falsifiers
- If the maintenance action may restore only one edge, no robust one-action repair exists because (j,L)/(j,R) are indistinguishable. Then Q_R=infinity, eliminating the separation.
- If the internal u_i becomes an authorized monitor, local subpath tests may distinguish z and Q_D can become finite.
- If one universal all-branch repair is authorized and affordable, Q_R=0.
- If n=1, no probe is required to choose a_1 and exact edge diagnosis remains impossible.
- If the service predicate requires only *some* branch UP, the initial network already satisfies service for n>=2, and the claimed positive repair cost collapses.
- A physically unavailable probe is not a DOWN observation. The construction uses installed, testable failed branches.
- If policies can perform repairs during diagnosis, diagnosis's task definition changes and the comparison must be restated.

## Unresolved target for E06–E08
Seek a graph family with *finite* exact diagnosis cost, a nontrivial **finite** separation under matched rights and/or repair-induced feasible path changes, and an independent structural theorem beyond static DRD/POMDP. This E05 family is a negative originality result, not a submission theorem.
