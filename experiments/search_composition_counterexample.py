"""Search finite binary evidence systems for composition-summary collisions.

A local coarse signature intentionally forgets operation names and keeps:
(status, possible answers, minimum cost, obstruction count).

We search for two evidence systems with identical signatures for q and r but
different signature for q AND r.
"""

from itertools import combinations, product
from eod import EODDatabase, EODEngine, EvidenceOperation

worlds=("w1","w2","w3","w4")
qv=(0,0,1,1)
rv=(0,1,0,1)
q=lambda w:bool(qv[worlds.index(w)])
r=lambda w:bool(rv[worlds.index(w)])
c=lambda w:q(w) and r(w)

patterns=[p for p in product((0,1),repeat=4) if len(set(p))>1]

def sig(db,query):
    x=EODEngine(db).resolve(query)
    return (x.status,tuple(x.possible_answers),x.minimum_cost,len(x.obstruction_pairs))

seen={}
for pats in combinations(patterns,2):
    db=EODDatabase(worlds,[
        EvidenceOperation("e1",dict(zip(worlds,pats[0])),1),
        EvidenceOperation("e2",dict(zip(worlds,pats[1])),1),
    ])
    local=(sig(db,q),sig(db,r))
    composed=sig(db,c)
    if local in seen and seen[local][0]!=composed:
        old_composed,old_pats=seen[local]
        print("FOUND")
        print("local_signature",local)
        print("system_1",old_pats,"conjunction",old_composed)
        print("system_2",pats,"conjunction",composed)
        break
    seen[local]=(composed,pats)
else:
    print("No collision found in searched class")
