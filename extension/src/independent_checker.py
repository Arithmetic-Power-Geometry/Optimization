"""E10 independent exhaustive checker: enumerate attainable terminal success masks.

Unlike exact_oracle's weighted Bellman recursion, this checker constructs the
entire set of possible success masks for deterministic observation trees.
"""
from __future__ import annotations
from fractions import Fraction
from physical_graph import admissible, outcome, restore, service, probe
from exact_oracle import Problem

def masks(problem: Problem) -> frozenset[int]:
    states = problem.hypotheses
    full = (1 << len(states)) - 1

    def enumerate_masks(items: tuple[tuple[int, object], ...], remaining: int) -> set[int]:
        terminal = sum(1 << i for i, s in items if service(s, problem.demands))
        results = {terminal}
        if remaining == 0:
            return results
        for action in problem.probes:
            if all(admissible(s, action) and s.budget.probes and s.budget.time for _, s in items):
                groups: dict[str, list[tuple[int, object]]] = {}
                for i, s in items:
                    t, label = probe(s, action)
                    groups.setdefault(label, []).append((i, t))
                combinations = {0}
                for group in groups.values():
                    possibilities = enumerate_masks(tuple(group), remaining - 1)
                    combinations = {a | b for a in combinations for b in possibilities}
                results.update(combinations)
        for name in problem.repairs:
            if all(s.budget.repairs and s.budget.time and name not in s.repaired
                   and name in {e.name for e in s.edges} for _, s in items):
                nxt = tuple((i, restore(s, name)) for i, s in items)
                results.update(enumerate_masks(nxt, remaining - 1))
        return results

    return frozenset(enumerate_masks(tuple(enumerate(states)), problem.horizon))

def check(problem: Problem, weights: tuple[Fraction, ...] | None = None) -> tuple[bool, Fraction, int]:
    m = masks(problem)
    n = len(problem.hypotheses)
    if weights is None:
        weights = (Fraction(1, n),) * n
    if len(weights) != n or any(w < 0 for w in weights) or sum(weights) <= 0:
        raise ValueError("invalid weights")
    norm = sum(weights)
    return ((1 << n) - 1 in m,
            max(sum((weights[i] for i in range(n) if mask & (1 << i)), Fraction()) / norm for mask in m),
            len(m))
