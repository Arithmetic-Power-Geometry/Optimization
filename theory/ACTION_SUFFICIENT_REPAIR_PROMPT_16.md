# Prompt 16 — action-sufficient repair theorem gate (elementary only)
Date: 2026-10-20. No original theorem established.

## Model repair to avoid ambiguity
Use a three-node series graph s—u—t with two required edges e1=(s,u), e2=(u,t), and an optional irrelevant dangling edge e3. Hidden states are subsets of failed edges. Budget permits **at most one** repair, each repair restores one named failed edge at cost 1; there is no new s–t bypass. A trusted test may inspect one edge, at cost c>0, returning its true binary status. Terminal target is physical s–t connectivity; certificate is a path checked against authenticated inspection/repair logs. Distinguish physical correctness from verifier acceptance.

## E16.1: one-bit necessity on two-state family (elementary)
Let Theta={F1={e1},F2={e2}} with uniform or adversarial hidden state. Under budget one, repairing e1 succeeds only for F1 and repairing e2 only for F2. A policy with no observation must make the same repair under both states (randomization cannot yield probability 1 under both), so robust zero-error repair requires at least one informative test. Inspecting e1 distinguishes F1 and F2, and choosing the matching repair succeeds. Thus exactly **one** noiseless test is necessary and sufficient when the available probes include e1 inspection. Worst-case total sensing+repair cost c+1, ignoring fixed equal verification overhead. This is standard binary decision-tree reasoning, NOT new.

## E16.2: robust repair without exact failure identification
Let Theta={F1={e1},F2={e1,e3},F3={e2}}. Edge e3 is dangling and irrelevant to s–t connectivity. Under one repair, F1 and F2 both require e1; F3 requires e2. Inspect e1 once: failure implies F1 or F2, repair e1; success implies F3, repair e2. Robust connectivity succeeds, yet F1 versus F2 remain indistinguishable under this test. If no permitted probe observes e3, exact state identification is impossible, while repair remains possible. This is an elementary *action sufficiency versus state identification* separation, not a new information-theoretic lower bound.

## E16.3: finite robust repair as decision-region identification
For each allowed edit tau define R_tau={F in Theta: L(F,tau)=true}. Given a history h, the feasible robust terminal edits are those tau for which support(Theta|h) subseteq R_tau. Thus robust stopping means the version-space support is contained in **at least one** action-valid region. Regions can overlap; they need not partition Theta. Proof: directly unfold the universal robust-validity quantifier. Under noiseless finite tests this is a generalized decision-region stopping problem, subject to edit costs; noisy tests with full support cannot shrink robust support and require chance or bounded-error semantics. This is an elementary equivalence of predicates, NOT a novel theorem.

## E16.4: false inference from region identification to unique diagnosis
The E16.2 model has a terminal region {F1,F2} sharing repair e1. Hence any lower bound demanding separation of F1 and F2 is not necessary for repair. Conversely, if action regions are pairwise singleton, region identification equals full state identification. Both claims are immediate.

## Reductions and research gate
The terminal predicate and sequential test selection reduce to known decision-region determination/active learning when repair costs are constant. E064 Golovin–Krause–Ray NeurIPS 2010 studies noisy cost-sensitive active learning; this is a strong nearby baseline, though exact overlap of its theorem hypotheses with overlapping action-valid regions is **not yet verified**. With arbitrary terminal edit costs, finite horizon still reduces semantically to POMDP planning. No complexity or approximation separation beyond these known settings was proved. Any future claim must explicitly handle overlapping decision regions, asymmetric repair costs, physically attested observations, and a natural graph family.

## Primary-proof audit limitation
E059–E063 paper and proof companion identities/abstract claims confirmed in earlier prompts; individual original theorems, all lemmas and full proof derivations were **not independently checked** in this turn. Do not label them theorem-verified. No software or numerical experiments were performed.
