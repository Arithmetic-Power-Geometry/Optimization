"""E11 matched-rights deterministic baseline policies (standard library only).

All policies act on public belief hypotheses, never a selected hidden truth state.
This is a restricted deterministic, unit-cost model, not a full HEC implementation.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from random import Random
from physical_graph import State, Probe, admissible, outcome, probe, restore, service
from exact_oracle import Problem

NAMES = ("diagnosis_first", "repair_first", "random", "cost_sensitive_greedy", "drd_region_greedy")

@dataclass(frozen=True)
class Evaluation:
    name: str
    success: Fraction
    robust: bool
    probe_attempts: Fraction
    repair_attempts: Fraction

def evaluate(problem: Problem, name: str, weights: tuple[Fraction, ...] | None = None,
             seed: int = 20261020) -> Evaluation:
    if name not in NAMES:
        raise ValueError("unknown baseline")
    n = len(problem.hypotheses)
    if weights is None:
        weights = (Fraction(1, n),) * n
    if len(weights) != n or any(w < 0 for w in weights) or sum(weights) <= 0:
        raise ValueError("invalid prior")
    weights = tuple(w / sum(weights) for w in weights)
    rng = Random(seed)
    success = [False] * n
    probe_counts = [0] * n
    repair_counts = [0] * n

    def decision(items, remaining):
        # items are (hypothesis id, physical state) but action scoring only
        # uses the public belief, common admissibility, and simulated
        # candidate consequences; no hidden state is selected as truth.
        if not items:
            return
        if remaining <= 0:
            for i, s in items:
                success[i] = service(s, problem.demands)
            return
        if all(service(s, problem.demands) for _, s in items):
            for i, _ in items:
                success[i] = True
            return
        feasible_probes = [p for p in problem.probes if all(
            admissible(s, p) and s.budget.probes > 0 and s.budget.time > 0 for _, s in items)]
        feasible_repairs = [a for a in problem.repairs if all(
            a in {e.name for e in s.edges} and a not in s.repaired and
            s.budget.repairs > 0 and s.budget.time > 0 for _, s in items)]
        if not feasible_probes and not feasible_repairs:
            for i, s in items:
                success[i] = service(s, problem.demands)
            return

        mass = sum(weights[i] for i, _ in items)
        def partitions(p):
            groups = {}
            for i, s in items:
                groups.setdefault(outcome(s, p), []).append((i, s))
            return tuple(groups.values())
        def entropy_split(p):
            # Gini impurity reduction, not HEC hyperedge cutting.
            groups = partitions(p)
            return mass - sum(sum(weights[i] for i, _ in g)**2 for g in groups) / mass
        def region_gain(p):
            # DRD-inspired surrogate: expected decrease in unresolved
            # pairs of states with different successful SINGLE repair.
            def signatures(group):
                sig = []
                for i, s in group:
                    possible = frozenset(a for a in problem.repairs
                        if a in {e.name for e in s.edges} and a not in s.repaired
                        and s.budget.repairs and s.budget.time
                        and service(restore(s, a), problem.demands))
                    sig.append((i, possible))
                return sig
            def conflict(group):
                v = signatures(group)
                return sum(weights[i]*weights[j] for k,(i,ai) in enumerate(v)
                           for j,aj in v[k+1:] if not ai.intersection(aj))
            return conflict(items) - sum(conflict(g) for g in partitions(p))
        def repair_gain(a):
            return sum(weights[i] for i,s in items if service(restore(s,a),problem.demands)) / mass

        choice = None
        if name == "diagnosis_first":
            if feasible_probes:
                choice = ("probe", max(feasible_probes,key=lambda p:(entropy_split(p),-problem.probes.index(p))))
            elif feasible_repairs:
                choice = ("repair",max(feasible_repairs,key=lambda a:(repair_gain(a),-problem.repairs.index(a))))
        elif name == "repair_first":
            if feasible_repairs:
                choice = ("repair",max(feasible_repairs,key=lambda a:(repair_gain(a),-problem.repairs.index(a))))
            elif feasible_probes:
                choice = ("probe",max(feasible_probes,key=lambda p:(entropy_split(p),-problem.probes.index(p))))
        elif name == "random":
            options = [("probe",p) for p in feasible_probes]+[("repair",a) for a in feasible_repairs]
            choice = rng.choice(options)
        elif name == "cost_sensitive_greedy":
            # Unit-cost, one-step immediate repair success vs Gini information.
            options = [(repair_gain(a),"repair",a) for a in feasible_repairs]
            options += [(entropy_split(p)/mass,"probe",p) for p in feasible_probes]
            if options:
                _,kind,obj = max(options,key=lambda t:t[0])
                choice=(kind,obj)
        elif name == "drd_region_greedy":
            if feasible_probes:
                p=max(feasible_probes,key=lambda p:(region_gain(p),-problem.probes.index(p)))
                if region_gain(p)>0:
                    choice=("probe",p)
            if choice is None and feasible_repairs:
                choice=("repair",max(feasible_repairs,key=lambda a:(repair_gain(a),-problem.repairs.index(a))))
            if choice is None and feasible_probes:
                choice=("probe",feasible_probes[0])

        if choice is None:
            for i,s in items:
                success[i]=service(s,problem.demands)
            return
        kind, action=choice
        if kind=="repair":
            nxt=[]
            for i,s in items:
                repair_counts[i]+=1
                nxt.append((i,restore(s,action)))
            decision(tuple(nxt),remaining-1)
        else:
            groups={}
            for i,s in items:
                probe_counts[i]+=1
                t,obs=probe(s,action)
                groups.setdefault(obs,[]).append((i,t))
            for group in groups.values():
                decision(tuple(group),remaining-1)

    decision(tuple(enumerate(problem.hypotheses)),problem.horizon)
    return Evaluation(name,sum((weights[i] for i in range(n) if success[i]),Fraction()),
                      all(success),sum((weights[i]*probe_counts[i] for i in range(n)),Fraction()),
                      sum((weights[i]*repair_counts[i] for i in range(n)),Fraction()))
