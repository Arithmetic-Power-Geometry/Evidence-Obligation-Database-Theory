# Finite EOD Representation Theorem

## Setup

Let

\[
D=(W,H,E,\Omega,C,\Gamma)
\]

be a finite deterministic EOD database and let \(q:W\to Y\).

Construct a finite sensing problem \(P(D,q)\) as follows:

- hidden states are the current worlds \(V_H\);
- the goal label of state \(w\) is \(q(w)\);
- every admissible evidence operation \(e\in E_\Gamma\) is a sensing action;
- executing \(e\) in state \(w\) observes \(\Omega_e(w)\);
- sensing does not change the hidden world;
- action cost is \(C(e)\);
- a belief state is terminal exactly when all worlds in it share the same query label.

## Theorem — Resolution-policy correspondence

For every finite deterministic EOD instance \((D,q)\):

1. a deterministic adaptive EOD policy guarantees query resolution iff the corresponding sensing policy reaches a query-homogeneous belief state on every reachable observation branch;
2. corresponding policies have identical path costs;
3. therefore their optimal worst-case costs are equal.

### Proof

Initially both systems have belief/version space \(V_H\).

Suppose corresponding executions have the same current set \(B\subseteq V_H\). Executing evidence operation/sensing action \(e\) and observing outcome \(o\) updates both systems to

\[
B' = \{w\in B:\Omega_e(w)=o\}.
\]

Thus by induction on policy depth, every corresponding observation history induces the same remaining world set.

An EOD leaf resolves \(q\) exactly when \(q\) is constant on its remaining worlds. The constructed sensing problem uses exactly the same terminal condition. Hence one policy succeeds on every branch iff the other does.

The action/evidence costs are copied unchanged, so every corresponding root-to-leaf path has identical cost. Taking maxima over branches and minima over successful policies preserves the optimum. ∎

## Corollary — Adaptive planning itself is not an EOD novelty

Finite deterministic adaptive EOD resolution can be represented as conditional sensing over a belief state.

Therefore neither outcome-contingent evidence policies nor their optimal worst-case cost should be claimed as fundamentally new planning machinery.

## Corollary — Where EOD must earn its contribution

Any distinct contribution must come from the **database abstraction and semantics**, such as:

- making evidence capability a typed component of database state;
- query-relative obstruction objects;
- obligation/certificate query outputs;
- compositional database operators;
- integration with relational/incomplete query semantics;
- database-specific optimization or representation results.

## Scientific consequence

This theorem narrows the novelty claim but strengthens the project: it identifies an exact bridge to established planning theory instead of relying on terminology differences.
