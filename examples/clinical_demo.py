from pprint import pprint
from eod import EODDatabase, EODEngine, EvidenceOperation

worlds = ["w1", "w2", "w3"]
treatment = {"w1": "A", "w2": "B", "w3": "B"}

db = EODDatabase(
    worlds,
    [
        EvidenceOperation("Test A", {"w1": 0, "w2": 1, "w3": 1}, 2.0),
        EvidenceOperation("Test B", {"w1": 0, "w2": 0, "w3": 1}, 1.0),
    ],
)

query = lambda w: treatment[w]
print("Initial EOD query")
pprint(EODEngine(db).resolve(query).as_dict())

print("\nAfter observing Test A = 1")
pprint(EODEngine(db.with_observation("Test A", 1)).resolve(query).as_dict())
