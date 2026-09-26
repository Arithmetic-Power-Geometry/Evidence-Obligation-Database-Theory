# Evidence-Obligation Database Theory (EOD)

> A finite database semantics in which state records not only current evidence, but also the evidence that can still be acquired to resolve a query.

**Version:** 1.0.0  
**Author:** Mohammad Amir Khusru Akhtar  
**Copyright © 2026 Mohammad Amir Khusru Akhtar**  
**License:** Apache License 2.0

## Core semantics

A finite EOD database is

[
mathbb D=(W,H,E,Omega,C,Gamma),
]

with admissible worlds (W), acquired evidence (H), evidence operations (E), deterministic outcomes (Omega), costs (C), and admissibility constraints (Gamma).

For query (q:W	o Y), current evidence induces version space (V_H). EOD distinguishes three typed outcomes:

```text
RESOLVED              -> answer certificate
ACQUIRABLY_RESOLVABLE -> evidence obligation / policy
UNRESOLVABLE          -> impossibility certificate
```

The query-relative obstruction is

[
mathcal O_q(H)={{u,v}subseteq V_H:q(u)
eq q(v)}.
]

An evidence operation separates a pair when its outcomes differ in the two worlds. A fixed obligation resolves the query exactly when it separates every obstruction pair.

## Minimum Evidence Obligation

For additive costs,

[
operatorname{MEO}(q,H)=
argmin_{Xsubseteq E_Gamma}sum_{ein X}C(e)
]

subject to

[
mathcal O_q(H)subseteqigcup_{ein X}S_e.
]

The reference implementation provides exact fixed search for small finite instances, exact adaptive worst-case planning, and a greedy weighted-cover planner.

## Main formal results

| Result | Statement |
|---|---|
| Capability separation | Same current query view need not imply the same future answerability. |
| Strict adaptivity gap | A finite witness has (C^*_{m fix}=3) and (C^*_{m ad}=2). |
| EOD-MEO NP-completeness | Minimum fixed evidence obligation is NP-complete even for a restricted binary deterministic fragment. |
| Sensing representation | Finite deterministic adaptive EOD policies translate cost-preservingly to conditional sensing policies. |
| Access-method translation | Qualitative answerability, costs, and static admissibility can be represented by finite access interfaces. |
| Coarse-composition impossibility | Status/answer/cost/obstruction-count summaries are insufficient to compose conjunction exactly. |
| Obligation hypergraph | Fixed sufficient obligations are precisely transversals of the obstruction-separator hypergraph. |
| Boolean composition | Signed query labels plus query-independent pairwise evidence incidence suffice for exact pointwise Boolean composition. |

These results deliberately narrow the novelty claim. Adaptive sensing, weighted set cover, minimum-cost testing, active information acquisition, possible worlds, provenance, and access-method planning are prior art and are **not** claimed as EOD inventions.

## Database-level contribution under study

The repository investigates a narrower abstraction:

> Treat future evidence capability as part of logical database state and make resolution artifacts—obstructions, obligations, policies, and impossibility witnesses—typed query-level objects.

This is a semantic/database abstraction claim, not a claim that EOD cannot be encoded using existing database or planning machinery.

## Algebra

The finite reference algebra includes:

| Operator | Meaning |
|---|---|
| `VIEW(D,q)` | current worlds and possible answers |
| `OBSTRUCT(D,q)` | answer-disagreeing world pairs |
| `SEPARATE(D,e)` | pairs distinguished by operation (e) |
| `OBLIGATE(D,q)` | minimum fixed evidence obligation |
| `ACQUIRE(D,e,o)` | refine state after evidence outcome (o) |
| `CERTIFY(D,q)` | answer, obligation, or impossibility certificate |

The package also exposes obligation-hypergraph and signed-composition APIs.

## Empirical evaluation

The formal guarantees belong to the finite deterministic EOD model. The real-data studies are **empirical analogues of progressive evidence acquisition**, not logical resolution proofs.

### Credit-card fraud: controlled feature-budget workload

A 284,807-transaction benchmark uses progressive feature budgets over `Time`, `Amount`, and anonymized PCA components. Because the PCA variables have no acquisition semantics, this workload is explicitly treated as a controlled proxy.

Key findings include:

- PR-AUC rises from 0.0018 at B0 to 0.7438 at B3 and 0.7439 at B4;
- some high-confidence early decisions reverse after later information;
- confidence-only and maturity-aware stopping produce different cost-quality frontiers;
- the trade-off is classifier-dependent;
- bootstrap analysis and a stopping-rule ablation are included.

See `docs/CREDITCARD_FIRST_RESULTS.md`, `docs/CREDITCARD_STOPPING_RESULTS.md`, and `docs/CREDITCARD_ROBUSTNESS.md`.

### UCI Default of Credit Card Clients: semantic-stage replication

The second workload contains 30,000 clients and interpretable evidence blocks:

[
	ext{profile/capacity}
ightarrow
	ext{repayment status}
ightarrow
	ext{bill history}
ightarrow
	ext{payment history}.
]

Repayment evidence supplies the dominant predictive gain, while individual decisions continue to change after aggregate performance largely saturates. Relative to the full final-stage decision, 6.68% of P1 decisions and 5.35% of P2 decisions differ.

The extreme-probability diagnostic from the first dataset does **not** replicate, and that negative result is retained. The cross-dataset message is therefore not a universal confidence threshold; it is the distinction between predictive saturation and decision/evidence maturity.

See `docs/UCI_DEFAULT_RESULTS.md`.

## Reproducibility

Install the finite core:

```bash
pip install -e .
python -m unittest discover -s tests -v
```

Run representative theorem witnesses and benchmarks:

```bash
python experiments/capability_separation.py
python experiments/strict_adaptivity_gap.py
python experiments/composition_witness.py
python benchmarks/exhaustive_binary_small.py
python benchmarks/synthetic_suite.py --seeds 100
```

GitHub Actions runs the regression suite, exhaustive finite audit, synthetic benchmark, and reproducibility artifact generation. The final v1.0 README commit passed the reproducibility workflow (run #55), including regression tests, exhaustive finite audit, the 100-seed synthetic suite, summary generation, and artifact upload.

## Repository map

```text
eod/                  finite reference implementation
tests/                theorem and regression tests
experiments/          executable witnesses
benchmarks/           exhaustive and synthetic evaluation
applications/         real-data workload protocols
artifacts/            frozen machine-readable results
docs/                 theory, proofs, comparisons, protocols, results
```

Important formal documents include:

- `docs/SEPARATION_THEOREM.md`
- `docs/NP_COMPLETENESS.md`
- `docs/REPRESENTATION_THEOREM.md`
- `docs/ACCESS_METHOD_RELATIONSHIP.md`
- `docs/COARSE_COMPOSITION_IMPOSSIBILITY.md`
- `docs/HYPERGRAPH_REPRESENTATION.md`
- `docs/BOOLEAN_COMPOSITION.md`
- `docs/Q1_READINESS.md`

## Claim boundaries

EOD does **not** claim to introduce:

- uncertainty or possible-world databases;
- active sensing or adaptive information acquisition;
- acquisitional query processing;
- minimum-cost test selection;
- weighted set cover or its approximation guarantee;
- provenance/why-not provenance;
- access-method answerability;
- conditional sensing or epistemic planning.

The exact relationship to these areas is part of the formal collision analysis in this repository. Historical novelty remains subject to literature review and peer review.

## Data

Raw third-party datasets are not redistributed. Application folders contain protocols and derived/frozen results only. Users should obtain source datasets from their original providers and follow the applicable terms.

## Citation

Citation metadata is provided in `CITATION.cff`.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
