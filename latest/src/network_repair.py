"""Finite-state, deterministic, physically gated network repair model.

Proof-of-concept only: no claim of algorithmic originality or field validation.
A probe is an ordered edge-path; its access path must be operational in the
physical world for it to be available. To keep decisions feasible without
knowing the hidden world, a probe is admissible only when its access path is
operational in EVERY currently possible world. A test returns UP iff all
edges on its measurement path are operational in the actual world.
Repairs are irreversible and restore one edge across all possible worlds.
Terminal service succeeds iff every service edge is operational.
"""
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from typing import Tuple

@dataclass(frozen=True)
class Probe:
    name: str
    path: Tuple[str, ...]
    access: Tuple[str, ...] = ()

@dataclass(frozen=True)
class Instance:
    edges: Tuple[str, ...]
    service: Tuple[str, ...]
    worlds: Tuple[Tuple[str, ...], ...]
    probes: Tuple[Probe, ...]
    repair_budget: int
    probe_budget: int

    def __post_init__(self):
        universe = set(self.edges)
        assert len(self.edges) == len(universe)
        assert self.repair_budget >= 0 and self.probe_budget >= 0
        assert set(self.service) <= universe
        assert all(set(w) <= universe for w in self.worlds)
        assert len(self.worlds) > 0 and len(set(self.worlds)) == len(self.worlds)
        assert all(set(p.path + p.access) <= universe and p.path for p in self.probes)

def working(world, repaired, path):
    return all(e in repaired or e not in world for e in path)

def success(instance, world, repaired):
    return working(world, repaired, instance.service)

def eligible(instance, world_ids, repaired, probe):
    return all(working(instance.worlds[i], repaired, probe.access) for i in world_ids)

def outcomes(instance, world_ids, repaired, probe):
    up = tuple(i for i in world_ids if working(instance.worlds[i], repaired, probe.path))
    down = tuple(i for i in world_ids if i not in up)
    return tuple(x for x in (up, down) if x)

def terminal(instance, world_ids, repaired):
    return Fraction(sum(success(instance, instance.worlds[i], repaired) for i in world_ids), len(world_ids))

def actions(instance, world_ids, repaired, rb, pb):
    if rb:
        for e in instance.edges:
            if e not in repaired:
                yield ("repair", e)
    if pb:
        for p in instance.probes:
            if eligible(instance, world_ids, repaired, p):
                splits = outcomes(instance, world_ids, repaired, p)
                if len(splits) > 1:
                    yield ("probe", p.name)

def apply(instance, world_ids, repaired, rb, pb, action):
    kind, name = action
    if kind == "repair":
        assert rb > 0 and name in instance.edges and name not in repaired
        return ((world_ids, frozenset(set(repaired) | {name}), rb - 1, pb, Fraction(1)),)
    assert kind == "probe" and pb > 0
    p = next(x for x in instance.probes if x.name == name)
    assert eligible(instance, world_ids, repaired, p)
    return tuple((ids, repaired, rb, pb - 1, Fraction(len(ids), len(world_ids)))
                 for ids in outcomes(instance, world_ids, repaired, p))

def exact_oracle(instance):
    """Bayesian success-maximizing finite-horizon policy; uniform prior."""
    ids = tuple(range(len(instance.worlds)))
    @lru_cache(None)
    def solve(world_ids, repaired, rb, pb):
        best = terminal(instance, world_ids, repaired)
        choice = ("stop", "")
        for action in actions(instance, world_ids, repaired, rb, pb):
            val = sum((prob * solve(x, r, b, q)[0]
                       for x, r, b, q, prob in apply(instance, world_ids, repaired, rb, pb, action)), Fraction())
            if val > best:
                best, choice = val, action
        return best, choice
    value, action = solve(ids, frozenset(), instance.repair_budget, instance.probe_budget)
    return value, action, solve.cache_info()

def myopic_policy(instance):
    """Non-novel one-step heuristic; optimize immediate terminal success."""
    ids = tuple(range(len(instance.worlds)))
    repaired = frozenset()
    rb, pb = instance.repair_budget, instance.probe_budget
    # Expected immediate terminal score; zero-valued probes cannot be selected.
    while True:
        base = terminal(instance, ids, repaired)
        best, chosen = base, None
        for action in actions(instance, ids, repaired, rb, pb):
            score = sum((prob * terminal(instance, x, r)
                         for x, r, b, q, prob in apply(instance, ids, repaired, rb, pb, action)), Fraction())
            if score > best:
                best, chosen = score, action
        if chosen is None:
            return base
        # Myopic policy cannot branch on probe observations: it will never
        # select a probe with no immediate terminal improvement.
        assert chosen[0] == "repair"
        ids, repaired, rb, pb, _ = apply(instance, ids, repaired, rb, pb, chosen)[0]

def unlocked_three():
    """Physical gate g fails in every world; three alternative service faults."""
    return Instance(("g", "a", "b", "c"), ("a", "b", "c"),
                    (("g", "a"), ("g", "b"), ("g", "c")),
                    (Probe("test_a", ("a",), ("g",)), Probe("test_b", ("b",), ("g",))),
                    2, 2)

def path_family(n):
    assert n >= 2
    es = tuple("e" + str(i) for i in range(n))
    return Instance(es, es, tuple((e,) for e in es), (Probe("whole_path", es),), 1, 1)

def main():
    i = unlocked_three()
    opt, first, info = exact_oracle(i)
    print("unlocked_three exact", opt, "first", first, "cache", info)
    print("unlocked_three myopic", myopic_policy(i))
    for n in (2, 3, 5, 8):
        j = path_family(n)
        print("path", n, "oracle", exact_oracle(j)[0], "myopic", myopic_policy(j))

if __name__ == "__main__":
    main()
