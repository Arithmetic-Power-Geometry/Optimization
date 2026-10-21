"""E10 golden fixtures: independent mask enumeration must agree with DP oracle."""
import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from physical_graph import Edge, State, Budget, Probe, gate_failure
from exact_oracle import Problem, solve
from independent_checker import check

def series(n, repair_budget, probe_budget):
    states = []
    for j in range(n):
        edges = tuple(Edge(f'e{i}',f'v{i}',f'v{i+1}',i != j) for i in range(n))
        states.append(State(edges,frozenset({'v0',f'v{n}'}),frozenset({('v0',f'v{n}')}),Budget(repair_budget,probe_budget,repair_budget+probe_budget)))
    p = Probe('full',tuple(f'v{i}' for i in range(n+1)),tuple(f'e{i}' for i in range(n)))
    return Problem(tuple(states),(p,),tuple(f'e{i}' for i in range(n)),(('v0',f'v{n}'),),repair_budget+probe_budget)

class ExactTests(unittest.TestCase):
    def compare(self, problem, weights=None):
        dp=solve(problem,weights)
        brute=check(problem,weights)
        self.assertEqual((dp.robust,dp.bayes),brute[:2])
        return dp
    def test_n_edge_one_over_n(self):
        for n in (2,3,4,5):
            p=series(n,1,1)
            r=self.compare(p)
            self.assertFalse(r.robust)
            self.assertEqual(r.bayes,Fraction(1,n))
    def test_all_repairs_robust(self):
        for n in (2,3,4):
            r=self.compare(series(n,n,0))
            self.assertTrue(r.robust)
            self.assertEqual(r.bayes,1)
    def test_no_budget(self):
        r=self.compare(series(3,0,0))
        self.assertFalse(r.robust)
        self.assertEqual(r.bayes,0)
    def test_gate_two_repairs(self):
        a,_,_=gate_failure('left')
        b,_,_=gate_failure('right')
        p=Problem((a,b),(),('left','right','gate'),(('s','t'),),2)
        self.assertTrue(self.compare(p).robust)
    def test_gate_one_repair(self):
        a,_,_=gate_failure('left')
        b,_,_=gate_failure('right')
        from dataclasses import replace
        a=replace(a,budget=Budget(1,0,1)); b=replace(b,budget=Budget(1,0,1))
        p=Problem((a,b),(),('left','right','gate'),(('s','t'),),1)
        self.assertEqual(self.compare(p).bayes,Fraction(1,2))
    def test_prior_weights(self):
        p=series(2,1,0)
        self.assertEqual(self.compare(p,(Fraction(3,4),Fraction(1,4))).bayes,Fraction(3,4))
    def test_admissibility_not_down(self):
        p=series(2,1,1)
        bad=Probe('bad',('v0','v1'),('e0',))
        q=Problem(p.hypotheses,(bad,),p.repairs,p.demands,p.horizon)
        self.assertEqual(self.compare(q).bayes,Fraction(1,2))
    def test_empty_or_duplicate(self):
        p=series(2,1,0)
        with self.assertRaises(ValueError): Problem((),(),(),(),1)
        with self.assertRaises(ValueError): Problem((p.hypotheses[0],)*2,(),(),(),1)

if __name__=='__main__': unittest.main()
