from pprint import pprint
from eod import EODDatabase, EODEngine, EvidenceOperation

W=("w1","w2","w3","w4")
Q=dict(zip(W,(0,0,1,1)))
R=dict(zip(W,(0,1,0,1)))
q=lambda w:bool(Q[w])
r=lambda w:bool(R[w])
c=lambda w:q(w) and r(w)

systems={
"D1":EODDatabase(W,[
    EvidenceOperation("e1",dict(zip(W,(0,0,0,1))),1),
    EvidenceOperation("e2",dict(zip(W,(1,1,0,0))),1),
]),
"D2":EODDatabase(W,[
    EvidenceOperation("f1",dict(zip(W,(0,0,1,0))),1),
    EvidenceOperation("f2",dict(zip(W,(0,0,1,1))),1),
]),
}

for name,db in systems.items():
    eng=EODEngine(db)
    print(name)
    for label,query in [("q",q),("r",r),("q AND r",c)]:
        x=eng.resolve(query)
        print(label)
        pprint(x.as_dict())
