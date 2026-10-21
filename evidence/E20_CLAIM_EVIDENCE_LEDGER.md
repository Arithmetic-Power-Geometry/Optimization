# E20 frozen claim-to-evidence ledger — 2026-10-21

| Claim ID | Claim | Evidence | Execution / replication | Decision |
|---|---|---|---|---|
| C01 | E09–E12 finite-model unit tests 31/31 pass | E14_TEST_EXECUTION.json; E09–E12 source/tests | E14 local Python 3.13.5 run; E20 no fresh clean checkout | HISTORICAL EXECUTED, NOT INDEPENDENTLY RE-RUN IN E20 |
| C02 | E10 exact oracle matches independent checker on E14 toys | E14_RAW_COMPACT.csv, E14 report | E14 executed; E20 recalculated 180 rows and policy means | RESTRICTED VERIFIED ARITHMETIC; no new oracle run |
| C03 | E14 random policy has three 1/2 gaps, nonrandom ties | E14_RAW_COMPACT.csv | E20 recomputed exact fractions and gaps | VERIFIED FROM FROZEN RAW CSV |
| C04 | Three Internet Topology Zoo historical graph structures acquired | E15_TOPOLOGY_MANIFEST.json, raw GraphML, clean CSV | E15–E17 GitHub source/blob/clean checks; E20 Python validator not run | VERIFIED SOURCE IDENTITY, PYTHON GATE OPEN |
| C05 | E16 has 720 deterministic synthetic-failure policy rows | E16_MATCHED_EPISODES.csv | E20 independently recomputed service indicator, budget and 120 matched six-policy groups | VERIFIED CSV INTEGRITY; NOT PYTHON REPRODUCTION |
| C06 | E16 paired bootstrap reports 15 descriptive intervals | E16_PAIRED_BOOTSTRAP.json | E20 recomputed 15 paired means, NOT 2000 bootstrap intervals | MEANS VERIFIED; INTERVALS NOT INDEPENDENTLY REGENERATED |
| C07 | E17 has 960 sensitivity rows and 24 group summaries | E17_ABLATION_EPISODES.csv, E17_ABLATION_SUMMARY.json | E20 recomputed success, repair cost and all 24 groups | VERIFIED CSV INTEGRITY; NOT PYTHON REPRODUCTION |
| C08 | E17 no-op probe ablations show no differences | E17_FAILURE_MODES.md, E17 raw | No probe used; noise flip ignored | TRIVIAL NO-EFFECT; NOT EVIDENCE OF ROBUSTNESS |
| C09 | E18 Mininet validation | E18_ENVIRONMENT_BLOCKER.json | Mininet/OVS absent; no runs | BLOCKED; ZERO MEASUREMENTS |
| C10 | E19 ns-3 packet validation | E19_ENVIRONMENT_BLOCKER.json | ns-3 absent; no runs | BLOCKED; ZERO MEASUREMENTS |
| C11 | Proposed repair-dependent observability theorem | E06 counterexample, E08 audit | E06.P2 false and retracted | REJECTED; DO NOT CITE AS PROVED |
| C12 | New superior optimization algorithm | E03/E08/E12 novelty audits; E14–E17 results | Candidate duplicate; no superiority or direct HEC comparator | NO-GO |
| C13 | Original eight-page manuscript source frozen | E01 source inventory | Original byte-identical TeX/PDF absent from GitHub | BLOCKED |
| C14 | CAIDA ITDK real network graph acquired | E15 provenance | AUA/access not completed | NOT ACQUIRED |
| C15 | E13 20-seed, 10k bootstrap Holm protocol executed | E13_MANIFEST.json | Only restricted E16 2000 descriptive bootstrap; no Holm | NOT EXECUTED |
| C16 | Active CI verifies extension | E13 staged CI | Workflow outside extension not activated | NOT EXECUTED |
| C17 | Prior-art novelty of decision-region sufficiency | Javdani et al. AISTATS 2014 PMLR 33, https://proceedings.mlr.press/v33/javdani14.html | Primary published DRD/HEC confirms overlap, decision sufficiency, HEC greedy | COLLISION; NO-GO |
| C18 | Real repair event / live packet measurement | E15–E19 evidence | All failures synthetically injected; no packet emulator run | UNSUPPORTED |

**Freeze policy:** Keep original raw results immutable. This ledger is an evidence audit, not a new theorem, successful replication of every stage, or manuscript-ready claim. E21 must not silently upgrade any BLOCKED or NOT EXECUTED entry.
