import unittest
from benchmarks.synthetic_suite import make_instance, evaluate

class SyntheticTests(unittest.TestCase):
    def test_reproducible_generation(self):
        a,qa=make_instance(7,5,5)
        b,qb=make_instance(7,5,5)
        self.assertEqual(a.worlds,b.worlds)
        self.assertEqual(
            [(x.name,dict(x.outcomes),x.cost,x.admissible) for x in a.evidence_operations],
            [(x.name,dict(x.outcomes),x.cost,x.admissible) for x in b.evidence_operations],
        )
        self.assertEqual([qa(w) for w in a.worlds],[qb(w) for w in b.worlds])

    def test_evaluation_schema(self):
        r=evaluate(1,4,4)
        for key in ["status","exact_cost","greedy_cost","exact_ms","greedy_ms"]:
            self.assertIn(key,r)

if __name__=="__main__":
    unittest.main()
