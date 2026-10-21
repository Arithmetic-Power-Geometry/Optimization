import unittest
from fractions import Fraction
from network_repair import Instance, Probe, exact_oracle, myopic_policy, unlocked_three, path_family, eligible, outcomes, success

class P03Contracts(unittest.TestCase):
    def test_path_bound(self):
        for n in range(2, 9):
            self.assertEqual(exact_oracle(path_family(n))[0], Fraction(1, n))
    def test_gate_unlocks_informative_probe(self):
        x = unlocked_three()
        ids = (0, 1, 2)
        self.assertFalse(eligible(x, ids, frozenset(), x.probes[0]))
        self.assertTrue(eligible(x, ids, frozenset(("g",)), x.probes[0]))
        self.assertEqual(len(outcomes(x, ids, frozenset(("g",)), x.probes[0])), 2)
    def test_gate_optimal_vs_myopic(self):
        x = unlocked_three()
        value, first, _ = exact_oracle(x)
        self.assertEqual(value, Fraction(1))
        self.assertEqual(first, ("repair", "g"))
        self.assertEqual(myopic_policy(x), Fraction(2, 3))
    def test_universal_repair(self):
        x = Instance(("a",), ("a",), (("a",), ()), (), 1, 0)
        self.assertEqual(exact_oracle(x)[0], Fraction(1))
    def test_zero_budget(self):
        x = Instance(("a",), ("a",), (("a",), ()), (), 0, 0)
        self.assertEqual(exact_oracle(x)[0], Fraction(1, 2))
    def test_indistinguishable_two_edges(self):
        x = path_family(2)
        self.assertEqual(exact_oracle(x)[0], Fraction(1, 2))
    def test_budget_and_access(self):
        x = unlocked_three()
        y = Instance(x.edges, x.service, x.worlds, x.probes, 1, 2)
        self.assertEqual(exact_oracle(y)[0], Fraction(1, 3))
    def test_no_probe_benefit(self):
        x = Instance(("a", "b"), ("a", "b"), (("a",), ("b",)),
                     (Probe("whole", ("a", "b")),), 1, 1)
        self.assertEqual(exact_oracle(x)[0], Fraction(1, 2))
    def test_permutation_invariance(self):
        x = unlocked_three()
        y = Instance(x.edges, x.service, tuple(reversed(x.worlds)), x.probes, 2, 2)
        self.assertEqual(exact_oracle(x)[0], exact_oracle(y)[0])
    def test_no_overclaim_on_repair_interleaving(self):
        x = Instance(("a", "b"), ("a", "b"), (("a",), ("b",)), (), 2, 0)
        self.assertEqual(exact_oracle(x)[0], Fraction(1))
        self.assertEqual(myopic_policy(x), Fraction(1))

if __name__ == "__main__":
    unittest.main()
