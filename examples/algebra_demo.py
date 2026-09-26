from pprint import pprint
from eod import EODDatabase, EvidenceOperation
from eod.algebra import EODAlgebra

worlds = ["w1", "w2", "w3"]
decision = {"w1": "A", "w2": "B", "w3": "B"}

db = EODDatabase(
    worlds,
    [
        EvidenceOperation("test_A", {"w1": 0, "w2": 1, "w3": 1}, 2),
        EvidenceOperation("test_B", {"w1": 0, "w2": 0, "w3": 1}, 1),
    ],
)
q = lambda w: decision[w]
alg = EODAlgebra(db)

print("VIEW")
pprint(alg.view(q))
print("\nOBSTRUCT")
pprint(alg.obstruct(q))
print("\nSEPARATE(test_A, query-relative)")
pprint(alg.separate("test_A", q))
print("\nOBLIGATE")
pprint(alg.obligate(q))
print("\nCERTIFY")
pprint(alg.certify(q).as_dict())

print("\nACQUIRE test_A = 1; then CERTIFY")
db2 = alg.acquire("test_A", 1)
pprint(EODAlgebra(db2).certify(q).as_dict())
