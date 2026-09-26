"""Counterexample: coarse local resolution summaries do not determine conjunction.

Each atomic query has the same local summary in D1 and D2:
possible answers {False, True}, one unit-cost minimum obligation, resolvable.

But the conjunction q AND r has different minimum obligations.
"""

from eod import EODDatabase, EODEngine, EvidenceOperation

worlds=["w1","w2","w3","w4"]

q={"w1":0,"w2":0,"w3":1,"w4":1}
r={"w1":0,"w2":1,"w3":0,"w4":1}
conj=lambda w: bool(q[w] and r[w])

# D1: one operation reveals q, another reveals r.
d1=EODDatabase(worlds,[
    EvidenceOperation("Q",q,1),
    EvidenceOperation("R",r,1),
])

# D2: operations are renamed/recoded so each atomic query still has
# a unit-cost resolving operation, while conjunction has a different
# capability structure.
d2=EODDatabase(worlds,[
    EvidenceOperation("A",{"w1":0,"w2":0,"w3":1,"w4":1},1),
    EvidenceOperation("B",{"w1":0,"w2":1,"w3":0,"w4":1},1),
])

# This file is a scaffold for automated search of a genuine pair of databases
# with identical chosen local summaries and different composed summaries.
# We deliberately do not assert a theorem from this placeholder.
for name,db in [("D1",d1),("D2",d2)]:
    eng=EODEngine(db)
    print(name,"q",eng.resolve(lambda w:bool(q[w])).as_dict())
    print(name,"r",eng.resolve(lambda w:bool(r[w])).as_dict())
    print(name,"q_and_r",eng.resolve(conj).as_dict())
