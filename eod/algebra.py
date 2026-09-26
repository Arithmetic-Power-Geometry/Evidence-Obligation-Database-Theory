from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Hashable

from .engine import EODEngine, ResolutionResult
from .model import EODDatabase, World

Query = Callable[[World], Any]
Pair = tuple[World, World]

@dataclass(frozen=True)
class QueryView:
    worlds: tuple[World, ...]
    possible_answers: tuple[Any, ...]

@dataclass(frozen=True)
class SeparationView:
    operation: str
    separated_pairs: tuple[Pair, ...]

class EODAlgebra:
    """Finite deterministic algebra for EOD v0.3.

    VIEW      : (D, q) -> QueryView
    OBSTRUCT  : (D, q) -> query-disagreeing world pairs
    SEPARATE  : (D, e, q?) -> pairs distinguished by evidence operation e
    OBLIGATE  : (D, q) -> minimum non-adaptive evidence obligation or None
    ACQUIRE   : (D, e, outcome) -> refined EOD database state
    CERTIFY   : (D, q) -> ResolutionResult
    """

    def __init__(self, db: EODDatabase):
        self.db = db

    def view(self, query: Query) -> QueryView:
        worlds = tuple(self.db.version_space())
        answers = tuple(sorted({query(w) for w in worlds}, key=repr))
        return QueryView(worlds, answers)

    def obstruct(self, query: Query) -> tuple[Pair, ...]:
        return tuple(EODEngine(self.db).obstruction(query))

    def separate(self, operation_name: str, query: Query | None = None) -> SeparationView:
        op = self.db.operation(operation_name)
        worlds = self.db.version_space()
        pairs: list[Pair] = []
        for i, u in enumerate(worlds):
            for v in worlds[i + 1:]:
                if query is not None and query(u) == query(v):
                    continue
                if op.separates(u, v):
                    pairs.append((u, v))
        return SeparationView(operation_name, tuple(pairs))

    def obligate(self, query: Query) -> tuple[tuple[str, ...], float] | None:
        engine = EODEngine(self.db)
        return engine.minimum_obligation(engine.obstruction(query))

    def acquire(self, operation_name: str, outcome: Hashable) -> EODDatabase:
        return self.db.with_observation(operation_name, outcome)

    def certify(self, query: Query) -> ResolutionResult:
        return EODEngine(self.db).resolve(query)
