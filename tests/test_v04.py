import unittest

from eod import EODDatabase, EODEngine, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy
from eod.greedy import greedy_obligation

class V04Tests(unittest.TestCase):
    def test_strict_adaptivity_gap(self):
        worlds=["w1","w2","w3","w4"]
        ans={w:i for i,w in enumerate(worlds)}
        db=EODDatabase(worlds,[
            EvidenceOperation("A",{"w1":0,"w2":0,"w3":0,"w4":1},1),
            EvidenceOperation("B",{"w1":0,"w2":0,"w3":1,"w4":0},1),
            EvidenceOperation("C",{"w1":0,"w2":1,"w3":0,"w4":1},1),
        ])
        q=lambda w:ans[w]
        fixed=EODEngine(db).resolve(q)
        adaptive=optimal_worst_case_policy(db,q)
        self.assertEqual(fixed.minimum_cost,3)
        self.assertEqual(adaptive.worst_case_cost,2)

    def test_greedy_resolves(self):
        worlds=["a","b","c"]
        ans={"a":0,"b":1,"c":2}
        db=EODDatabase(worlds,[
            EvidenceOperation("x",{"a":0,"b":1,"c":1},1),
            EvidenceOperation("y",{"a":0,"b":0,"c":1},1),
        ])
        g=greedy_obligation(db,lambda w:ans[w])
        self.assertIsNotNone(g)
        self.assertEqual(set(g.operations),{"x","y"})

if __name__=="__main__":
    unittest.main()
