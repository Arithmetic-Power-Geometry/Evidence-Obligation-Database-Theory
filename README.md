# Evidence-Obligation Database Theory (EOD)

> A proposed database model in which a database state is defined not only by what it currently knows, but also by what it can still learn.

**Author:** Mohammad Amir Khusru Akhtar  
**Copyright © 2026 Mohammad Amir Khusru Akhtar**  
**License:** Apache License 2.0

## Core idea

Conventional database queries primarily map a stored database state to an answer. In incomplete or uncertain settings they may instead expose certain answers, possible answers, nulls, confidence, provenance, or missing-answer explanations.

EOD introduces a different native query result:

```text
QUERY
  -> ANSWER CERTIFICATE
  -> EVIDENCE OBLIGATION
  -> IMPOSSIBILITY CERTIFICATE
```

The central proposal is:

> **Future evidence-generating capability is part of database state.**

Two systems may contain identical current facts yet be different EOD databases if they have different abilities to acquire evidence that resolves future queries.

## Formal model

A finite EOD database is

\[
\mathbb D=(W,H,E,\Omega,C,\Gamma),
\]

where:

- \(W\): admissible worlds;
- \(H\): currently acquired evidence;
- \(E\): evidence-producing operations;
- \(\Omega_e(w)\): outcome of operation \(e\) in world \(w\);
- \(C(e)\): acquisition cost;
- \(\Gamma\): admissibility constraints.

For a query \(q:W\to Y\), current evidence induces the version space

\[
V_H=\{w\in W:w\text{ is consistent with }H\}.
\]

The query is resolved exactly when all worlds in \(V_H\) agree on its answer.

## Resolution obstruction

EOD keeps only ambiguity that matters to the requested query:

\[
\mathcal O_q(H)
=
\{\{u,v\}\subseteq V_H:q(u)\neq q(v)\}.
\]

For evidence operation \(e\),

\[
S_e
=
\{\{u,v\}:\Omega_e(u)\neq\Omega_e(v)\}.
\]

A set of future evidence operations resolves the query if it separates every query-disagreeing pair.

## Minimum Evidence Obligation

For additive acquisition cost,

\[
\operatorname{MEO}(q,H)
=
\arg\min_{X\subseteq E_\Gamma}
\sum_{e\in X}C(e)
\]

subject to

\[
\mathcal O_q(H)
\subseteq
\bigcup_{e\in X}S_e.
\]

The exact finite implementation in this repository searches this obligation exhaustively. It is a semantic reference engine, not yet a scalable optimizer.

## Native query-result trichotomy

An EOD query returns one of three semantic outcomes:

| Status | Meaning | Native result |
|---|---|---|
| **RESOLVED** | Current evidence already determines the answer | Answer certificate |
| **ACQUIRABLY_RESOLVABLE** | Ambiguity remains but admissible evidence can remove it | Minimum evidence obligation |
| **UNRESOLVABLE** | Some answer-disagreeing worlds cannot be separated by any admissible operation | Impossibility certificate |

This distinction is stronger than returning a generic unknown value.

## Resolution antiprovenance

Traditional provenance is backward-facing:

\[
\text{existing evidence}\rightarrow\text{answer}.
\]

EOD adds a forward-facing dual:

\[
\text{unresolved query}\rightarrow\text{future evidence sufficient for resolution}.
\]

This repository calls that object **resolution antiprovenance**.

## What is already known

EOD does **not** claim that the following ideas are new:

- possible-world and incomplete-database semantics;
- certain answers;
- query completeness;
- provenance or why-not provenance;
- sensor/acquisitional query processing;
- minimum-cost test selection;
- experimental design or active information acquisition.

Those areas are explicit prior art.

The current research hypothesis is narrower:

> **A useful database model can make evidence-generating capability part of logical database state, while unresolved queries natively denote resolution obligations or impossibility certificates.**

See [docs/PRIOR_ART.md](docs/PRIOR_ART.md).

## Comparison with established paradigms

| Paradigm | Typical primitive output for incomplete knowledge | What EOD adds |
|---|---|---|
| Relational DB | tuples / relations | Prospective resolution semantics |
| Incomplete DB | possible or certain answers | Future evidence obligations |
| Probabilistic DB | answer probabilities | Separability without requiring probability |
| Provenance system | derivation/explanation | Forward resolution antiprovenance |
| Why-not provenance | explanation for missing output | Evidence sufficient to make target invariant |
| Acquisitional DB | optimized acquisition/sampling | Acquisition capability as logical DB state |
| EOD | certificate / obligation / impossibility certificate | Native future-answerability semantics |

