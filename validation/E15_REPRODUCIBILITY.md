# E15 reproducibility and independent verification
Run from repository root (Python 3.11+ standard library only):
```sh
python extension/data/e15_validate.py
```
This verifies the raw GraphML source Git blob hashes, undirected topology and absence of self-loops/parallel edges, then regenerates and byte-compares every cleaned node and edge CSV with manifest Git blob SHA-1. Expected verified graph counts: Abilene 11/14, Geant2012 40/61, Arpanet19728 29/32. **This Python command was not executed during E15**; expected outputs are specifications, not measured Python test results.

Acquisition method: GitHub repository file API, `mroughan/InternetTopologyZoo` raw graphml paths. The author's CC BY 4.0 LICENSE was fetched and reviewed. Compare source Git blob SHA to the copied `extension/data/E15_raw` blob; identical Git blobs establish byte-identical source content. Do not confuse Git blob SHA-1 with bare SHA-1 of file contents.

Cleaning contract: UTF-8 XML GraphML, undirected only; node IDs preserved and sorted numerically; edge endpoints ordered numerically and sorted; reject duplicate IDs, loops, parallel undirected edges and dangling endpoints; retain original files and metadata. No synthetic failures inserted at acquisition stage. For E16, use declared synthetic-failure seeds and document service demand, probe access, budgets and any graph-component restrictions.
