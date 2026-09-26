import unittest
from eod import EODDatabase, EODEngine, EvidenceOperation

def reduce_set_cover(universe, sets, costs):
    worlds=["a"]+[f"u{i}" for i in universe]
    ops=[]
    for j,S in enumerate(sets):
        outcomes={"a":0}
        outcomes.update({f"u{i}":int(i in S) for i in universe})
        ops.append(EvidenceOperation(f"e{j}",outcomes,costs[j]))
    db=EODDatabase(worlds,ops)
    q=lambda w:0 if w=="a" else 1
    return db,q

class SetCoverReductionTests(unittest.TestCase):
    def test_weighted_reduction(self):
        U=[1,2,3]
        sets=[{1,2},{2,3},{1},{3}]
        costs=[3,2,1,1]
        db,q=reduce_set_cover(U,sets,costs)
        result=EODEngine(db).resolve(q)
        # {1} and {2,3} costs 1+2=3; {1,2} and {3} also cost 4.
        self.assertEqual(result.minimum_cost,3)

    def test_uncoverable_element_is_unresolvable(self):
        U=[1,2,3]
        sets=[{1},{2}]
        db,q=reduce_set_cover(U,sets,[1,1])
        self.assertEqual(EODEngine(db).resolve(q).status,"UNRESOLVABLE")

if __name__=="__main__":
    unittest.main()
