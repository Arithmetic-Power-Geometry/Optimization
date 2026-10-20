"""E14 synthetic exact-small experiment, deterministic, Python >=3.11.
Run: python extension/experiments/e14_exact_small.py --output extension/results/E14_EXACT_SMALL.csv
"""
import argparse
import csv
import hashlib
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from fractions import Fraction
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from physical_graph import Edge, State, Budget, Probe, gate_failure
from exact_oracle import Problem, solve
from independent_checker import check
from baselines import NAMES, evaluate

COLUMNS = ['family','n','repair_budget','probe_budget','policy','success_exact','robust','probe_attempts_exact','repair_attempts_exact','gap_to_oracle_exact','oracle_nodes','elapsed_ns','status']

def series_problem(n, repairs, probes):
    states = []
    for fault in range(n):
        edges = tuple(Edge(f'e{i}', f'v{i}', f'v{i+1}', i != fault) for i in range(n))
        states.append(State(edges, frozenset({'v0', f'v{n}'}), frozenset({('v0', f'v{n}')}), Budget(repairs, probes, repairs + probes)))
    path = Probe('full', tuple(f'v{i}' for i in range(n+1)), tuple(f'e{i}' for i in range(n)))
    return Problem(tuple(states), (path,), tuple(f'e{i}' for i in range(n)), (('v0', f'v{n}'),), repairs+probes)

def gate_problem(repairs, probes):
    a, p, _ = gate_failure('left')
    b, _, _ = gate_failure('right')
    budget = Budget(repairs, probes, repairs + probes)
    return Problem((replace(a,budget=budget), replace(b,budget=budget)), (p,), ('left','right','gate'), (('s','t'),), repairs+probes)

def rows():
    for family, n, problem in (
        [('series', n, series_problem(n, r, p)) for n in (2,3,4,5) for r in (0,1,2) for p in (0,1)]
        + [('gate', 2, gate_problem(r,p)) for r in (0,1,2) for p in (0,1)]
    ):
        start=time.perf_counter_ns()
        optimum=solve(problem)
        oracle_ns=time.perf_counter_ns()-start
        independently=check(problem)
        assert (optimum.robust,optimum.bayes)==independently[:2], (family,n,problem)
        yield [family,n,problem.hypotheses[0].budget.repairs,problem.hypotheses[0].budget.probes,'exact_oracle',str(optimum.bayes),str(optimum.robust).lower(),'NA','NA','0',optimum.nodes,oracle_ns,'EXECUTED_VERIFIED']
        for policy in NAMES:
            start=time.perf_counter_ns()
            result=evaluate(problem,policy,seed=20261020)
            elapsed=time.perf_counter_ns()-start
            assert result.success<=optimum.bayes, (family,n,policy,result.success,optimum.bayes)
            assert result.repair_attempts<=problem.hypotheses[0].budget.repairs
            assert result.probe_attempts<=problem.hypotheses[0].budget.probes
            yield [family,n,problem.hypotheses[0].budget.repairs,problem.hypotheses[0].budget.probes,policy,str(result.success),str(result.robust).lower(),str(result.probe_attempts),str(result.repair_attempts),str(optimum.bayes-result.success),optimum.nodes,elapsed,'EXECUTED_VERIFIED']

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=ROOT/'results/E14_EXACT_SMALL.csv')
    args=parser.parse_args()
    data=list(rows())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f,lineterminator='\n');writer.writerow(COLUMNS);writer.writerows(data)
    blob=args.output.read_bytes()
    print(json.dumps({'rows':len(data),'instances':len(data)//6,'sha256':hashlib.sha256(blob).hexdigest(),'file':str(args.output),'oracle_verified':True},sort_keys=True))

if __name__=='__main__':main()
