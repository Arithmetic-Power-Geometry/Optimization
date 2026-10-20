# Prompt 09 — bibliography and novelty gate (2026-10-20)

## Scope and audit method
Fetched cumulative GitHub registry and BibTeX (55 entries each). Checked stable ID and citation-key uniqueness, manually reviewed every registry line for obvious incomplete fields, matched key primary metadata against publisher and institutional records for high-risk sources. Not an exhaustive DOI-resolution test for all 55 or proof-by-proof full-text verification. Keep that distinction explicit.

## Confirmed corrections
- E038: Maciej Rysz, Pavlo A. Krokhmal, Eduardo L. Pasiliao; Wiley Networks 69(2):189–204 (2017), DOI 10.1002/net.21727. Strong prior art: reparable structures via vertex addition/removal after observed stochastic edge changes.
- E039: Diman Zad Tootaghaj et al., 2017 IFIP Networking Conference, pp. 1–9, DOI 10.23919/IFIPNetworking.2017.8264831. Strong prior art: repair actions progressively reveal uncertain damage.
- E048: Anderson et al. authors verified by Princeton university record; POPL 2014 pp. 113–126.
- E009: PMLR 267:1864–1886, four authors verified by PMLR primary proceedings.
- E050: Omer, Poss, Rougier, OJMO volume 5 article 5 (2024), DOI 10.5802/ojmo.33; compact MILP only when number of non-bound uncertainty-polytope constraints is constant.
- E052: ICAPS 2025 vol. 35 pp. 54–63, DOI 10.1609/icaps.v35i1.36101; lower-bound proof logs for planning.
- E053: Automatica volume 185 article 112798, DOI 10.1016/j.automatica.2025.112798; Oxford archive online publication 2025-11-19, while volume assigned 2026. Preserve issue-year convention with note.
- E040: Original DOI 10.1007/978-3-030-25543-5_18 could not be independently tied to claimed title and authors. QUARANTINED, not citeable pending publisher check.

## Evidence counts
55 registry IDs, 55 BibTeX keys, no duplicate IDs/keys detected in final readback. 54 provisional retained records plus one quarantined E040. These counts do NOT imply all 54 have independently verified complete bibliographies.

## Novelty decision
NO-GO for a general new optimization paradigm: DDID spanning trees (E050), paid stochastic probing (E029), sensing/routing (E023), stochastic structural repair (E038), sensing-and-repair (E039), proof-producing optimal planning (E052) already cover broad ingredients.
CONDITIONAL GO for an adversarial restricted-model theorem-search: explicitly model hidden-state sensing, graph edits, proof language, witness generation/checking and compare total cost with matched nonadaptive baseline. This is a research question, not an established discovery or a proved theorem.

## Counterexamples and proof obligations
- Two independent bits, XOR target: either alone has zero value; both together have positive value. General value of information not submodular.
- Adding one bridge connects two components: graph creation and a path witness are standard, not novel.
- Witness valid for observed graph need not prove truth for hidden physical network; distinguish universal vs PAC vs encoded-instance guarantees.
- Finite policy trees can be encoded as POMDPs; seek complexity/approximation lower bounds, not expressive novelty.
- Proof-system choice matters for certificate length; no universal lower bound without fixed representation.

## Outstanding QA
E016 full author list, E040 publisher association, remaining metadata and theorem-level audits. Literature coverage is targeted rather than a systematic review. Bibliography freeze is *conditional*, with unresolved entries flagged.

## Decision for Prompt 10
Permit formal definitions and falsification attempts only, not an assertion of novelty. Stop and ask user permission. No software, experiments or manuscript.
