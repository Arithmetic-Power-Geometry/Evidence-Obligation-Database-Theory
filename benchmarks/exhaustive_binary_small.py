"""Exhaustive small binary-capability audit.

Enumerates 4-world, 3-test binary evidence systems for the identity query.
Reports resolvable instances, strict adaptivity-gap instances, and greedy
agreement with the exact fixed optimum. Unit costs are used.
"""

from itertools import product, combinations

from eod import EODDatabase, EODEngine, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy
from eod.greedy import greedy_obligation

worlds = ["w1","w2","w3","w4"]
qmap = {w:i for i,w in enumerate(worlds)}
q = lambda w:qmap[w]

patterns = [p for p in product([0,1], repeat=4) if len(set(p)) > 1]

total = resolvable = strict_gap = greedy_exact = 0
max_gap = 1.0
max_witness = None

for pattern_set in combinations(patterns, 3):
    total += 1
    ops = [
        EvidenceOperation(
            f"T{i+1}",
            {w: pattern[j] for j,w in enumerate(worlds)},
            1,
        )
        for i,pattern in enumerate(pattern_set)
    ]
    db = EODDatabase(worlds, ops)
    exact = EODEngine(db).resolve(q)
    if exact.status != "ACQUIRABLY_RESOLVABLE":
        continue

    resolvable += 1
    greedy = greedy_obligation(db,q)
    adaptive = optimal_worst_case_policy(db,q)

    if greedy is not None and greedy.cost == exact.minimum_cost:
        greedy_exact += 1

    if adaptive is not None:
        gap = exact.minimum_cost / adaptive.worst_case_cost
        if gap > 1:
            strict_gap += 1
        if gap > max_gap:
            max_gap = gap
            max_witness = pattern_set

print("total_pattern_sets", total)
print("resolvable", resolvable)
print("strict_adaptivity_gap", strict_gap)
print("greedy_equals_exact", greedy_exact)
print("maximum_gap", max_gap)
print("maximum_gap_witness", max_witness)
