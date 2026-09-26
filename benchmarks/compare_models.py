from pprint import pprint
from eod import EODDatabase, EODEngine, EvidenceOperation

worlds = ["w1", "w2", "w3", "w4"]
decision = {"w1": "REJECT", "w2": "APPROVE", "w3": "APPROVE", "w4": "APPROVE"}

db = EODDatabase(
    worlds,
    [
        EvidenceOperation("identity_check", {"w1":"fail","w2":"pass","w3":"pass","w4":"pass"}, 4),
        EvidenceOperation("income_check", {"w1":"low","w2":"low","w3":"high","w4":"high"}, 2),
        EvidenceOperation("history_check", {"w1":"thin","w2":"thin","w3":"thin","w4":"rich"}, 1),
    ],
)
q = lambda w: decision[w]

print("=== Relational-style result ===")
print({"rows": [(w, decision[w]) for w in worlds]})

print("\n=== Possible-world result ===")
possible = sorted({q(w) for w in db.version_space()})
print({"possible_answers": possible})

print("\n=== Certain-answer result ===")
print({"certain_answer": possible[0] if len(possible) == 1 else None})

print("\n=== EOD result ===")
pprint(EODEngine(db).resolve(q).as_dict())

print("\n=== EOD after identity_check = pass ===")
pprint(EODEngine(db.with_observation("identity_check", "pass")).resolve(q).as_dict())

print("\n=== Unresolvable case ===")
u = EODDatabase(
    ["u1", "u2"],
    [EvidenceOperation("available_test", {"u1":0, "u2":0}, 1)]
)
pprint(EODEngine(u).resolve(lambda w: {"u1":"A","u2":"B"}[w]).as_dict())
