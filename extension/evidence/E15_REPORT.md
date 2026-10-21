# E15 — Public Graph Benchmark Acquisition
Date: 2026-10-21

## Actual acquisition
Successfully fetched the author's Internet Topology Zoo CC BY 4.0 license and three original GraphML topology files via the GitHub repository API. Committed the exact original GraphML bytes to extension/data/E15_raw/, and deterministic canonical simple undirected node and edge CSVs to extension/data/E15_clean/. The original archive blob hashes matched target repository blobs after independent re-fetch. Cleaned files were independently re-read and matched the node/edge parsing and manifest checks. The three graphs have 11/14, 40/61, and 29/32 nodes/edges; all are connected with no loops, duplicate edges or missing endpoints.

## CAIDA gate
Official CAIDA ITDK access and acceptable-use conditions were checked. No authorized release download was available; **CAIDA acquisition is BLOCKED**. Do not fabricate CAIDA checksums or treat ITDK links as acquired data.

## Reproducibility
Committed E15_TOPOLOGY_MANIFEST.json with original/cleaned Git blob SHA-1 values, node/edge counts, connected component sizes and license/provenance; committed e15_validate.py standard-library GraphML cleaner and verifier. Original GraphML preserved to avoid information loss. Local container could not resolve raw.githubusercontent.com, but GitHub connector fetched actual source bytes successfully. Python validator NOT EXECUTED; connector-based independent content verification EXECUTED.

## Scientific decision
E15 PARTIAL GO for 3 verified Internet Topology Zoo graphs; CAIDA ITDK NO-GO until access/terms. E16 may use only acquired Zoo graphs and clearly synthetic injected failures, subject to explicit user authorization. No live outages, repair measurements, novel theorem or performance claims. E08 originality NO-GO and exact original manuscript-source BLOCKED persist. STOP before E16.
