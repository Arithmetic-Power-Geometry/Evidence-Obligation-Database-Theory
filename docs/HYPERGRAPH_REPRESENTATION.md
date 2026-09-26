# Obligation-Hypergraph Representation

For query \(q\) and current history \(H\), define the obstruction universe

\[
U=\mathcal O_q(H).
\]

For each obstruction pair \(p=\{u,v\}\), define its admissible separator set

\[
T_p=\{e\in E_\Gamma:\Omega_e(u)\neq\Omega_e(v)\}.
\]

The family

\[
\mathcal H_q(H)=\{T_p:p\in U\}
\]

is the EOD obligation hypergraph.

## Theorem — Fixed-obligation representation

A set \(X\subseteq E_\Gamma\) is a sufficient fixed evidence obligation iff

\[
\forall p\in U,\quad X\cap T_p\neq\varnothing.
\]

Equivalently, sufficient obligations are exactly the transversals (hitting sets) of \(\mathcal H_q(H)\).

### Proof

By EOD semantics, \(X\) resolves the query iff every query-disagreeing pair \(p\) is separated by at least one selected operation. By definition, the operations that separate \(p\) are exactly \(T_p\). Thus the condition is exactly \(X\cap T_p\neq\varnothing\) for every hyperedge. ∎

## Corollary 1 — Impossibility

The query is unresolvable by fixed admissible evidence iff

\[
\exists p\in U:T_p=\varnothing.
\]

Thus an empty hyperedge is an impossibility certificate.

## Corollary 2 — Minimal obligations

Inclusion-minimal sufficient evidence obligations are exactly the minimal transversals of \(\mathcal H_q(H)\).

## Corollary 3 — Minimum-cost obligation

With evidence costs \(C(e)\), minimum EOD obligation is minimum-weight hypergraph transversal.

## Significance after the compositionality counterexample

The coarse signature theorem shows that status, possible answers, minimum cost, and obstruction count are insufficient for composition.

This theorem identifies the information they discarded: the incidence relation

\[
p\mapsto T_p.
\]

The obligation hypergraph is therefore a sufficient representation for all **fixed** resolution-obligation and impossibility questions in the finite deterministic model.

This does not yet prove that the hypergraph itself composes through every relational operator without access to underlying worlds. That is the next constructive problem.
