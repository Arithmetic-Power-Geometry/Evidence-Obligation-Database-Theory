"""A finite example where adaptive evidence costs less than a fixed obligation."""

from pprint import pprint
from eod import EODDatabase, EODEngine, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy

worlds = ["w1", "w2", "w3"]
answer = {"w1": "A", "w2": "B", "w3": "C"}
q = lambda w: answer[w]

# Test X isolates w1. If X says "not w1", Test Y distinguishes w2/w3.
# A fixed non-adaptive guarantee needs both X and Y (cost 2).
# The adaptive policy also has worst-case cost 2 here, but some branches stop at 1.
db = EODDatabase(
    worlds,
    [
        EvidenceOperation("X", {"w1":1,"w2":0,"w3":0}, 1),
        EvidenceOperation("Y", {"w1":0,"w2":1,"w3":0}, 1),
    ],
)

fixed = EODEngine(db).resolve(q)
adaptive = optimal_worst_case_policy(db, q)

print("Fixed non-adaptive obligation:")
pprint(fixed.as_dict())
print("\nOptimal adaptive worst-case policy:")
pprint(adaptive.as_dict() if adaptive else None)

print("\nInterpretation:")
print("The adaptive tree can terminate after X on the w1 branch,")
print("while retaining a worst-case guarantee for every world.")
