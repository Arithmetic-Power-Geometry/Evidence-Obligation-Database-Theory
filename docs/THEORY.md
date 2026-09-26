# EOD Theory v0.1

## Primitive model

A finite Evidence-Obligation Database is

\[
\mathbb D=(W,H,E,\Omega,C,\Gamma).
\]

- \(W\): admissible worlds.
- \(H\): acquired evidence history.
- \(E\): evidence-producing operations.
- \(\Omega_e(w)\): outcome of operation \(e\) in world \(w\).
- \(C(e)\): acquisition cost.
- \(\Gamma\): admissibility constraints.

For query \(q:W\to Y\), current history induces

\[
V_H=\{w\in W:w\text{ agrees with }H\}.
\]

The query is resolved iff \(|\{q(w):w\in V_H\}|=1\).

## Resolution obstruction

\[
\mathcal O_q(H)=\{\{u,v\}\subseteq V_H:q(u)\neq q(v)\}.
\]

This retains only ambiguity relevant to the requested query.

For each evidence operation,

\[
S_e=\{\{u,v\}:\Omega_e(u)\neq\Omega_e(v)\}.
\]

A non-adaptive evidence set \(X\) guarantees resolution iff

\[
\mathcal O_q(H)\subseteq\bigcup_{e\in X}S_e.
\]

## Minimum Evidence Obligation

\[
\operatorname{MEO}(q,H)=
\arg\min_{X\subseteq E_\Gamma}\sum_{e\in X}C(e)
\]

subject to coverage of all query-disagreeing pairs.

The finite exact optimization is a weighted covering problem. That optimization structure is not itself claimed as novel.

## Resolution trichotomy

A finite query is exactly one of:

- **RESOLVED**: \(\mathcal O_q(H)=\varnothing\).
- **ACQUIRABLY_RESOLVABLE**: every obstruction pair can be separated by admissible evidence.
- **UNRESOLVABLE**: some query-disagreeing pair is inseparable by every admissible operation.

An inseparable disagreeing pair is an impossibility certificate.

## Resolution antiprovenance

Define

\[
\operatorname{AntiProv}(q,H)=
\{X\subseteq E_\Gamma:
\mathcal O_q(H)\subseteq\bigcup_{e\in X}S_e\}.
\]

Its minimal elements are minimal evidence obligations.

This is prospective: it maps an unresolved target to future evidence sufficient for query invariance.

## Capability-sensitive equivalence

Two databases may have the same materialized facts but differ in evidence capability. EOD therefore distinguishes current knowledge from future answerability.

For a query family \(\mathcal Q\), a future research objective is a canonical resolution signature capturing:

- current possible answers;
- obstruction structure;
- minimal resolution obligations;
- irreducible obstruction certificates.

This supplies the basis for capability-sensitive database equivalence.

## Immediate research program

1. Adaptive evidence policies.
2. Algebra over answer/obligation/certificate objects.
3. Complexity bounds for restricted evidence languages.
4. Formal embeddings into incomplete databases.
5. Separation results showing where explicit evidence-capability semantics is useful.
6. Noisy, probabilistic, temporal, and authorization-dependent observations.
