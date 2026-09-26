"""Deterministic synthetic benchmark suite for EOD v0.5.

Generates explicit finite EOD instances and compares:
- exact fixed obligation,
- greedy fixed obligation,
- exact adaptive worst-case policy (small instances only).

Writes machine-readable CSV without external dependencies.
"""

from __future__ import annotations
import argparse, csv, random, time
from pathlib import Path

from eod import EODDatabase, EODEngine, EvidenceOperation
from eod.adaptive import optimal_worst_case_policy
from eod.greedy import greedy_obligation

def make_instance(seed: int, n_worlds: int, n_ops: int, n_answers: int = 3):
    rng = random.Random(seed)
    worlds = [f"w{i}" for i in range(n_worlds)]
    answers = {w: rng.randrange(n_answers) for w in worlds}
    # Ensure query is nonconstant when possible.
    if n_worlds >= 2 and len(set(answers.values())) == 1:
        answers[worlds[-1]] = (answers[worlds[0]] + 1) % n_answers

    ops = []
    for j in range(n_ops):
        outcomes = {w: rng.randrange(2) for w in worlds}
        cost = rng.randint(1, 5)
        admissible = rng.random() >= 0.1
        ops.append(EvidenceOperation(f"e{j}", outcomes, cost, admissible))
    return EODDatabase(worlds, ops), (lambda w: answers[w])

def evaluate(seed, n_worlds, n_ops, adaptive_limit=8):
    db, q = make_instance(seed, n_worlds, n_ops)

    t0=time.perf_counter()
    exact=EODEngine(db).resolve(q)
    exact_ms=(time.perf_counter()-t0)*1000

    t0=time.perf_counter()
    greedy=greedy_obligation(db,q)
    greedy_ms=(time.perf_counter()-t0)*1000

    adaptive=None
    adaptive_ms=None
    if n_worlds <= adaptive_limit and n_ops <= adaptive_limit:
        t0=time.perf_counter()
        adaptive=optimal_worst_case_policy(db,q)
        adaptive_ms=(time.perf_counter()-t0)*1000

    exact_cost=exact.minimum_cost
    greedy_cost=None if greedy is None else greedy.cost
    adaptive_cost=None if adaptive is None else adaptive.worst_case_cost

    return {
        "seed":seed,
        "worlds":n_worlds,
        "operations":n_ops,
        "status":exact.status,
        "obstruction_pairs":len(exact.obstruction_pairs),
        "exact_cost":exact_cost,
        "greedy_cost":greedy_cost,
        "greedy_ratio":(
            None if exact_cost in (None,0) or greedy_cost is None
            else greedy_cost/exact_cost
        ),
        "adaptive_cost":adaptive_cost,
        "adaptivity_gap":(
            None if exact_cost in (None,0) or adaptive_cost in (None,0)
            else exact_cost/adaptive_cost
        ),
        "exact_ms":round(exact_ms,6),
        "greedy_ms":round(greedy_ms,6),
        "adaptive_ms":None if adaptive_ms is None else round(adaptive_ms,6),
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",type=int,default=100)
    p.add_argument("--out",default="artifacts/synthetic_results.csv")
    args=p.parse_args()

    rows=[]
    configs=[(4,4),(5,5),(6,6),(8,8),(12,10),(16,12)]
    for n_worlds,n_ops in configs:
        for seed in range(args.seeds):
            rows.append(evaluate(seed,n_worlds,n_ops))

    path=Path(args.out)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {path}")

if __name__=="__main__":
    main()
