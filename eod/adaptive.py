from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Callable, Hashable

from .model import EODDatabase, World

Query = Callable[[World], Any]

@dataclass(frozen=True)
class PolicyNode:
    operation: str | None
    answer: Any | None
    worst_case_cost: float
    branches: tuple[tuple[Hashable, "PolicyNode"], ...] = ()

    def as_dict(self):
        if self.operation is None:
            return {"answer": self.answer, "worst_case_cost": self.worst_case_cost}
        return {
            "operation": self.operation,
            "worst_case_cost": self.worst_case_cost,
            "branches": {str(k): v.as_dict() for k, v in self.branches},
        }

def optimal_worst_case_policy(db: EODDatabase, query: Query) -> PolicyNode | None:
    """Exact optimal adaptive policy for small finite deterministic EOD states.

    Returns None if no admissible adaptive policy can guarantee resolution.
    """

    operations = tuple(db.admissible_operations())
    initial = tuple(db.version_space())

    @lru_cache(maxsize=None)
    def solve(worlds: tuple[World, ...], available: tuple[int, ...]):
        answers = {query(w) for w in worlds}
        if len(answers) == 1:
            return PolicyNode(None, next(iter(answers)), 0.0, ())

        best = None
        for idx in available:
            op = operations[idx]
            groups = {}
            for w in worlds:
                groups.setdefault(op.outcomes[w], []).append(w)

            # No refinement: this operation cannot help in this state.
            if len(groups) <= 1:
                continue

            remaining = tuple(i for i in available if i != idx)
            children = []
            feasible = True
            child_costs = []
            for outcome, group in sorted(groups.items(), key=lambda kv: repr(kv[0])):
                child = solve(tuple(group), remaining)
                if child is None:
                    feasible = False
                    break
                children.append((outcome, child))
                child_costs.append(child.worst_case_cost)

            if not feasible:
                continue

            total = op.cost + max(child_costs, default=0.0)
            node = PolicyNode(op.name, None, total, tuple(children))
            key = (total, op.name)
            if best is None or key < best[0]:
                best = (key, node)

        return None if best is None else best[1]

    return solve(initial, tuple(range(len(operations))))
