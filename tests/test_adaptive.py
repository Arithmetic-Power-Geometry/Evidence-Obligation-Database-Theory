import unittest
from eod import EODDatabase, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy

class AdaptiveTests(unittest.TestCase):
    def test_policy_resolves(self):
        ans = {"w1":"A","w2":"B","w3":"C"}
        db = EODDatabase(
            ["w1","w2","w3"],
            [
                EvidenceOperation("X", {"w1":1,"w2":0,"w3":0}, 1),
                EvidenceOperation("Y", {"w1":0,"w2":1,"w3":0}, 1),
            ],
        )
        p = optimal_worst_case_policy(db, lambda w: ans[w])
        self.assertIsNotNone(p)
        self.assertEqual(p.worst_case_cost, 2)

    def test_impossible_returns_none(self):
        ans = {"u":"A","v":"B"}
        db = EODDatabase(
            ["u","v"],
            [EvidenceOperation("same", {"u":0,"v":0}, 1)],
        )
        self.assertIsNone(optimal_worst_case_policy(db, lambda w: ans[w]))

if __name__ == "__main__":
    unittest.main()
