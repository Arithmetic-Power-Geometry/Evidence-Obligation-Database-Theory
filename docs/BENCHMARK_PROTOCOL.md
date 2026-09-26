# EOD Benchmark Protocol

## Objective

Evaluate whether the proposed semantics can be computed reproducibly and how exact, greedy, and adaptive resolution planning behave as explicit finite EOD instances grow.

## Instance factors

The deterministic generator varies:

- number of admissible worlds;
- number of evidence operations;
- query-answer classes;
- binary observation patterns;
- evidence costs;
- evidence admissibility.

Every instance is reproducible from its integer seed.

## Algorithms

### Exact fixed

Enumerates evidence subsets and returns the minimum-cost fixed obligation.

### Greedy fixed

Uses weighted obstruction coverage per unit cost.

### Exact adaptive

Uses dynamic programming over version spaces and remaining evidence operations. It is intentionally restricted to small instances.

## Metrics

- semantic status;
- number of obstruction pairs;
- exact fixed cost;
- greedy cost;
- greedy/exact ratio;
- adaptive worst-case cost;
- fixed/adaptive adaptivity gap;
- runtime for each algorithm.

## Reproducibility

Run:

```bash
python benchmarks/synthetic_suite.py --seeds 100
python benchmarks/summarize_results.py artifacts/synthetic_results.csv
```

The benchmark uses a local deterministic pseudorandom generator and no third-party Python dependencies.

## Interpretation discipline

Synthetic results establish algorithmic behavior under controlled finite models. They do not establish application utility by themselves. A publication-grade evaluation additionally requires realistic workloads and relevant baselines.
