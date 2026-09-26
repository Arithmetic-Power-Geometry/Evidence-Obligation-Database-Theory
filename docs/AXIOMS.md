# EOD Axioms v0.2

These axioms define the finite deterministic core of Evidence-Obligation Database Theory.

## Axiom 1 — World semantics

At every query point there is a nonempty admissible set of worlds \(W\). Current evidence history \(H\) determines a version space \(V_H\subseteq W\).

## Axiom 2 — Query extensionality

A query \(q\) assigns an answer to each admissible world:

\[
q:W\to Y.
\]

Current resolution depends only on the restriction \(q|_{V_H}\).

## Axiom 3 — Evidence capability

A database state may contain admissible evidence-producing operations. Each operation \(e\) has an outcome map

\[
\Omega_e:W\to O_e.
\]

Thus a database describes both materialized evidence and potential evidence.

## Axiom 4 — Observational refinement

Observing outcome \(o\) of operation \(e\) updates the version space to

\[
V_{H'}=\{w\in V_H:\Omega_e(w)=o\}.
\]

Therefore evidence acquisition refines, rather than enlarges, the current version space.

## Axiom 5 — Query-relative resolution

A query is resolved exactly when

\[
\forall u,v\in V_H,\quad q(u)=q(v).
\]

Complete world identification is not required.

## Axiom 6 — Resolution obligation

If the query is unresolved but every query-disagreeing pair is separable by some admissible evidence operation, the database may return a sufficient evidence set or policy as a first-class query result.

## Axiom 7 — Impossibility certification

If there exists \(u,v\in V_H\) such that

\[
q(u)\neq q(v)
\]

and

\[
\Omega_e(u)=\Omega_e(v)
\quad\forall e\in E_\Gamma,
\]

then the query is unresolvable under the current admissible evidence capability, and \(\{u,v\}\) is an impossibility certificate.

## Design consequence

A database state is not characterized solely by its materialized facts. Its evidence capability can change the semantic class of an unresolved query without changing any currently stored observation.
