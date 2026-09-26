import unittest
from eod import EODDatabase, EODEngine, EvidenceOperation

W=("w1","w2","w3","w4")
Q=dict(zip(W,(0,0,1,1)))
R=dict(zip(W,(0,1,0,1)))

def signature(db, query):
    x=EODEngine(db).resolve(query)
    return (x.status, tuple(x.possible_answers), x.minimum_cost, len(x.obstruction_pairs))

class CompositionImpossibilityTests(unittest.TestCase):
    def test_exact_witness(self):
        d1=EODDatabase(W,[
            EvidenceOperation("e1",dict(zip(W,(0,0,0,1))),1),
            EvidenceOperation("e2",dict(zip(W,(1,1,0,0))),1),
        ])
        d2=EODDatabase(W,[
            EvidenceOperation("f1",dict(zip(W,(0,0,1,0))),1),
            EvidenceOperation("f2",dict(zip(W,(0,0,1,1))),1),
        ])
        q=lambda w:bool(Q[w])
        r=lambda w:bool(R[w])
        c=lambda w:q(w) and r(w)

        self.assertEqual(signature(d1,q),signature(d2,q))
        self.assertEqual(signature(d1,r),signature(d2,r))
        self.assertNotEqual(signature(d1,c),signature(d2,c))
        self.assertEqual(signature(d1,c)[2],1)
        self.assertEqual(signature(d2,c)[2],2)

if __name__=="__main__":
    unittest.main()
