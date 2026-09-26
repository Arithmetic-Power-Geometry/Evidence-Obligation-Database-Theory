"""Summarize synthetic_results.csv using only the Python standard library."""

import csv, statistics, sys
from collections import Counter

path=sys.argv[1] if len(sys.argv)>1 else "artifacts/synthetic_results.csv"
with open(path,newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))

status=Counter(r["status"] for r in rows)
ratios=[float(r["greedy_ratio"]) for r in rows if r["greedy_ratio"] not in ("","None")]
gaps=[float(r["adaptivity_gap"]) for r in rows if r["adaptivity_gap"] not in ("","None")]
strict=[g for g in gaps if g>1+1e-12]

print("instances",len(rows))
print("status_counts",dict(status))
if ratios:
    print("greedy_ratio_mean",statistics.mean(ratios))
    print("greedy_ratio_max",max(ratios))
    print("greedy_exact_fraction",sum(abs(x-1)<1e-12 for x in ratios)/len(ratios))
if gaps:
    print("adaptive_instances",len(gaps))
    print("strict_adaptivity_fraction",len(strict)/len(gaps))
    print("adaptivity_gap_max",max(gaps))
