# NP-Completeness of Fixed EOD Minimum Evidence Obligation

## Decision problem EOD-MEO

Input:

- a finite deterministic EOD database;
- a query \(q\);
- nonnegative integer evidence costs;
- a budget \(B\).

Question: is there an admissible fixed evidence set of total cost at most \(B\) that resolves \(q\)?

## Theorem

EOD-MEO is NP-complete, even when:

- history is empty;
- query answers are binary;
- evidence outcomes are binary;
- there is one query-0 anchor world;
- all other worlds have query value 1;
- all evidence operations are deterministic and admissible.

## Membership in NP

A certificate is a selected evidence subset \(X\).

In polynomial time we can:

1. sum its encoded costs;
2. enumerate every query-disagreeing world pair;
3. verify that at least one selected operation separates each such pair.

Hence EOD-MEO is in NP.

## NP-hardness

Reduce from Weighted Set Cover.

Given:

- universe \(U=\{1,\dots,n\}\);
- subsets \(S_1,\dots,S_m\subseteq U\);
- integer weights \(c_1,\dots,c_m\);
- budget \(B\),

construct worlds

\[
W=\{a,u_1,\dots,u_n\}.
\]

Define

\[
q(a)=0,\qquad q(u_i)=1.
\]

Because all \(u_i\) share the same query value, the obstruction set is exactly

\[
\mathcal O_q=\{\{a,u_i\}:i\in U\}.
\]

For each set \(S_j\), construct binary evidence operation \(e_j\):

\[
\Omega_{e_j}(a)=0,
\]

and

\[
\Omega_{e_j}(u_i)=
\begin{cases}
1,&i\in S_j,\\
0,&i\notin S_j.
\end{cases}
\]

Set \(C(e_j)=c_j\).

Then \(e_j\) separates obstruction pair \(\{a,u_i\}\) iff \(i\in S_j\).

Therefore an evidence subset resolves \(q\) iff the corresponding family of sets covers \(U\), and costs are identical.

Thus there is a set cover of cost at most \(B\) iff there is an EOD fixed obligation of cost at most \(B\).

The construction is polynomial, proving NP-hardness. Together with membership in NP, EOD-MEO is NP-complete. ∎

## Interpretation

The hardness is inherited from covering structure; weighted set cover itself is not an EOD novelty.

The result matters because it formally justifies:

- exact exponential solvers for small instances;
- approximation algorithms for larger instances;
- investigation of tractable structural fragments.
