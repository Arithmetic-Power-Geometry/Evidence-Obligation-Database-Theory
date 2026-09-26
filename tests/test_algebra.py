import unittest
from eod import EODDatabase, EvidenceOperation
from eod.algebra import EODAlgebra

class AlgebraTests(unittest.TestCase):
    def setUp(self):
        self.answer = {"w1":"A","w2":"B","w3":"B"}
        self.q = lambda w: self.answer[w]
        self.db = EODDatabase(
            ["w1","w2","w3"],
            [
                EvidenceOperation("a", {"w1":0,"w2":1,"w3":1}, 2),
                EvidenceOperation("b", {"w1":0,"w2":0,"w3":1}, 1),
            ],
        )

    def test_resolution_law(self):
        alg = EODAlgebra(self.db)
        self.assertTrue(alg.obstruct(self.q))
        resolved = EODAlgebra(alg.acquire("a", 1))
        self.assertEqual(resolved.obstruct(self.q), ())
        self.assertEqual(resolved.certify(self.q).status, "RESOLVED")

    def test_obstruction_contracts(self):
        alg = EODAlgebra(self.db)
        before = set(alg.obstruct(self.q))
        after = set(EODAlgebra(alg.acquire("b", 0)).obstruct(self.q))
        self.assertTrue(after.issubset(before))

    def test_acquire_idempotent(self):
        once = EODAlgebra(self.db).acquire("a", 1)
        twice = EODAlgebra(once).acquire("a", 1)
        self.assertEqual(once.version_space(), twice.version_space())

    def test_compatible_acquisitions_commute(self):
        left = EODAlgebra(EODAlgebra(self.db).acquire("a",1)).acquire("b",1)
        right = EODAlgebra(EODAlgebra(self.db).acquire("b",1)).acquire("a",1)
        self.assertEqual(left.version_space(), right.version_space())

    def test_obligate(self):
        obligation = EODAlgebra(self.db).obligate(self.q)
        self.assertEqual(obligation, (("a",), 2))

if __name__ == "__main__":
    unittest.main()
