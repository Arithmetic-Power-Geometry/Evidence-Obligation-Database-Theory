from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from .model import EODDatabase, World

Query=Callable[[World],Any]
Pair=tuple[World,World]

@dataclass(frozen=True)
class ObligationHypergraph:
    obstruction_pairs: tuple[Pair,...]
    separators: tuple[tuple[Pair,tuple[str,...]],...]

    def impossible_pairs(self):
        return tuple(pair for pair,ops in self.separators if not ops)

def obligation_hypergraph(db:EODDatabase, query:Query)->ObligationHypergraph:
    worlds=db.version_space()
    pairs=[]
    rows=[]
    ops=db.admissible_operations()
    for i,u in enumerate(worlds):
        for v in worlds[i+1:]:
            if query(u)==query(v):
                continue
            pair=(u,v); pairs.append(pair)
            rows.append((pair,tuple(sorted(op.name for op in ops if op.separates(u,v)))))
    return ObligationHypergraph(tuple(pairs),tuple(rows))
