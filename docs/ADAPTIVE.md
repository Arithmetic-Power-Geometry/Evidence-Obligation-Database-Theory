# Adaptive Evidence Policies

A fixed EOD obligation chooses an evidence set before any new outcome is observed.

An adaptive policy instead chooses the next operation as a function of earlier outcomes.

Formally, a policy is a rooted decision tree. Internal nodes are evidence operations, outgoing edges are observed outcomes, and every reachable leaf must be query-homogeneous.

For a world \(w\), let \(C(\pi,w)\) be the cost accumulated along its path. The worst-case objective is

\[
C^*_{\max}(q,H)
=
\min_{\pi}
\max_{w\in V_H}C(\pi,w).
\]

The reference implementation computes the exact optimum for small explicit finite states by dynamic programming over remaining worlds and unused evidence operations.

Adaptive policies matter because different outcomes can make different later observations unnecessary. Even when worst-case cost equals a fixed obligation, realized branch cost can be smaller.

Future extensions will add probability-weighted expected cost and approximation methods.
