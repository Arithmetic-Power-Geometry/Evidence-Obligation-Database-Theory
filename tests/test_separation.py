import unittest
from eod import EODDatabase, EODEngine, EvidenceOperation

class CapabilitySeparationTests(unittest.TestCase):
    def test_same_current_view_different_future_answerability(self):
        worlds = ["u", "v"]
        answers = {"u": 0, "v": 1}
        q = lambda w: answers[w]

        d_plus = EODDatabase(
            worlds,
            [EvidenceOperation("separator", {"u": 0, "v": 1}, 1)],
        )
        d_minus = EODDatabase(
            worlds,
            [EvidenceOperation("nonseparator", {"u": 0, "v": 0}, 1)],
        )

        self.assertEqual(d_plus.version_space(), d_minus.version_space())
        self.assertEqual(
            [q(w) for w in d_plus.version_space()],
            [q(w) for w in d_minus.version_space()],
        )

        plus = EODEngine(d_plus).resolve(q)
        minus = EODEngine(d_minus).resolve(q)

        self.assertEqual(plus.status, "ACQUIRABLY_RESOLVABLE")
        self.assertEqual(minus.status, "UNRESOLVABLE")

if __name__ == "__main__":
    unittest.main()
