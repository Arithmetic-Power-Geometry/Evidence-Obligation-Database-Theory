from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .engine import EODEngine
from .model import EODDatabase, World

Query = Callable[[World], Any]
Pair = tuple[World, World]

@dataclass(frozen=True)
class GreedyObligation:
    operations: tuple[str, ...]
    cost: float
    covered_pairs: int
    total_pairs: int

def greedy_obligation(db: EODDatabase, query: Query) -> GreedyObligation | None:
    """Weighted greedy set cover on EOD query-obstruction pairs.

    At each step choose the admissible operation maximizing newly covered
    obstruction pairs per unit cost. Returns None when resolution is impossible.
    """
    engine = EODEngine(db)
    obstruction = set(engine.obstruction(query))
    if not obstruction:
        return GreedyObligation((), 0.0, 0, 0)

    ops = db.admissible_operations()
    if not engine._covers(ops, tuple(obstruction)):
        return None

    uncovered = set(obstruction)
    chosen = []
    total_cost = 0.0

    while uncovered:
        best = None
        for op in ops:
            if op.name in chosen:
                continue
            newly = {p for p in uncovered if op.separates(*p)}
            if not newly:
                continue
            if op.cost == 0:
                key = (float("inf"), len(newly), op.name)
            else:
                key = (len(newly) / op.cost, len(newly), op.name)
            if best is None or key > best[0]:
                best = (key, op, newly)

        if best is None:
            return None

        _, op, newly = best
        chosen.append(op.name)
        total_cost += op.cost
        uncovered -= newly

    return GreedyObligation(
        tuple(chosen), total_cost, len(obstruction), len(obstruction)
    )
