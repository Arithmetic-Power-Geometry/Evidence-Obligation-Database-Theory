import unittest
from eod import EODDatabase, EODEngine, EvidenceOperation

class EODTests(unittest.TestCase):
    def test_resolved(self):
        r = EODEngine(EODDatabase(["w1","w2"], [])).resolve(lambda w: "A")
        self.assertEqual(r.status, "RESOLVED")
        self.assertEqual(r.answer, "A")

    def test_minimum_obligation(self):
        decision = {"w1":"A","w2":"B","w3":"B"}
        db = EODDatabase(
            ["w1","w2","w3"],
            [
                EvidenceOperation("cheap_partial", {"w1":0,"w2":0,"w3":1}, 1),
                EvidenceOperation("separator", {"w1":0,"w2":1,"w3":1}, 2),
            ],
        )
        r = EODEngine(db).resolve(lambda w: decision[w])
        self.assertEqual(r.status, "ACQUIRABLY_RESOLVABLE")
        self.assertEqual(r.minimum_obligation, ("separator",))
        self.assertEqual(r.minimum_cost, 2)

    def test_unresolvable_certificate(self):
        db = EODDatabase(
            ["w1","w2"],
            [EvidenceOperation("same_outcome", {"w1":0,"w2":0}, 1)],
        )
        r = EODEngine(db).resolve(lambda w: {"w1":"A","w2":"B"}[w])
        self.assertEqual(r.status, "UNRESOLVABLE")
        self.assertEqual(set(r.impossibility_certificate), {"w1","w2"})

    def test_observation_resolves(self):
        op = EvidenceOperation("test", {"w1":0,"w2":1}, 1)
        db = EODDatabase(["w1","w2"], [op]).with_observation("test", 1)
        r = EODEngine(db).resolve(lambda w: {"w1":"A","w2":"B"}[w])
        self.assertEqual(r.status, "RESOLVED")
        self.assertEqual(r.answer, "B")

if __name__ == "__main__":
    unittest.main()
