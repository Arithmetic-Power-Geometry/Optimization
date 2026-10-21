"""E15 deterministic GraphML -> node/edge CSV verifier; Python stdlib only.
Run: python extension/data/e15_validate.py
Verifies frozen source bytes via Git blob SHA-1 and reproduces cleaned CSV.
"""
from pathlib import Path
import csv
import hashlib
import io
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "E15_TOPOLOGY_MANIFEST.json"

def blob_sha(raw):
    header = b"blob " + str(len(raw)).encode("ascii") + b"\x00"
    return hashlib.sha1(header + raw).hexdigest()

def graph_clean(raw):
    root = ET.fromstring(raw)
    ns = {"g": "http://graphml.graphdrawing.org/xmlns"}
    graph = root.find("g:graph", ns)
    if graph is None or graph.attrib.get("edgedefault") != "undirected":
        raise ValueError("expected undirected GraphML")
    nodes = [x.attrib["id"] for x in graph.findall("g:node", ns)]
    if len(set(nodes)) != len(nodes) or not nodes:
        raise ValueError("duplicate or absent nodes")
    node_set = set(nodes)
    pairs = []
    seen = set()
    for edge in graph.findall("g:edge", ns):
        a, b = edge.attrib["source"], edge.attrib["target"]
        if a not in node_set or b not in node_set or a == b:
            raise ValueError("invalid edge endpoint or loop")
        pair = tuple(sorted((a, b), key=int))
        if pair in seen:
            raise ValueError("parallel edge: excluded from this simple-graph benchmark")
        seen.add(pair)
        pairs.append(pair)
    nodes.sort(key=int)
    pairs.sort(key=lambda ab: (int(ab[0]), int(ab[1])))
    node_csv = "node_id\n" + "".join(n+"\n" for n in nodes)
    edge_csv = "u,v\n" + "".join(a+","+b+"\n" for a,b in pairs)
    return nodes, pairs, node_csv.encode(), edge_csv.encode()

def verify():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["status"] == "ACQUIRED_VERIFIED"
    for entry in manifest["topologies"]:
        name = entry["id"]
        raw = (ROOT / "E15_raw" / (name+".graphml")).read_bytes()
        assert blob_sha(raw) == entry["source_git_blob_sha1"], name
        nodes, pairs, node_bytes, edge_bytes = graph_clean(raw)
        assert len(nodes) == entry["nodes"] and len(pairs) == entry["edges"]
        for suffix, expected in [("nodes", node_bytes), ("edges", edge_bytes)]:
            path = ROOT / "E15_clean" / (name+"."+suffix+".csv")
            assert path.read_bytes() == expected, str(path)
            assert blob_sha(expected) == entry["clean_"+suffix+"_git_blob_sha1"]
        print(name, len(nodes), len(pairs), "VERIFIED")
    print("E15 verified",len(manifest["topologies"]),"topologies")

if __name__ == "__main__":
    verify()
