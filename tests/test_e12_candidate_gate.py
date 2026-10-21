"""E12 regression and candidate-rejection contracts (not an originality test)."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from physical_graph import Budget, Edge, State
from exact_oracle import Problem, solve
from baselines import evaluate, NAMES

def two_serial(repairs):
    edges_a=(Edge("left","s","u",False),Edge("right","u","t",True))
    edges_b=(Edge("left","s","u",True),Edge("right","u","t",False))
    args=(frozenset({"s","t"}),frozenset({("s","t")}),Budget(repairs,0,repairs))
    return Problem((State(edges_a,*args),State(edges_b,*args)),(),("left","right"),(("s","t"),),repairs)

class E12Contracts(unittest.TestCase):
    def test_horizon_terminal_success_is_recorded(self):
        # E11 previously returned before recording success at depth zero.
        p=two_serial(2)
        self.assertEqual(evaluate(p,"repair_first").success,Fraction(1))
        self.assertTrue(evaluate(p,"repair_first").robust)
    def test_one_repair_partial_success_is_recorded(self):
        p=two_serial(1)
        self.assertEqual(evaluate(p,"repair_first").success,Fraction(1,2))
    def test_baseline_bound_against_exact(self):
        for budget in (0,1,2):
            p=two_serial(budget)
            opt=solve(p)
            for name in NAMES:
                with self.subTest(budget=budget,name=name):
                    value=evaluate(p,name,seed=19)
                    self.assertLessEqual(value.success,opt.bayes)
                    self.assertLessEqual(value.repair_attempts,budget)
    def test_no_budget_cannot_repair(self):
        p=two_serial(0)
        for name in NAMES:
            self.assertEqual(evaluate(p,name).success,0)

if __name__=="__main__":
    unittest.main()
