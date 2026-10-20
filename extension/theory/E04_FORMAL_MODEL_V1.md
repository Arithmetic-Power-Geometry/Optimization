# E04 — Versioned mathematical specification v1.0
Date: 2026-10-20. Status: SPECIFIED, NOT NOVEL; no experimental or theorem claim.

## 1. Graph and physical state
Let G0=(V,E0) be a finite undirected multigraph with distinct edge IDs (parallel edges permitted). For a state x, E_x subset of E0 union E_add is the set of installed edges; f_x:E_x->{0,1} is the actual operational indicator, 1=UP. Hidden exogenous failure theta in finite Theta constrains initial f and optional post-action stochastic transitions. Monitors M_x subseteq V and access policy L_x define which endpoint pairs can originate/receive tests. A physical state x=(E_x,f_x,M_x,L_x,auxiliary resource status); a complete planning state is s=(theta,x,b,t,k) where b is remaining vector budget, t is elapsed time and k is remaining decision horizon. Theta and the physical state are not necessarily observed by the controller.

**No conflation:** an edge present in E_x may be failed; a physically failed path is not automatically an inadmissible probe. An edge absent from E_x cannot be traversed as an installed path.

## 2. Test feasibility is not test success
A test descriptor p=(u,v,walk,routing_mode) specifies a proposed end-to-end measurement. The state-dependent admissibility predicate A(x,p) requires (i) u,v in M_x and access granted by L_x, (ii) the prescribed walk uses installed edges and is permitted by the chosen routing mechanism, (iii) the test apparatus can launch and report a result. Crucially A does NOT require every traversed edge to be UP. The deterministic noiseless observation is O(x,p)=UP iff every traversed edge has f_x(e)=1; otherwise DOWN, conditional on A(x,p)=true. For noisy tests use Z(o|s,p) and distinguish instrument error from path failure. A probe that is not launchable is an **INADMISSIBLE ACTION**, not an observed DOWN; if a protocol explicitly emits UNREACHABLE, it must be modeled as a third outcome and its cost specified.

Routing modes: CAP permits admissible monitor-to-monitor walks; CSP only simple paths; UP only the current protocol-selected route. In a dynamic graph, routes may be recomputed following edits; do not assume CAP/CSP/UP share test rights. Do not silently grant direct edge inspection.

**Information pattern:** If A depends on hidden x, an agent cannot simply choose actions knowing A(x,p). Default model: public control configuration c(h) determines the advertised feasible descriptor set T(h); tests must be admissible in every s in the current belief B(h) unless a separately modeled attempted-test action with failure feedback exists. This avoids leaking hidden failures through a hidden feasibility oracle.

## 3. Repairs, interventions and state transitions
An intervention a=(kind,target) has precondition P(s,a), physical transition F(s,a,xi), duration tau(s,a,xi), nonnegative resource vector c(s,a,xi), and possibly observation feedback Z_a(o|s',a). Actions include restore_existing_edge, install_bypass, relocate_monitor, change_route and verify_service; these are DISTINCT action types with separately stated permissions. Restoring e changes f(e) from 0 to 1 only when allowed and repair succeeds; on an already-UP edge it may incur cost but not create a second repair. Installing a bypass changes E_x and is not an ordinary edge restoration. If repair outcomes are uncertain, transition distributions or adversarial outcomes must be specified. Irreversibility means the action consumes its allocated intervention quota even if it fails, and no inverse edit is available in the allowed action set. A repair may change both physical service and subsequent test admissibility, but neither change is assumed by default.

## 4. Information state, updates and action rights
History h_t=(a_0,o_1,...,a_{t-1},o_t) plus public budget/time counters determines policy decisions. Robust belief B_t is a set of feasible complete states consistent with the initial state family, deterministic transitions and observed outcomes. For action a and outcome o:
B_{t+1}= {s' : exists s in B_t, s' in Succ(s,a), a admissible at s, Obs(s',a)=o}.
For noisy/Bayesian models posterior mu_{t+1}(s') proportional to sum_s mu_t(s) P(s'|s,a) Z(o|s',a), with denominator >0; a zero-probability observation is not an ordinary posterior update. The controller may use only public h_t and not theta or actual f.

**Common-feasible robust action:** a is allowed at B iff P(s,a) holds for every s in B and its worst-case resource use is <= remaining b. An alternative risk-taking model must define failed-precondition feedback and charge the attempted action consistently; never mix the two.

## 5. Cost, budgets and horizon
Define nonnegative vector c=(repair units, probe units, money, time) and budget b with componentwise constraints. All actions, including unsuccessful edits, probes and explicit service-verification actions, debit the budget once at their actual transition. If the horizon is H actions, no transition occurs after H; stopping is a terminal decision, not a free additional repair. Objective choices must be stated: (A) minimum expected total cost subject to posterior success threshold; (B) minimum worst-case cost for robust service; (C) maximum success probability within fixed budgets. Never compare objective values from different conventions or count a terminal plan's repair cost twice.

## 6. Service, stopping and success
For service demand d=(s,t), define C(x,d)=1 iff there is an operational s-t path in (V,{e in E_x:f_x(e)=1}); multi-demand C(x,D)=1 iff all required demands hold. **Robust success** after terminal stop means for every s in B(h), C(x(s),D)=1. **Bayesian success** means posterior probability sum_{s:C(x(s),D)=1} mu_h(s) >= alpha for specified alpha in [0,1]; expected success and guaranteed success must not be interchanged. An explicitly chosen terminal repair plan pi is valid only if every physical action in pi is feasible, affordable and charged; terminal plans are not free. Service attestation by a signed measurement certifies record origin/integrity, not that C(x,D)=1 absent sensor reliability assumptions.

## 7. Static subcase and prior-art boundary
If tests do not change x, admissible test set is fixed, and stopping selects a repair decision without executing it during sensing, define R_a={theta: a would restore service}. Then robust stopping B subset R_a is overlapping decision-region determination (Javdani et al., AISTATS 2014). This is not a new theorem. Fixed-graph binary path observations are a tomography subcase (Ma et al., 2015/2017). Finite state/action/observation transitions embed in POMDP theory. Novelty must arise from a separately proved structural result or independently validated method.

## 8. Contract for later research
E05–E08 may specialize v1.0, but must record each assumption change and adversarial countermodel. E09–E10 code must implement test-admissibility and test-outcome as distinct functions; assert no hidden-state leakage, no negative budgets, no double charging, no silent bypass, and correct state transitions. No algorithm implementation or experiment is claimed by E04.
