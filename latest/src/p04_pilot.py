"""P04 synthetic abstract-world pilot. No graph-path, outage or packet validation."""
import csv, json, random, statistics
from pathlib import Path
from fractions import Fraction
from network_repair import Instance, Probe, exact_oracle, myopic_policy, unlocked_three, path_family

def run(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    rows = []
    for seed in range(30):
        rng = random.Random(seed)
        n = rng.choice((3, 4, 5))
        edges = tuple(chr(97+i) for i in range(n))
        faults = tuple(rng.sample(edges, 3))
        worlds = tuple(("g", e) for e in faults)
        probes = tuple(Probe("test_"+e, (e,), ("g",)) for e in faults[:-1])
        x = Instance(("g",)+edges, edges, worlds, probes, 2, 2)
        optimum, first, cache = exact_oracle(x)
        greedy = myopic_policy(x)
        rows.append(dict(seed=seed, service_edges=n, oracle=str(optimum),
                         myopic=str(greedy), gap=str(optimum-greedy),
                         oracle_states=cache.currsize, first_action=":".join(first)))
    with (out/"pilot_raw.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    gaps = [float(Fraction(r["gap"])) for r in rows]
    rng = random.Random(20261021)
    boots = sorted(statistics.mean(rng.choices(gaps, k=len(gaps))) for _ in range(5000))
    x = unlocked_three()
    negative = {f"uninformative_path_n{n}":str(exact_oracle(path_family(n))[0]) for n in (2,3,5,8)}
    negative.update(gate_optimum=str(exact_oracle(x)[0]), gate_myopic=str(myopic_policy(x)),
                    no_probe_budget=str(exact_oracle(Instance(x.edges,x.service,x.worlds,x.probes,2,0))[0]),
                    repair_all_service_edges=str(exact_oracle(Instance(x.edges,x.service,x.worlds,x.probes,3,0))[0]))
    summary = dict(n_scenarios=len(rows), scenario_kind="synthetic abstract worlds, not verified graph routes",
                   oracle_mean=statistics.mean(float(Fraction(r["oracle"])) for r in rows),
                   myopic_mean=statistics.mean(float(Fraction(r["myopic"])) for r in rows),
                   paired_mean_gap=statistics.mean(gaps),
                   bootstrap_95_descriptive=[boots[125], boots[4874]],
                   all_scenarios_positive_gap=all(g>0 for g in gaps),
                   seed_list=list(range(30)), negative_controls=negative,
                   limitations=["No independent topology data","No actual packet simulations",
                                "No faithful HEC baseline","No cost/downtime/noise model",
                                "30 constructed worlds are not independent outages"])
    (out/"pilot_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    return summary

if __name__ == "__main__":
    print(json.dumps(run(Path(__file__).resolve().parents[1]/"results"), indent=2))