This is a **semantic comparison**, not a claim that EOD cannot be encoded on top of a relational DBMS.

## Working reference software

The repository includes a zero-dependency Python reference engine:

```text
eod/
  model.py       finite worlds + evidence operations
  engine.py      obstruction, exact obligation search, certificates
examples/
  clinical_demo.py
benchmarks/
  compare_models.py
tests/
  test_eod.py
docs/
  THEORY.md
  PRIOR_ART.md
```

Run:

```bash
python examples/clinical_demo.py
python benchmarks/compare_models.py
python -m unittest discover -s tests -v
```

## Example

Suppose three admissible worlds imply:

| World | Decision | Test A | Test B |
|---|---|---:|---:|
| w1 | A | 0 | 0 |
| w2 | B | 1 | 0 |
| w3 | B | 1 | 1 |

If Test A costs 2 and Test B costs 1, the target decision is currently ambiguous.

Test B does not separate w1 from w2. Test A separates every pair that disagrees on the decision.

EOD therefore returns conceptually:

```text
status: ACQUIRABLY_RESOLVABLE
possible_answers: [A, B]
minimum_obligation: [Test A]
minimum_cost: 2
```

After observing Test A = 1, only worlds w2 and w3 remain and both give answer B:

```text
status: RESOLVED
answer: B
```

If two answer-disagreeing worlds produce the same outcome under every admissible evidence operation, EOD instead returns an impossibility certificate identifying that inseparable pair.

## Why the benchmark matters

The included benchmark is intentionally **not a speed benchmark**. It puts the same finite-world problem through four semantic views:

1. relational-style storage;
2. possible answers;
3. certain-answer semantics;
4. EOD resolution semantics.

Its purpose is to make the proposed benefit concrete: EOD does not merely say that an answer is currently uncertain; it determines whether the uncertainty is **resolvable**, identifies a minimum evidence obligation when it is, and provides a witness when it is not.

## First formal separation result

EOD now has an executable **Capability-Separation Theorem**.

There exist two finite databases \(\mathbb D_+\) and \(\mathbb D_-\) with exactly the same current version space and exactly the same query values on that space, yet

\[
\operatorname{RS}(\mathbb D_+,q)
=
\mathrm{ACQUIRABLY\_RESOLVABLE}
\]

while

\[
\operatorname{RS}(\mathbb D_-,q)
=
\mathrm{UNRESOLVABLE}.
\]

The difference is solely their admissible evidence capability. Therefore:

\[
\boxed{\text{same current knowledge}\;\not\Rightarrow\;\text{same future answerability}}
\]

This proves that future answerability is not determined by the current query view alone. It does **not** claim that conventional DBMS software cannot encode evidence metadata.

See [docs/SEPARATION_THEOREM.md](docs/SEPARATION_THEOREM.md) and run:

```bash
python experiments/capability_separation.py
```

The seven finite-core axioms are in [docs/AXIOMS.md](docs/AXIOMS.md).

## Complexity boundary

For an explicit finite EOD instance, the non-adaptive minimum-evidence problem can be represented as weighted covering over the query-obstruction pairs. The exact engine is therefore intentionally a small-instance semantic oracle rather than a production optimizer.

See [docs/COMPLEXITY.md](docs/COMPLEXITY.md) and:

```bash
python benchmarks/scaling_exact.py
```

## Research questions now made executable

The repository turns the proposal into falsifiable questions:

1. Can evidence capability be treated as a first-class logical component of DB state?
2. Can answer certificates, obligations, and impossibility certificates form a closed algebra?
3. What fragments admit polynomial-time evaluation?
4. What is the exact expressive relationship to incomplete and acquisitional databases?
5. When are two databases equivalent with respect to both current answers and future answerability?
6. How should adaptive, noisy, temporal, and authorization-dependent evidence be represented?

## Current status

**v0.2 — axiomatized finite theory + capability-separation theorem + exact reference engine + semantic and complexity benchmarks.**

This repository establishes the concept and makes it executable. It does **not** yet claim historical proof that EOD is a new canonical database model; that requires a fuller literature review, formal separation results, and peer review.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff).

## License

Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
