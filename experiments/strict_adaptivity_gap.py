from pprint import pprint

from eod import EODDatabase, EODEngine, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy

worlds = ["w1","w2","w3","w4"]
answer = {w: i + 1 for i, w in enumerate(worlds)}
q = lambda w: answer[w]

db = EODDatabase(
    worlds,
    [
        EvidenceOperation("A", {"w1":0,"w2":0,"w3":0,"w4":1}, 1),
        EvidenceOperation("B", {"w1":0,"w2":0,"w3":1,"w4":0}, 1),
        EvidenceOperation("C", {"w1":0,"w2":1,"w3":0,"w4":1}, 1),
    ],
)

fixed = EODEngine(db).resolve(q)
adaptive = optimal_worst_case_policy(db, q)

assert fixed.minimum_cost == 3
assert adaptive is not None
assert adaptive.worst_case_cost == 2

print("Fixed optimum:")
pprint(fixed.as_dict())
print("\nAdaptive optimum:")
pprint(adaptive.as_dict())
print("\nAdaptivity gap:", fixed.minimum_cost / adaptive.worst_case_cost)
