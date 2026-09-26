import unittest
from eod import EODDatabase, EvidenceOperation
from eod.composition import signed_annotation, compose_boolean, obstruction_hypergraph
from eod.hypergraph import obligation_hypergraph

class BooleanCompositionTests(unittest.TestCase):
    def setUp(self):
        self.db=EODDatabase(["a","b","c","d"],[
            EvidenceOperation("x",{"a":0,"b":0,"c":1,"d":1}),
            EvidenceOperation("y",{"a":0,"b":1,"c":0,"d":1}),
        ])
        self.q=lambda w:w in ("c","d")
        self.r=lambda w:w in ("b","d")

    def test_conjunction_matches_direct_hypergraph(self):
        aq=signed_annotation(self.db,self.q)
        ar=signed_annotation(self.db,self.r)
        ac=compose_boolean(aq,ar,lambda x,y:bool(x and y))
        composed=obstruction_hypergraph(ac)
        direct=obligation_hypergraph(self.db,lambda w:self.q(w) and self.r(w)).separators
        self.assertEqual(composed,direct)

    def test_disjunction_matches_direct_hypergraph(self):
        aq=signed_annotation(self.db,self.q)
        ar=signed_annotation(self.db,self.r)
        ac=compose_boolean(aq,ar,lambda x,y:bool(x or y))
        self.assertEqual(
            obstruction_hypergraph(ac),
            obligation_hypergraph(self.db,lambda w:self.q(w) or self.r(w)).separators
        )

    def test_xor_matches_direct_hypergraph(self):
        aq=signed_annotation(self.db,self.q)
        ar=signed_annotation(self.db,self.r)
        ac=compose_boolean(aq,ar,lambda x,y:bool(x)^bool(y))
        self.assertEqual(
            obstruction_hypergraph(ac),
            obligation_hypergraph(self.db,lambda w:bool(self.q(w))^bool(self.r(w))).separators
        )

if __name__=="__main__":
    unittest.main()
