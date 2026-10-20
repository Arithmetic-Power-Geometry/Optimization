# Prompt 15 adversarial falsification of Q14 — 2026-10-20
No original theorem established. The following are **elementary countermodels** under explicit assumptions, not computational experiments.

## C15.1: Universal-repair counterexample
Take a physical graph with two parallel s–t paths, each consisting of a single potentially failed edge e1 or e2; exactly one may fail. An allowed edit is installation of an independent new s–t edge e3, guaranteed functional, cost 1. All authenticated probes have positive cost. Repairing with e3 works for every hidden failure state, so the optimal robust policy requires zero probes. Thus any unconditional positive lower bound on sensing for robust connectivity repair is false. If the action set forbids e3, the example does not apply; the edit family is a theorem-critical assumption.

## C15.2: Repair need not identify failure
Let two hidden states F1={e1}, F2={e2} affect two parallel edges; only a fixed shared replacement edge e3 is permitted. Both states require the same action. The observation distributions may be identical and unique localization impossible, yet robust repair is possible. Therefore *identifiability is not necessary for repair* and a tomography lower bound cannot be copied to repair without an action-disjointness premise.

## C15.3: Authentication does not imply correctness
A sensor signs a binary observation "path up" even though a physical edge has failed (sensor fault/noise). Signature verification succeeds; physical connectivity is false. The verifier's provenance predicate and the physical target predicate differ. Claims of sound physical attestation require a trusted sensor-error assumption or an independent physical measurement oracle.

## C15.4: Equal-cost reduction
If authenticated probing consists of ordinary observation y plus deterministic public signature verification cost d(s), absorb d(s) into the probe cost c'(s)=c(s)+d(s). Histories, feasible policies and objective values match a priced POMDP model, provided signatures convey no new information and no policy restrictions depend on cryptographic secrets. Hence charging signature verification alone does not establish a new expressive paradigm or complexity bound.

## C15.5: Fair policy comparator
Adaptive policies include fixed-schedule policies only when both use identical sensor sets, horizon, edits, terminal validity semantics and certificate rules. Allow the nonadaptive policy to condition its final edit on observed outcomes; otherwise a purported gap is artificially inflated.

## C15.6: Identifiability versus action sufficiency
A robust policy need only distinguish failure states requiring incompatible feasible terminal edits. Define action equivalence F~F' when a common terminal edit is feasible for both; this is not necessarily transitive, so **do not** call it an equivalence relation without proving transitivity. The relevant object is the family of sets of hidden states sharing a feasible repair, not necessarily singleton localization classes.

## Literature/theorem-level audit
E059 publisher abstract states CAP optimal monitor-placement algorithm, CSP/UP bounds, and linear-time CSP single-failure monitor placement. E061 is the author's full-proof technical companion; its *existence and relationship* were independently verified, but individual lemmas and proofs were not checked line by line. E060 was identified as the 2017 IEEE/ACM Transactions on Networking journal article (DOI 10.1109/TNET.2016.2584544), corresponding to 2015 arXiv:1509.06333; E063 arXiv:2012.09959 is its technical proof companion. E062 is the 2014 study's proof companion. This is publication-relationship verification, **not** an independently completed theorem-by-theorem proof audit.
Q14 as a general novel framework: NO-GO. Narrow theorem search remains conditional on a specific family with disjoint feasible repairs, nontrivial attestation information, and a bound not already explained by diagnosis or priced planning.
