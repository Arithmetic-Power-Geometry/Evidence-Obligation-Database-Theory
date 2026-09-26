from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Any, Callable, Hashable
from .model import EODDatabase, World

@dataclass(frozen=True)
class SignedResolutionAnnotation:
    worlds: tuple[World,...]
    labels: tuple[tuple[World,Hashable],...]
    incidence: tuple[tuple[tuple[World,World],tuple[str,...]],...]

    def label_map(self):
        return dict(self.labels)

    def incidence_map(self):
        return dict(self.incidence)

def signed_annotation(db:EODDatabase, query:Callable[[World],Any]):
    worlds=tuple(db.version_space())
    ops=db.admissible_operations()
    labels=tuple((w,query(w)) for w in worlds)
    incidence=[]
    for u,v in combinations(worlds,2):
        sep=tuple(sorted(op.name for op in ops if op.separates(u,v)))
        incidence.append(((u,v),sep))
    return SignedResolutionAnnotation(worlds,labels,tuple(incidence))

def compose_boolean(
    left:SignedResolutionAnnotation,
    right:SignedResolutionAnnotation,
    connective:Callable[[Any,Any],Any],
):
    if left.worlds != right.worlds:
        raise ValueError("annotations must share the same ordered world set")
    if left.incidence != right.incidence:
        raise ValueError("annotations must share the same evidence incidence")
    l=left.label_map(); r=right.label_map()
    labels=tuple((w,connective(l[w],r[w])) for w in left.worlds)
    return SignedResolutionAnnotation(left.worlds,labels,left.incidence)

def obstruction_hypergraph(annotation:SignedResolutionAnnotation):
    labels=annotation.label_map()
    return tuple(
        (pair,seps)
        for pair,seps in annotation.incidence
        if labels[pair[0]] != labels[pair[1]]
    )
