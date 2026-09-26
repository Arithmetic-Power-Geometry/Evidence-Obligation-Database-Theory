"""Small deterministic scaling benchmark for the exact EOD obligation engine.

The goal is not to publish machine-specific performance numbers. It exposes
how many candidate evidence subsets an exhaustive semantic oracle may need to
consider as the capability set grows.
"""

from math import comb

def candidate_subsets(n):
    return sum(comb(n, r) for r in range(1, n + 1))

print("evidence_operations,candidate_nonempty_subsets")
for n in range(1, 21):
    print(f"{n},{candidate_subsets(n)}")

print("\nExact exhaustive search grows as 2^n - 1 in the worst case.")
print("This motivates approximation and structured EOD fragments.")
