# Evidence-Obligation Database Theory (EOD)

> A finite database semantics in which state records not only current evidence, but also the evidence that can still be acquired to resolve a query.

**Version:** 1.0.0  
**Author:** Mohammad Amir Khusru Akhtar  
**Copyright © 2026 Mohammad Amir Khusru Akhtar**  
**License:** Apache License 2.0  
**Archival research release:** [Evidence-Obligation Database Theory: What Must Be Learned to Resolve an Unknown Query](https://doi.org/10.5281/zenodo.22980041)

## Research trajectory

EOD began as a formal question about unresolved database queries: when an answer is not yet determined, is decisive evidence still obtainable, and if so, what is the least evidence needed to resolve the query?

The finite semantics and its mathematical objects were developed first. They were then implemented as a reference software package with executable theorem witnesses, tests, exact and approximate planners, benchmark generators, and reproducibility workflows. The v1.0 software release and its machine-readable artifacts provide the computational basis for the archived research paper.

The repository is therefore the implementation and reproducibility record of the theory, rather than a code package reconstructed from the manuscript.

## Core semantics

A finite EOD database is

$$
\mathbb{D}=(W,H,E,\Omega,C,\Gamma),
$$

where \(W\) is the finite set of admissible worlds, \(H\) is acquired evidence, \(E\) is the set of evidence-producing operations, \(\Omega_e(w)\) is the deterministic outcome of operation \(e\) in world \(w\), \(C(e)\) is acquisition cost, and \(\Gamma\) specifies admissibility.

For a query \(q:W\to Y\), current evidence induces the version space \(V_H\). EOD distinguishes three typed outcomes:

\`\`\`text
RESOLVED              -> answer certificate
ACQUIRABLY_RESOLVABLE -> evidence obligation / policy
UNRESOLVABLE          -> impossibility certificate
\`\`\`

The query-relative obstruction is

$$
\mathcal{O}_q(H)=\{\{u,v\}\subseteq V_H:q(u)\neq q(v)\}.
$$

For evidence operation \(e\),

$$
S_e=\{\{u,v\}:\Omega_e(u)\neq\Omega_e(v)\}.
$$

A fixed evidence set \(X\) resolves the query exactly when

$$
\mathcal{O}_q(H)\subseteq\bigcup_{e\in X}S_e.
$$

## Minimum Evidence Obligation

For additive costs,

$$
\operatorname{MEO}(q,H)=
\arg\min_{X\subseteq E_\Gamma}\sum_{e\in X}C(e)
$$

subject to

$$
\mathcal{O}_q(H)\subseteq\bigcup_{e\in X}S_e.
$$

The reference implementation provides exact fixed search for small finite instances, exact adaptive worst-case planning, and a greedy weighted-cover planner.

## Main formal results

| Result | Statement |
|---|---|
| Capability separation | The same current query view need not imply the same future answerability. |
| Strict adaptivity gap | A finite witness has \(C^*_{\mathrm{fix}}=3\) and \(C^*_{\mathrm{ad}}=2\). |
| EOD-MEO NP-completeness | Minimum fixed evidence obligation is NP-complete even for a restricted binary deterministic fragment. |
| Hypergraph representation | Fixed sufficient obligations are precisely transversals of the obstruction-separator hypergraph. |
| Sensing representation | Finite deterministic adaptive EOD policies translate cost-preservingly to conditional sensing policies. |
| Coarse-composition impossibility | Status/answer/cost/obstruction-count summaries are insufficient to compose conjunction exactly. |
| Boolean composition | Signed query labels plus query-independent pairwise evidence incidence suffice for exact pointwise Boolean composition. |

These results place EOD relative to established structures rather than treating those structures as new. Weighted covering explains fixed obligation optimization, and conditional sensing captures the adaptive finite planning problem. The EOD contribution is the database-level resolution semantics that makes obstructions, obligations, policies, and impossibility witnesses explicit query-level objects.

## Database-level contribution

The central abstraction is:

> Treat future evidence capability as part of logical database state and make resolution artifacts—obstructions, obligations, policies, and impossibility witnesses—typed query-level objects.

This makes it possible to distinguish an answer that is currently unknown but resolvable from one that cannot be resolved under the admissible evidence regime.

## Algebra

| Operator | Meaning |
|---|---|
| \`VIEW(D,q)\` | current worlds and possible query answers |
| \`OBSTRUCT(D,q)\` | query-disagreeing world pairs |
| \`SEPARATE(D,e)\` | world pairs distinguished by evidence operation \(e\) |
| \`OBLIGATE(D,q)\` | minimum fixed evidence obligation, if one exists |
| \`ACQUIRE(D,e,o)\` | refined state after observing outcome \(o\) |
| \`CERTIFY(D,q)\` | answer, evidence obligation, or impossibility certificate |

The package also exposes obligation-hypergraph and signed-composition APIs.

## Empirical evaluation

The formal guarantees belong to the finite deterministic EOD model. The real-data studies are empirical analogues of progressive evidence acquisition, not logical resolution proofs.

### Credit-card fraud: controlled feature-budget workload

A 284,807-transaction benchmark uses progressive feature budgets over \`Time\`, \`Amount\`, and anonymized PCA components. Because the PCA variables have no acquisition semantics, this workload is treated as a controlled feature-budget proxy.

Key results include:

- PR-AUC rises from 0.0018 at B0 to 0.7438 at B3 and 0.7439 at B4;
- some high-confidence early decisions reverse after later information;
- confidence-only and maturity-aware stopping induce different cost-quality frontiers;
- the trade-off is classifier-dependent;
- bootstrap analysis and a stopping-rule ablation are included.

See \`docs/CREDITCARD_FIRST_RESULTS.md\`, \`docs/CREDITCARD_STOPPING_RESULTS.md\`, and \`docs/CREDITCARD_ROBUSTNESS.md\`.

### UCI Default of Credit Card Clients: semantic-stage replication

The second workload contains 30,000 clients and uses interpretable evidence blocks:

$$
\text{profile/capacity}
\rightarrow
\text{repayment status}
\rightarrow
\text{bill history}
\rightarrow
\text{payment history}.
$$

Repayment evidence supplies the dominant predictive gain, while individual decisions continue to change after aggregate performance largely saturates. Relative to the final P3 decision, 6.68% of P1 decisions and 5.35% of P2 decisions differ.

The extreme-probability diagnostic from the first dataset does not replicate. This negative result is retained. The cross-dataset conclusion is therefore deliberately narrower: confidence thresholds are model- and dataset-specific, while staged evidence can continue to change decisions after aggregate predictive performance has nearly saturated.

See \`docs/UCI_DEFAULT_RESULTS.md\`.

## Reproducibility

Install the finite core:

\`\`\`bash
pip install -e .
python -m unittest discover -s tests -v
\`\`\`

Run representative theorem witnesses and benchmarks:

\`\`\`bash
python experiments/capability_separation.py
python experiments/strict_adaptivity_gap.py
python experiments/composition_witness.py
python benchmarks/exhaustive_binary_small.py
python benchmarks/synthetic_suite.py --seeds 100
\`\`\`

GitHub Actions runs the regression suite, exhaustive finite audit, synthetic benchmark, summary generation, and reproducibility artifact generation. The v1.0 software release was validated through this workflow.

## Repository map

\`\`\`text
eod/                  finite reference implementation
tests/                theorem and regression tests
experiments/          executable witnesses
benchmarks/           exhaustive and synthetic evaluation
applications/         real-data workload protocols
artifacts/            frozen machine-readable results
docs/                 theory, proofs, comparisons, protocols, results
\`\`\`

Formal documentation includes:

- \`docs/SEPARATION_THEOREM.md\`
- \`docs/NP_COMPLETENESS.md\`
- \`docs/REPRESENTATION_THEOREM.md\`
- \`docs/ACCESS_METHOD_RELATIONSHIP.md\`
- \`docs/COARSE_COMPOSITION_IMPOSSIBILITY.md\`
- \`docs/HYPERGRAPH_REPRESENTATION.md\`
- \`docs/BOOLEAN_COMPOSITION.md\`

## Scope and relationship to established methods

EOD is a database-level resolution semantics rather than a replacement for possible-world databases, provenance, acquisitional query processing, access-method answerability, active sensing, minimum-cost testing, weighted covering, or conditional sensing. The repository includes explicit correspondences and boundary results so that EOD objects can be interpreted relative to these established formalisms.

## Data

Raw third-party datasets are not redistributed. Application folders contain protocols and derived or frozen results only. Source datasets should be obtained from their original providers under the applicable terms.

## Citation

Please cite the archival V1 research release as:

> Akhtar, M. A. K. (2026). *Evidence-Obligation Database Theory: What Must Be Learned to Resolve an Unknown Query* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22980041

Machine-readable citation metadata is provided in \`CITATION.cff\`.

## License

Apache License 2.0. See \`LICENSE\` and \`NOTICE\`.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
