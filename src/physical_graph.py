"""E09 deterministic physical graph kernel (Python >=3.11; standard library only).

No hidden-state oracle is supplied to policies. State represents physical truth;
the controller must choose only actions commonly feasible in its belief set.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Literal

Outcome = Literal["UP", "DOWN"]
Mode = Literal["CSP", "CAP", "UP"]

@dataclass(frozen=True)
class Edge:
    name: str
    u: str
    v: str
    up: bool = True

@dataclass(frozen=True)
class Probe:
    name: str
    nodes: tuple[str, ...]
    edges: tuple[str, ...]
    mode: Mode = "CSP"

@dataclass(frozen=True)
class Budget:
    repairs: int
    probes: int
    time: int
    def __post_init__(self) -> None:
        if min(self.repairs, self.probes, self.time) < 0:
            raise ValueError("negative budget")

@dataclass(frozen=True)
class State:
    edges: tuple[Edge, ...]
    monitors: frozenset[str]
    allowed_pairs: frozenset[tuple[str, str]]
    budget: Budget
    selected_routes: frozenset[str] = frozenset()
    history: tuple[tuple[str, str], ...] = ()
    repaired: frozenset[str] = frozenset()
    def __post_init__(self) -> None:
        names = [e.name for e in self.edges]
        if len(set(names)) != len(names):
            raise ValueError("duplicate edge identifiers")

def admissible(s: State, p: Probe) -> bool:
    if len(p.nodes) != len(p.edges) + 1 or not p.edges:
        return False
    if p.nodes[0] not in s.monitors or p.nodes[-1] not in s.monitors:
        return False
    if (p.nodes[0], p.nodes[-1]) not in s.allowed_pairs:
        return False
    if p.mode == "CSP" and len(set(p.nodes)) != len(p.nodes):
        return False
    if p.mode == "UP" and p.name not in s.selected_routes:
        return False
    lookup = {e.name: e for e in s.edges}
    for i, name in enumerate(p.edges):
        e = lookup.get(name)
        if e is None or {e.u, e.v} != {p.nodes[i], p.nodes[i + 1]}:
            return False
    return True

def outcome(s: State, p: Probe) -> Outcome:
    if not admissible(s, p):
        raise ValueError("probe inadmissible, not DOWN")
    lookup = {e.name: e for e in s.edges}
    return "UP" if all(lookup[n].up for n in p.edges) else "DOWN"

def probe(s: State, p: Probe, time_cost: int = 1) -> tuple[State, Outcome]:
    if not admissible(s, p):
        raise ValueError("probe inadmissible")
    if time_cost < 0 or s.budget.probes < 1 or s.budget.time < time_cost:
        raise ValueError("probe budget exhausted")
    o = outcome(s, p)
    b = replace(s.budget, probes=s.budget.probes - 1, time=s.budget.time - time_cost)
    return replace(s, budget=b, history=s.history + (("probe:" + p.name, o),)), o

def restore(s: State, edge_name: str, *, success: bool = True, time_cost: int = 1,
            enable_monitor: str | None = None,
            enable_pairs: frozenset[tuple[str, str]] = frozenset()) -> State:
    if time_cost < 0 or s.budget.repairs < 1 or s.budget.time < time_cost:
        raise ValueError("repair budget exhausted")
    if edge_name in s.repaired:
        raise ValueError("irreversible restoration cannot repeat")
    if edge_name not in {e.name for e in s.edges}:
        raise ValueError("cannot restore uninstalled edge")
    updated = tuple(replace(e, up=True) if e.name == edge_name and success else e for e in s.edges)
    b = replace(s.budget, repairs=s.budget.repairs - 1, time=s.budget.time - time_cost)
    # Public access only activates on a successful restoration.
    m = s.monitors | frozenset((enable_monitor,)) if success and enable_monitor else s.monitors
    pairs = s.allowed_pairs | enable_pairs if success else s.allowed_pairs
    return replace(s, edges=updated, monitors=m, allowed_pairs=pairs, budget=b,
                   repaired=s.repaired | {edge_name},
                   history=s.history + (("restore:" + edge_name, "SUCCESS" if success else "FAILED"),))

def service(s: State, demands: tuple[tuple[str, str], ...]) -> bool:
    adj: dict[str, set[str]] = {}
    for e in s.edges:
        if e.up:
            adj.setdefault(e.u, set()).add(e.v)
            adj.setdefault(e.v, set()).add(e.u)
    for start, end in demands:
        seen = {start}
        todo = [start]
        while todo:
            for v in adj.get(todo.pop(), ()):
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        if end not in seen:
            return False
    return True

def common_admissible(states: tuple[State, ...], p: Probe) -> bool:
    return bool(states) and all(admissible(s, p) for s in states)

def series_failure(failed: str = "left") -> tuple[State, Probe]:
    if failed not in {"left", "right"}:
        raise ValueError("unknown failure")
    s = State((Edge("left", "s", "u", failed != "left"),
               Edge("right", "u", "t", failed != "right")),
              frozenset({"s", "t"}), frozenset({("s", "t")}), Budget(2, 2, 5))
    return s, Probe("full", ("s", "u", "t"), ("left", "right"))

def gate_failure(failed: str = "left") -> tuple[State, Probe, Probe]:
    base, full = series_failure(failed)
    s = replace(base, edges=base.edges + (Edge("gate", "c", "u", False),))
    sub = Probe("subleft", ("s", "u"), ("left",))
    return s, full, sub
