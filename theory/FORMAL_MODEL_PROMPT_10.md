# Prompt 10 — Formal model and falsification programme
Status: research definitions and elementary baseline propositions; **no new theorem or novelty claim**.
Date: 2026-10-20

## 1. Finite, fully specified model
An instance is I=(Theta,mu,G0,S,Y,K,T,L,P,V,c,B). Theta is a finite set of hidden physical network states, with optional prior mu of full support; G0=(V0,E0) is a finite labelled graph; S is a finite set of sensing actions; Y_s finite outcomes; K_s(y|theta,h) is a rational stochastic kernel conditional on history h, including dependence induced by prior edits. T is a finite set of graph edits, each specified by explicit vertex/edge insertion/removal and preconditions. An admissible policy pi maps a finite observation/edit history h to a sense, edit or halt action. Finite horizon H and rational action costs are encoded in binary. Policies may randomize unless a theorem explicitly excludes this.

A final edit sequence tau produces G_tau(theta), possibly dependent on physical theta. L(theta,tau) is the target validity predicate (e.g. s-t connectivity under the actual physical failures). The public instance string enc(I,tau) may contain *declared* observations but cannot silently include theta. A fixed proof system P with alphabet Sigma and deterministic verifier V_P(enc(I,tau),w) in polynomial time checks a witness w. A trusted measurement attestation, if allowed, must be part of the instance and charged; otherwise a proof of the declared graph is not a proof of physical truth.

Define:
- Encoded-instance validity: V_P(enc(I,tau),w)=1 and soundness implies L_enc(I,tau).
- Robust validity: for every theta consistent with admissible histories or every theta in a specified uncertainty set U, L(theta,tau)=1.
- Chance validity: Pr_{theta~mu,Y~K,pi}[L(theta,tau_pi)=1] >= 1-delta.
These are distinct predicates. Witness existence for encoded validity does not imply robust or chance validity.

Costs per realized trajectory h: C(h)=sum_s c_s(h)+sum_t c_t(h)+g_P(enc(I,tau),w)+v_P(enc(I,tau),w). The functions g_P and v_P are explicitly charged computational work for witness generation and checking; they are not interchangeable with proof length |w|. One must specify a canonical witness-generation algorithm or optimize over algorithms with a common computational model, otherwise g_P can hide arbitrary advice. Expected cost E[C] and worst-case cost max_{theta,Y} C are separate objectives. Invalid termination has +infinity cost for hard-validity models, or a declared finite penalty for chance-constrained models.

## 2. Matched policy classes
Adaptive A: may select each sensing action from all prior observations, and edits may be interleaved if physically admissible.
Nonadaptive N: chooses the entire ordered sensing schedule (possibly randomized) before receiving observations, with exactly the same sensing alphabet, budget, edit options, certificate verifier, and terminal validity criterion. The final edit and witness *may* depend on the resulting observations. Do not handicap the baseline by requiring it to commit to a graph before sensing. If edits affect future observation kernels, specify whether the comparison class is edit-adaptive; otherwise comparisons conflate sensing adaptivity with physical action availability.

## 3. Elementary propositions (baseline only)
P10.1 (Containment). If all fixed schedules are admissible adaptive policies and the terminal edit/witness class is identical, OPT_A <= OPT_N for any common minimization objective. Proof: every fixed-schedule policy is a history-dependent policy that ignores its history. The feasible policy set N is contained in A. Taking infima proves the inequality. **This is not new.**

P10.2 (No automatic physical certificate). There exist two hidden states theta0,theta1 producing identical public encoded graph strings and the same accepted witness, but L(theta0,tau)=1 and L(theta1,tau)=0. Construction: two terminals joined by one edge; the public graph declares the edge present; theta0 has the working edge, theta1 has a failed edge; the witness is the declared s-t path. A deterministic verifier sees identical strings and accepts both. Therefore encoded-instance acceptance cannot imply correctness in both physical worlds without a trusted observation or robust condition. **Elementary indistinguishability, not new.**

