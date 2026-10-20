"""E11 baseline contract tests. Execute with unittest discover from repository root."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from physical_graph import Budget, Edge, Probe, State, gate_failure
from exact_oracle import Problem, solve
from baselines import NAMES, evaluate

def two_faults(repairs=2,probes=1):
    a,full,_=gate_failure("left")
    b,_,_=gate_failure("right")
    from dataclasses import replace
    budget=Budget(repairs,probes,repairs+probes)
    return Problem((replace(a,budget=budget),replace(b,budget=budget)),
                   (full,),("left","right"),(("s","t"),),repairs+probes)

class BaselineContracts(unittest.TestCase):
    def test_every_baseline_matched_rights_and_oracle_bound(self):
        p=two_faults(2,1)
        oracle=solve(p)
        for name in NAMES:
            with self.subTest(name=name):
                v=evaluate(p,name)
                self.assertLessEqual(v.success,oracle.bayes)
                self.assertLessEqual(v.probe_attempts,1)
                self.assertLessEqual(v.repair_attempts,2)
    def test_no_repair_no_success(self):
        p=two_faults(0,1)
        for name in NAMES:
            self.assertEqual(evaluate(p,name).success,0)
    def test_bruteforce_repair_first(self):
        p=two_faults(2,0)
        v=evaluate(p,"repair_first")
        self.assertEqual(v.success,1)
        self.assertTrue(v.robust)
    def test_one_repair_upper_bound(self):
        p=two_faults(1,1)
        for name in NAMES:
            self.assertLessEqual(evaluate(p,name).success,Fraction(1,2))
    def test_seed_repeatable(self):
        p=two_faults()
        self.assertEqual(evaluate(p,"random",seed=19),evaluate(p,"random",seed=19))
    def test_unknown_baseline_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(two_faults(),"HEC")
    def test_weighted_prior(self):
        p=two_faults(1,0)
        for name in NAMES:
            self.assertLessEqual(evaluate(p,name,(Fraction(3,4),Fraction(1,4))).success,Fraction(3,4))

if __name__=="__main__": unittest.main()
