# Complexity of Finite Non-Adaptive EOD Resolution

## Decision problem

Define **EOD-MEO**:

**Input:** a finite EOD state, query \(q\), nonnegative evidence costs, and budget \(B\).

**Question:** does there exist an admissible evidence set \(X\) with

\[
\sum_{e\in X}C(e)\le B
\]

that separates every query-disagreeing pair in \(\mathcal O_q(H)\)?

## Membership in NP

Given a candidate evidence set \(X\), we can verify its total cost and test every obstruction pair against the operations in \(X\) in polynomial time in the explicit finite representation.

Therefore EOD-MEO is in NP.

## Cover formulation

Construct a universe

\[
U=\mathcal O_q(H).
\]

Each admissible evidence operation \(e\) contributes the subset

\[
S_e\cap U
\]

of obstruction pairs it separates.

Then a sufficient non-adaptive evidence obligation is exactly a set of operations whose separation subsets cover \(U\).

Thus finite non-adaptive EOD obligation minimization is an instance of weighted set cover over the query-obstruction universe.

## Complexity consequence

The generic explicit finite optimization inherits the computational hardness of weighted covering. The reference engine therefore uses exact exhaustive search only as a transparent semantic oracle for small instances.

This document intentionally avoids claiming that every EOD fragment is hard. Structured evidence families may admit polynomial algorithms, parameterized algorithms, approximation guarantees, or compact symbolic methods.

## Research directions

1. Greedy approximation for large finite instances.
2. Fixed-parameter algorithms in obstruction size.
3. Laminar or interval separation families.
4. Bounded outcome alphabets.
5. Adaptive policies and decision-tree complexity.
6. Symbolic worlds rather than explicit enumeration.
