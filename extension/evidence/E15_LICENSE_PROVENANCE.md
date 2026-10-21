# E15 — Licensing, acquisition, provenance, and topology limits
Date: 2026-10-21.

## Acquired and verified: Internet Topology Zoo
Source: https://github.com/mroughan/InternetTopologyZoo
Original work: Knight, S., Nguyen, H. X., Falkner, N., Bowden, R., & Roughan, M. (2011). The Internet Topology Zoo. *IEEE Journal on Selected Areas in Communications*, 29(9), 1765–1775. https://doi.org/10.1109/JSAC.2011.111002.
Archive license: Creative Commons Attribution 4.0 International (CC BY 4.0), original https://github.com/mroughan/InternetTopologyZoo/blob/main/LICENSE . The license was independently fetched from the author's archive and its header checked. Attribution, license link, and change indication required; no implied author endorsement.

Acquired from the original public archive via GitHub repository file API (not from a secondary reconstruction):
- `graphml/Abilene.graphml` — 11 nodes, 14 undirected edges; source Git blob SHA-1 `330c97a349a80a8f3e1c825072e45ca503d0eab7`.
- `graphml/Geant2012.graphml` — 40 nodes, 61 undirected edges; source Git blob SHA-1 `a61eb6798dae90a000ed2f64a43241a075b05ed3`.
- `graphml/Arpanet19728.graphml` — 29 nodes, 32 undirected edges; source Git blob SHA-1 `50b7f8d9802f1bd396a5a1a506ff4cd3caf7f3d0`.

Original bytes preserved in `extension/data/E15_raw/`; cleaned node and edge CSV in `extension/data/E15_clean/`. Processing: GraphML node IDs preserved, undirected edges endpoint-normalized and sorted; GraphML node/edge annotations excluded from cleaned CSV but preserved in original source. All three are connected, with no self-loops, parallel undirected edges, missing endpoints, or isolated nodes under the selected parser. These are historical curated topology structures; they do not encode contemporary failures, true outage labels, actual repair permissions or monitoring access. Future injected failures must be labeled **synthetic faults on real/historical topologies**. A cleaned graph is not a measurement of an actual operating network.

## CAIDA ITDK — not acquired
Official dataset: https://www.caida.org/catalog/datasets/internet-topology-data-kit/
Release page: https://www.caida.org/catalog/datasets/internet-topology-data-kit/release-2026-03/
CAIDA distinguishes older public releases under an Acceptable Use Agreement from recent releases requiring approval. The terms require dataset-specific attribution and reporting resulting publications to CAIDA. No user-approved AUA/access request, authenticated download, release archive, or actual ITDK content was obtained in E15. Accordingly there is **no CAIDA release SHA, no CAIDA cleaned graph, and no CAIDA experiment**. Do not mirror or redistribute CAIDA content before confirming license permissions.

## Independent provenance checks
All raw file Git blob hashes were compared with the original mroughan archive and matched exactly after commit to the target repository. Cleaned CSV Git blob hashes and counts are frozen in E15_TOPOLOGY_MANIFEST.json. Git blob SHA-1 is a content identifier including the Git blob header, not plain SHA-1 or SHA-256 of raw file bytes. Standard-library verifier `extension/data/e15_validate.py` reproduces and checks cleaned files; it has been committed but **was not executed in the local Python runtime in this stage**. The GitHub-connector-based cross-file checks were executed.
