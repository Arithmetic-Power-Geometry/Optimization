"""E09 deterministic contract tests. Run: python -m unittest discover -s extension/tests -v"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from physical_graph import (Budget, Edge, Probe, State, admissible, outcome, probe,
                            restore, service, common_admissible, series_failure, gate_failure)

class KernelTests(unittest.TestCase):
    def test_down_is_admissible(self):
        s,p=series_failure("left")
        self.assertTrue(admissible(s,p))
        self.assertEqual(outcome(s,p),"DOWN")
    def test_absent_edge_not_down(self):
        s,p=series_failure()
        q=Probe("bad",("s","u","t"),("left","missing"))
        self.assertFalse(admissible(s,q))
        with self.assertRaises(ValueError): outcome(s,q)
    def test_monitor_access(self):
        s,full,sub=gate_failure()
        self.assertFalse(admissible(s,sub))
        self.assertEqual(outcome(s,full),"DOWN")
        t=restore(s,"gate",enable_monitor="u",enable_pairs=frozenset({("s","u")}))
        self.assertTrue(admissible(t,sub))
        self.assertEqual(outcome(t,sub),"DOWN")
        self.assertEqual(t.budget.repairs,1)
    def test_failed_gate_costs_and_does_not_enable(self):
        s,_,sub=gate_failure()
        t=restore(s,"gate",success=False,enable_monitor="u",enable_pairs=frozenset({("s","u")}))
        self.assertFalse(admissible(t,sub))
        self.assertEqual(t.budget.repairs,1)
        with self.assertRaises(ValueError): restore(t,"gate")
    def test_probe_charged_once_and_history(self):
        s,p=series_failure()
        t,o=probe(s,p)
        self.assertEqual(o,"DOWN")
        self.assertEqual(t.budget.probes,1)
        self.assertEqual(t.budget.time,4)
        self.assertEqual(t.history[-1],("probe:full","DOWN"))
        self.assertEqual(s.budget.probes,2)
    def test_two_restorations_beat_false_e06_separation(self):
        for failed in ("left","right"):
            s,_,_=gate_failure(failed)
            t=restore(restore(s,"left"),"right")
            self.assertTrue(service(t,(("s","t"),)))
            self.assertEqual(t.budget.repairs,0)
    def test_one_restoration_not_robust(self):
        left,_,_=gate_failure("left")
        right,_,_=gate_failure("right")
        self.assertFalse(service(restore(left,"right"),(("s","t"),)))
        self.assertFalse(service(restore(right,"left"),(("s","t"),)))
    def test_hidden_state_not_leaked_by_admissibility(self):
        a,p=series_failure("left")
        b,_=series_failure("right")
        self.assertTrue(common_admissible((a,b),p))
        self.assertEqual(outcome(a,p),outcome(b,p))
    def test_budget_and_repeat(self):
        s,p=series_failure()
        with self.assertRaises(ValueError): Budget(-1,0,0)
        with self.assertRaises(ValueError): restore(s,"absent")
        t=restore(s,"left")
        with self.assertRaises(ValueError): restore(t,"left")
        with self.assertRaises(ValueError): probe(s,p,time_cost=6)
    def test_service_multi_demand(self):
        s,_=series_failure()
        self.assertFalse(service(s,(("s","t"),)))
        self.assertTrue(service(restore(s,"left"),(("s","t"),)))
    def test_csp_rejects_cycle(self):
        s=State((Edge("a","s","u"),Edge("b","u","s")),frozenset({"s"}),frozenset({("s","s")}),Budget(1,1,1))
        self.assertFalse(admissible(s,Probe("loop",("s","u","s"),("a","b"))))
        self.assertTrue(admissible(s,Probe("loop",("s","u","s"),("a","b"),"CAP")))
    def test_up_mode_requires_route_right(self):
        s,p=series_failure()
        q=Probe("route",p.nodes,p.edges,"UP")
        self.assertFalse(admissible(s,q))
        from dataclasses import replace
        self.assertTrue(admissible(replace(s,selected_routes=frozenset({"route"})),q))

if __name__ == "__main__":
    unittest.main()
