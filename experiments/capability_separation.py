"""Executable witness for the EOD Capability-Separation Theorem."""

from pprint import pprint

from eod import EODDatabase, EODEngine, EvidenceOperation

worlds = ["u", "v"]
answer = {"u": 0, "v": 1}
query = lambda w: answer[w]

# D_plus has a future evidence operation that separates u and v.
d_plus = EODDatabase(
    worlds,
    [EvidenceOperation("separating_test", {"u": 0, "v": 1}, cost=1.0)],
)

# D_minus has an evidence operation, but it cannot separate u and v.
d_minus = EODDatabase(
    worlds,
    [EvidenceOperation("nonseparating_test", {"u": 0, "v": 0}, cost=1.0)],
)

def current_query_view(db):
    version = tuple(db.version_space())
    return {
        "version_space": version,
        "query_values": tuple((w, query(w)) for w in version),
        "possible_answers": tuple(sorted({query(w) for w in version})),
    }

view_plus = current_query_view(d_plus)
view_minus = current_query_view(d_minus)
result_plus = EODEngine(d_plus).resolve(query)
result_minus = EODEngine(d_minus).resolve(query)

print("D+ current query view:")
pprint(view_plus)
print("\nD- current query view:")
pprint(view_minus)

print("\nCurrent-query equivalent:", view_plus == view_minus)

print("\nD+ EOD result:")
pprint(result_plus.as_dict())

print("\nD- EOD result:")
pprint(result_minus.as_dict())

assert view_plus == view_minus
assert result_plus.status == "ACQUIRABLY_RESOLVABLE"
assert result_minus.status == "UNRESOLVABLE"
assert result_plus.status != result_minus.status

print("\nCapability-Separation witness verified.")
