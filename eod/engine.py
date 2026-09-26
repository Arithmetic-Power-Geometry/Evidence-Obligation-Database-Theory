from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any, Callable, Sequence

from .model import EODDatabase, EvidenceOperation, World

Pair = tuple[World, World]

@dataclass(frozen=True)
class ResolutionResult:
    status: str
    possible_answers: tuple[Any, ...]
    answer: Any | None
    obstruction_pairs: tuple[Pair, ...]
    minimum_obligation: tuple[str, ...]
    minimum_cost: float | None
    impossibility_certificate: Pair | None

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "possible_answers": list(self.possible_answers),
            "answer": self.answer,
            "obstruction_pairs": [list(p) for p in self.obstruction_pairs],
            "minimum_obligation": list(self.minimum_obligation),
            "minimum_cost": self.minimum_cost,
            "impossibility_certificate": (
                list(self.impossibility_certificate)
                if self.impossibility_certificate is not None else None
            ),
        }

class EODEngine:
    def __init__(self, db: EODDatabase):
        self.db = db

    def obstruction(self, query: Callable[[World], Any]) -> list[Pair]:
        worlds = self.db.version_space()
        return [(u, v) for u, v in combinations(worlds, 2) if query(u) != query(v)]

    @staticmethod
    def _covers(operations: Sequence[EvidenceOperation], pairs: Sequence[Pair]) -> bool:
        return all(any(op.separates(u, v) for op in operations) for u, v in pairs)

    def minimum_obligation(self, pairs: Sequence[Pair]):
        if not pairs:
            return (), 0.0
        operations = self.db.admissible_operations()
        if not self._covers(operations, pairs):
            return None
        best = None
        for r in range(1, len(operations) + 1):
            for subset in combinations(operations, r):
                if self._covers(subset, pairs):
                    cost = sum(op.cost for op in subset)
                    names = tuple(sorted(op.name for op in subset))
                    candidate = (cost, len(names), names)
                    if best is None or candidate < best:
                        best = candidate
        assert best is not None
        return best[2], best[0]

    def resolve(self, query: Callable[[World], Any]) -> ResolutionResult:
        worlds = self.db.version_space()
        answers = tuple(sorted({query(w) for w in worlds}, key=repr))
        if len(answers) == 1:
            return ResolutionResult("RESOLVED", answers, answers[0], (), (), 0.0, None)

        pairs = tuple(self.obstruction(query))
        obligation = self.minimum_obligation(pairs)
        if obligation is None:
            admissible = self.db.admissible_operations()
            witness = next(
                p for p in pairs if not any(op.separates(*p) for op in admissible)
            )
            return ResolutionResult(
                "UNRESOLVABLE", answers, None, pairs, (), None, witness
            )

        names, cost = obligation
        return ResolutionResult(
            "ACQUIRABLY_RESOLVABLE", answers, None, pairs, names, cost, None
        )
