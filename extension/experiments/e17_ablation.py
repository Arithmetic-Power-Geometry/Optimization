"""E17 restricted ablation reproduction; requires full checkout. NOT executed in E17."""
from pathlib import Path
import csv
import json
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"data"))
sys.path.insert(0,str(ROOT/"experiments"))
from e15_validate import verify
from e16_matched import edges_for,longest_shortest_path

SCENARIOS=("baseline","no_adaptive_probes","no_post_repair_probes","no_decision_sufficiency",
           "heterogeneous_costs","noisy_full_path","correlated_failures","shifted_prior")
NAMES=("Abilene","Geant2012","Arpanet19728")
FIELDS=("topology,seed,seed_index,repair_budget,scenario,path_length,failed_edge_indices,"
        "repaired_edge_indices,repair_cost,probe_budget,synthetic_observation_flip,"
        "service_success,classification,failure_provenance,execution").split(",")

def episodes():
    seeds=json.loads((ROOT/"experiments"/"E13_MANIFEST.json").read_text())["paired_seeds"]
    for ti,name in enumerate(NAMES):
        path,_=longest_shortest_path(edges_for(name))
        L=len(path)-1
        for si,seed in enumerate(seeds):
            fault=(si+ti)%L
            shifted=0 if si<16 else 1+(si%max(1,L-1))
            for budget in (1,2):
                for scenario in SCENARIOS:
                    failures=[fault,(fault+1)%L] if scenario=="correlated_failures" else [
                        shifted if scenario=="shifted_prior" else fault]
                    repairs=[]
                    cost=0
                    for j in range(L):
                        c=(2 if j%2==0 else 1) if scenario=="heterogeneous_costs" else 1
                        if cost+c<=budget:
                            cost+=c
                            repairs.append(j)
                    success=int(all(i in repairs for i in failures))
                    flip=int(scenario=="noisy_full_path" and si%5==0)
                    kind="MODEL_CHANGE" if scenario in (
                        "heterogeneous_costs","correlated_failures","noisy_full_path",
                        "shifted_prior") else "POLICY_ABLATION"
                    yield dict(zip(FIELDS,[name,seed,si,budget,scenario,L,
                        ";".join(map(str,failures)),";".join(map(str,repairs)),
                        cost,1,flip,success,kind,"SYNTHETIC","EXECUTED_JS"]))

def main():
    verify()
    rows=list(episodes())
    assert len(rows)==960
    with (ROOT/"results"/"E17_ABLATION_EPISODES.csv").open(newline="") as f:
        frozen=list(csv.DictReader(f))
    assert [{k:str(v) for k,v in row.items()} for row in rows]==frozen
    print("E17 reproducibility passed",len(rows),"rows")

if __name__=="__main__":
    main()
