# Compositionality Program

The next database-specific milestone is to determine whether EOD resolution semantics composes through relational algebra.

## Target setting

Let a database schema induce a finite set of admissible worlds. For relational expressions \(R,S\), investigate operators:

- selection \(\sigma_\phi(R)\);
- projection \(\pi_A(R)\);
- union \(R\cup S\);
- join \(R\bowtie S\);
- difference \(R-S\).

For each expression \(Q\), define a resolution object

\[
\mathcal R(Q,D)
\]

containing answer/candidate answers, obstruction, and obligation/certificate information.

## Central question

Does there exist an operator \(\odot\) such that for a relational constructor \(F\),

\[
\mathcal R(F(Q_1,Q_2),D)
=
\mathcal R(Q_1,D)\odot_F\mathcal R(Q_2,D)
\]

without reconstructing all underlying possible worlds?

## Why this matters

If such composition is possible for useful fragments, EOD gains a genuinely database-specific optimization principle: resolution metadata could propagate through a query plan similarly to other database annotations.

If composition is impossible from coarse resolution summaries, a negative theorem is also valuable: it identifies exactly what information an EOD query planner must preserve.

## First attack

Start with selection and projection over tuple-independent finite world representations.

Seek either:

1. a sound and complete compositional rule; or
2. two subqueries with identical local resolution summaries whose composed queries have different resolution status/obligations.

The second would prove that the chosen summary is insufficient for compositional evaluation.