P10.3 (Threshold-query adaptivity gap; known binary-search phenomenon). Theta={1,...,N}; a threshold sensor q_j returns 1[theta<=j] for j=1,...,N-1, deterministically, at unit cost. To terminate, identify theta exactly and insert one edge e_theta from s to the appropriate labelled terminal t_theta; only e_theta satisfies the state-specific target. The final witness consists of signed threshold responses that bracket theta, plus the edit index; verifier checks transcript consistency and unique identification, assuming authenticated sensor outcomes. Under worst-case zero-error validity and deterministic policies, adaptive sensing uses at most ceil(log2 N) queries by binary search; any nonadaptive schedule must query all N-1 thresholds: if threshold j is absent, states j and j+1 have identical responses to every other threshold, and cannot be distinguished. Thus adaptive upper bound ceil(log2 N) and nonadaptive lower bound N-1. This gap is classical adaptive search, **not an original theorem**. With randomization and almost-sure zero error, each nonadaptive schedule in support must still separate every pair, hence contain all N-1 thresholds. The same statement does not hold under unrestricted sensor actions or nonzero error.

P10.4 (Certificate-overhead collapse). If both classes must output the same fixed-size witness and the same terminal edit, and certificate generation/checking costs are a constant K independent of observation history, then their cost difference equals the difference in sensing costs (edit and certificate terms cancel). Thus P10.3 cannot establish a certificate-driven advantage. Proof: write C_A=S_A+E+K and C_N=S_N+E+K, subtract. **Elementary accounting.**

## 4. Counterexamples to broad conjectures
CEX-A (VOI complementarity). Two fair independent bits X,Y; utility for correctly guessing X xor Y. Observing either bit alone leaves best success 1/2, observing both raises it to 1. Thus marginal value of second observation increases after the first; general VOI is not submodular.
CEX-B (certificate mismatch). P10.2 shows an encoded graph path does not certify a physical edge under unobserved failure.
CEX-C (trivial certificate). If a proposed edge connects s and t, a constant-size path witness suffices; certificate checking need not be a bottleneck.
CEX-D (proof-language dependence). An encoding may admit short extended-system proofs but long proofs in a restricted system; no proof-length lower bound transfers to all proof systems.
CEX-E (unbounded cost ratio through zero costs). If observation cost is zero or OPT_A=0, adaptivity ratios can be undefined or uninformative; require positive normalized costs and clear additive/ratio benchmarks.
CEX-F (unrestricted sensor). A single action revealing theta destroys P10.3's threshold-only lower bound. Sensor alphabet restriction is substantive.

## 5. Falsifiable conjectures — explicitly unproved
H10.1: In a fixed proof system and a carefully restricted family of physically hidden graph edits, the optimal **combined** sensing/edit/proof-generation/checking cost exhibits a separation not explainable by standard DDID or adaptive search. Falsify by a polynomial reduction to E029 or E050 or by decomposing certificate cost as in P10.4.
H10.2: There exists a family where a certificate *requirement* changes the identity of the optimal sensing action, compared with an otherwise identical uncertified objective. Falsify if witness cost is constant or only terminal-state dependent and the policy can defer witness choice; prove by constructing two policies and exact cost calculations.
H10.3: Under a fixed verifier and trusted sensing protocol, robust physical validity requires an information budget lower bound beyond the ordinary indistinguishability bound. Falsify by applying standard hypothesis testing / decision-tree arguments (E019,E031) or by exhibiting a universally valid edit.
These are research prompts, not claimed discoveries. No complexity class or asymptotic theorem is asserted.

## 6. Prior-art reduction table
| Target | Direct competitor | Reduction attempt / unresolved obstruction |
|---|---|---|
| sensing + graph construction | E029 Singla | Edge cost probes and spanning-tree selection already cover broad objective; only a *nonseparable proof cost* could remain |
| decision-dependent observation + network design | E050 Omer/Poss/Rougier | Their polyhedral uncertainty and bounded-description assumptions give compact MILP; must show a sharply different assumption or separation |
| joint sensor placement and routing | E023 Paradiso et al. | Application overlap direct; no novelty merely from co-design |
| stochastic structural repair | E038 Rysz et al. | Vertex addition/removal under random edge changes established |
| sensing while repairing | E039 Tootaghaj et al. | Interleaving is established |
| proof-producing optimal planning | E052 Dold et al. | Independent planning optimality certificates established; cannot claim certification new |
| general adaptive policies | E017-E018 POMDP | Finite history policy trees already express full policy; only restricted complexity results possible |

## 7. Decision and next gate
P10.1-P10.4 are elementary or classical baseline propositions. No original theorem established. The most promising *falsifiable* direction is H10.2, but even a witness-cost-induced policy reversal may be an elementary instance of decision-theoretic cost accounting; novelty must be checked separately. Prompt 11 should adversarially try to disprove H10.1-H10.3, seek exact proof systems and non-artificial cost models, and stop with NO-GO if only known effects remain.
