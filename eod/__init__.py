"""Evidence-Obligation Database Theory reference implementation."""

from .model import EvidenceOperation, EODDatabase
from .engine import EODEngine, ResolutionResult
from .algebra import EODAlgebra, QueryView, SeparationView
from .adaptive import PolicyNode, optimal_worst_case_policy
from .hypergraph import ObligationHypergraph, obligation_hypergraph
from .composition import (
    SignedResolutionAnnotation,
    signed_annotation,
    compose_boolean,
    obstruction_hypergraph,
)

__all__ = [
    "EvidenceOperation",
    "EODDatabase",
    "EODEngine",
    "ResolutionResult",
    "EODAlgebra",
    "QueryView",
    "SeparationView",
    "PolicyNode",
    "optimal_worst_case_policy",
    "ObligationHypergraph",
    "obligation_hypergraph",
    "SignedResolutionAnnotation",
    "signed_annotation",
    "compose_boolean",
    "obstruction_hypergraph",
]
