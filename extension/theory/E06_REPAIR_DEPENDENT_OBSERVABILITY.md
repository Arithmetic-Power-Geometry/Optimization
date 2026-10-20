# E06 — Repair-dependent observability: explicit construction and proof
Date: 2026-10-20. Status: **elementary conditional separation PROVED within specified model; novelty NOT ESTABLISHED**.

## Construction G_gate
Physical service path s--e_L--u--e_R--t consists of two installed edges. Exactly one of e_L and e_R is failed, with hidden state theta in {L,R}; both remain installed. Service demand D={(s,t)}. A separate installed monitor-access edge g joins a controller access node c to monitor station u; g is failed in BOTH hidden states. The monitor-access edge g is not part of the service s-t path and is not counted as a substitute service route.

Before any intervention, only s and t have controller-authorized measurement access. A full s-u-t end-to-end path test p0 is admissible and returns DOWN in both states. Subpath tests p_L=s-u and p_R=u-t are **not admissible**, because u has no controller monitor access. The controller knows the monitor access configuration, including that g is down, but not which service edge failed. Restoring g (action a_g, unit repair cost) succeeds deterministically and publicly restores access to u. It does not restore either service edge. After a_g, p_L and p_R become admissible (installed, testable paths), and one test of p_L yields DOWN exactly when theta=L, UP exactly when theta=R. Action a_L restores e_L, action a_R restores e_R; both cost one repair unit and succeed deterministically. All three repairs are irreversible and consume a repair unit. Total repair budget=2; probe budget=1; horizon permits a_g, one probe, one service repair. No free terminal repair, no direct edge inspection and no universal bypass.

## Policy classes and matched rights
Adaptive class A may interleave actions; sensing-first class S must complete all probes before its first repair, then may use remaining repairs but no more probes. Both classes have exactly the same installed graph, monitor permissions, three repair actions, state information, probe budget, repair budget, service success predicate and costs. The ordering restriction is the **only** policy-class difference. If sensing-first is redefined to allow probing after its first repair, it becomes an interleaving policy and the separation disappears by definition.

## Proposition E06.P1 — repair can activate a previously inadmissible probe
In G_gate, a_g changes admissibility of p_L and p_R from false to true, without changing their installed edge status. Before a_g, p0 returns DOWN for both theta; after a_g, p_L has outcome DOWN for L and UP for R. This follows immediately from public monitor access and the separate admissibility/outcome functions in E04. This is a formal example, not a novelty theorem.

## Proposition E06.P2 — matched-rights robust feasibility separation
With two repair units and one probe unit, adaptive interleaving A admits a robustly successful policy, while sensing-first S has no robustly successful policy.

**Proof (upper bound).** Interleaving executes a_g, publicly enabling u. It tests p_L. On DOWN, it restores e_L; on UP, it restores e_R. This consumes exactly two repair units and one probe, and restores the unique failed service edge in either state; thus C(x,D)=1 robustly.

**Proof (lower bound for S).** Before its first repair, S can only test p0, whose outcome is DOWN under both L and R; repeating cannot distinguish. At the start of its repair-only phase, both states remain possible. To restore service in both states without subsequent observation, S would need to restore both e_L and e_R, costing two units. It could do so without restoring g; indeed with repair budget two, S can simply repair both service edges and succeed. Therefore the claimed infeasibility is **FALSE** in this construction! This counterpolicy invalidates the proposed separation. E06.P2 is **RETRACTED** and must not be cited as a proved theorem.

## Corrected conclusion
The action a_g is not mandatory for the service predicate. With two repair units, a sensing-first policy repairs both e_L and e_R, restoring service without information. Hence the construction proves only P1 (dynamic probe admissibility), not a strict robust-feasibility separation. Under one repair unit, a_g plus target repair is unaffordable, so the interleaving policy also fails. A separation might require extra service constraints, repair costs, distinct budgets, or a larger fault family, but must avoid a contrived mandatory access-gate condition and must match rights.

## General repair-budget counterargument
If at most k service edges might independently be failed, all k edge restorations are allowed, guaranteed successful and cost one, and the repair budget permits k, then a sensing-first policy can restore all k edges without probes. Thus activating observability cannot by itself imply a robust-feasibility advantage. The argument depends on guaranteed restorations and known finite candidate set; it does not extend to costly/unavailable repairs.

## Open conjecture E06.C1 — explicitly UNPROVED
There may exist a parameterized family with intervention-induced path admissibility changes and tight robust **cost** separation (not just feasibility) against a sensing-first class under identical action rights, without allowing a cheap universal repair. No family or proof satisfying all constraints has been verified in E06. Prior-art collision with POMDP, progressive recovery and multistage DDID remains substantial.
