from __future__ import annotations

from dataclasses import dataclass, field
from typing import Hashable, Mapping, Sequence

World = Hashable

@dataclass(frozen=True)
class EvidenceOperation:
    name: str
    outcomes: Mapping[World, Hashable]
    cost: float = 1.0
    admissible: bool = True

    def separates(self, u: World, v: World) -> bool:
        return self.outcomes[u] != self.outcomes[v]

@dataclass
class EODDatabase:
    worlds: Sequence[World]
    evidence_operations: Sequence[EvidenceOperation]
    observations: dict[str, Hashable] = field(default_factory=dict)

    def operation(self, name: str) -> EvidenceOperation:
        for op in self.evidence_operations:
            if op.name == name:
                return op
        raise KeyError(f"Unknown evidence operation: {name}")

    def admissible_operations(self) -> list[EvidenceOperation]:
        return [op for op in self.evidence_operations if op.admissible]

    def version_space(self) -> list[World]:
        return [
            w for w in self.worlds
            if all(self.operation(name).outcomes[w] == value
                   for name, value in self.observations.items())
        ]

    def with_observation(self, operation_name: str, value: Hashable) -> "EODDatabase":
        observations = dict(self.observations)
        observations[operation_name] = value
        return EODDatabase(list(self.worlds), list(self.evidence_operations), observations)
