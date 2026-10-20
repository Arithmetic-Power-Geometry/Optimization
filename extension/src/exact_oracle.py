"""E10 exhaustive finite-horizon oracle; deterministic transitions and noiseless probes.

Policies see only common admissible actions and public observations. No hidden state
is exposed in the returned decision; terminal service is checked per hypothesis.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from physical_graph import State, Probe, admissible, outcome, restore, probe, service

@dataclass(frozen=True)
class Problem:
    hypotheses: tuple[State, ...]
    probes: tuple[Probe, ...]
    repairs: tuple[str, ...]
    demands: tuple[tuple[str, str], ...]
    horizon: int
    def __post_init__(self):
        if not self.hypotheses or self.horizon < 0:
            raise ValueError("nonempty hypotheses and nonnegative horizon required")
        if len(set(self.hypotheses)) != len(self.hypotheses):
            raise ValueError("duplicate physical hypotheses")
        if len({s.budget for s in self.hypotheses}) != 1:
            raise ValueError("all hypotheses must start with equal public budgets")

@dataclass(frozen=True)
class Result:
    robust: bool
    bayes: Fraction
    nodes: int

def solve(problem: Problem, weights: tuple[Fraction, ...] | None = None) -> Result:
    """Maximize probability of terminal service, and separately robust feasibility.

    Weights are unnormalized nonnegative rational masses; deterministic repair
    feedback is public SUCCESS (including already-UP repairs). One probe costs
    one time/probe unit; one repair costs one time/repair unit.
    """
    n = len(problem.hypotheses)
    if weights is None:
        weights = (Fraction(1, n),) * n
    if len(weights) != n or any(w < 0 for w in weights) or sum(weights) == 0:
        raise ValueError("invalid weights")
    weights = tuple(w / sum(weights) for w in weights)
    count = 0

    @lru_cache(None)
    def visit(items: tuple[tuple[int, State], ...], depth: int) -> tuple[bool, Fraction]:
        nonlocal count
        count += 1
        success = tuple(service(s, problem.demands) for _, s in items)
        best_r = all(success)
        best_p = sum((weights[i] for (i, _), ok in zip(items, success) if ok), Fraction())
        if depth == 0 or best_r:
            return best_r, best_p
        for p in problem.probes:
            if not all(admissible(s, p) and s.budget.probes >= 1 and s.budget.time >= 1 for _, s in items):
                continue
            groups: dict[str, list[tuple[int, State]]] = {}
            for i, s in items:
                nxt, obs = probe(s, p)
                groups.setdefault(obs, []).append((i, nxt))
            vals = [visit(tuple(group), depth - 1) for group in groups.values()]
            best_r |= all(v[0] for v in vals)
            best_p = max(best_p, sum((v[1] for v in vals), Fraction()))
        for name in problem.repairs:
            if not all(s.budget.repairs >= 1 and s.budget.time >= 1 and name not in s.repaired
                       and name in {e.name for e in s.edges} for _, s in items):
                continue
            nxt = tuple((i, restore(s, name)) for i, s in items)
            r, value = visit(nxt, depth - 1)
            best_r |= r
            best_p = max(best_p, value)
        return best_r, best_p

    robust, bayes = visit(tuple(enumerate(problem.hypotheses)), problem.horizon)
    return Result(robust, bayes, count)
