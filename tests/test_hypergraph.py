import unittest
from eod import EODDatabase, EvidenceOperation
from eod.hypergraph import obligation_hypergraph

class HypergraphTests(unittest.TestCase):
    def test_empty_edge_is_impossibility(self):
        db=EODDatabase(["u","v"],[
            EvidenceOperation("same",{"u":0,"v":0},1)
        ])
        q=lambda w:0 if w=="u" else 1
        h=obligation_hypergraph(db,q)
        self.assertEqual(h.impossible_pairs(),(("u","v"),))

    def test_separator_incidence(self):
        db=EODDatabase(["u","v"],[
            EvidenceOperation("sep",{"u":0,"v":1},1)
        ])
        q=lambda w:0 if w=="u" else 1
        h=obligation_hypergraph(db,q)
        self.assertEqual(h.separators,((("u","v"),("sep",)),))

if __name__=="__main__":
    unittest.main()
