"""E16 deterministic reproduction of matched *synthetic* single-path faults.
Python 3.11+ standard library. This script is committed but NOT PYTHON-EXECUTED
in E16; recorded episode CSV and bootstrap JSON were produced by an
independent JavaScript execution over GitHub-fetched, hash-verified graph CSVs.
"""
from pathlib import Path
import csv
import json
import sys
from collections import deque

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))
from e15_validate import verify

NAMES = ("exact_uniform_oracle", "repair_first", "diagnosis_first",
         "cost_sensitive_greedy", "drd_region_greedy", "random")
GRAPHS = ("Abilene", "Geant2012", "Arpanet19728")
FIELDS = ("topology,topology_index,seed,monitor_s,monitor_t,path_edges,"
          "fault_index,failed_edge,repair_budget,probe_budget,time_budget,"
          "policy,repaired_edges,service_success,oracle_expected_success,"
          "fault_label,status").split(",")

def edges_for(name):
    with (ROOT/"data"/"E15_clean"/(name+".edges.csv")).open(newline="") as f:
        return [(int(r["u"]),int(r["v"])) for r in csv.DictReader(f)]

def longest_shortest_path(edges):
    adj = {}
    for u,v in edges:
        adj.setdefault(u,[]).append(v)
        adj.setdefault(v,[]).append(u)
    for v in adj.values():
        v.sort()
    best = []
    for src in sorted(adj):
        queue=deque([[src]])
        seen={src}
        while queue:
            path=queue.popleft()
            if len(path)>len(best):
                best=path
            for nxt in adj[path[-1]]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(path+[nxt])
    return best, adj

def shuffled_indices(n,seed,topo_index):
    arr=list(range(n))
    x=(seed+(topo_index+1)*2654435761)&0xffffffff
    for j in range(n-1,0,-1):
        x=(1664525*x+1013904223)&0xffffffff
        k=x%(j+1)
        arr[j],arr[k]=arr[k],arr[j]
    return arr

def episodes():
    seeds=json.loads((ROOT/"experiments"/"E13_MANIFEST.json").read_text())["paired_seeds"]
    for ti,name in enumerate(GRAPHS):
        path,adj=longest_shortest_path(edges_for(name))
        pe=[f"{min(u,v)}-{max(u,v)}" for u,v in zip(path,path[1:])]
        score=[len(adj[u])+len(adj[v]) for u,v in zip(path,path[1:])]
        n=len(pe)
        indices=list(range(n))
        policies={
            "exact_uniform_oracle":indices,
            "repair_first":sorted(indices,key=lambda i:pe[i]),
            "diagnosis_first":sorted(indices,key=lambda i:pe[i],reverse=True),
            "cost_sensitive_greedy":sorted(indices,key=lambda i:(-score[i],i)),
            "drd_region_greedy":sorted(indices,key=lambda i:(score[i],i))
        }
        for si,seed in enumerate(seeds):
            # Balanced deterministic schedule: NOT an independent random draw.
            fault=(si+ti)%n
            rand=shuffled_indices(n,seed,ti)
            for budget in (1,2):
                for policy in NAMES:
                    order=rand if policy=="random" else policies[policy]
                    repaired=order[:min(budget,n)]
                    yield dict(zip(FIELDS,[
                        name,ti,seed,path[0],path[-1],n,fault,pe[fault],
                        budget,1,budget+1,policy,";".join(pe[i] for i in repaired),
                        int(fault in repaired),f"{min(budget,n)}/{n}",
                        "SYNTHETIC_SINGLE_EDGE_FAILURE","EXECUTED_JS_EXACT_GRAPH"
                    ]))

def main():
    verify() # Mandatory E15 byte-level and GraphML checks before experiments.
    rows=list(episodes())
    assert len(rows)==720
    path=ROOT/"results"/"E16_MATCHED_EPISODES.csv"
    with path.open(newline="") as f:
        actual=list(csv.DictReader(f))
    assert [{k:str(v) for k,v in row.items()} for row in rows]==actual
    print("E16 verified",len(rows),"recorded matched episodes")

if __name__=="__main__":
    main()
