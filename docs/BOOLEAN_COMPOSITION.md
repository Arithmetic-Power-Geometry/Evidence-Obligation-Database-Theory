# Boolean Composition of EOD Obstructions

Let \(q,r:V_H\to\{0,1\}\) be Boolean queries.

For a query \(f\), its obstruction set is

\[
\mathcal O_f=\{\{u,v\}:f(u)\neq f(v)\}.
\]

## Important limitation

The obligation hypergraph \(\mathcal H_f\) records evidence separators for pairs already known to obstruct \(f\). By itself it does **not** retain the truth value \(f(w)\) of each world.

For Boolean composition, child truth labels matter.

## Signed obstruction annotation

Define the signed query annotation

\[
\mathcal S_f=(V_H,f|_{V_H},I),
\]

where \(I(u,v)\) is the evidence-separator incidence map

\[
I(u,v)=\{e:\Omega_e(u)\neq\Omega_e(v)\}.
\]

The incidence map is query-independent; the query label map determines which pairs become obstructions.

## Theorem — Boolean compositional sufficiency

Given signed annotations for \(q\) and \(r\) over the same current world set and evidence-incidence map, the complete obligation hypergraph for any pointwise Boolean connective

\[
b(q,r)
\]

can be computed without invoking evidence outcomes again.

### Construction

For every pair \(u,v\), compute

\[
b(q(u),r(u)),\qquad b(q(v),r(v)).
\]

The pair is an obstruction exactly when these values differ. If it is an obstruction, attach the already-known separator set \(I(u,v)\).

Thus

\[
\mathcal H_{b(q,r)}
=
\{I(u,v):b(q(u),r(u))\neq b(q(v),r(v))\}.
\]

### Proof

The construction applies the definition of query obstruction directly. Evidence separation depends only on the two worlds and evidence operations, not on the query. Therefore the stored incidence set for every newly obstructing pair is exactly the separator set required by EOD semantics. ∎

## Corollaries

The construction applies to:

- negation;
- conjunction;
- disjunction;
- XOR;
- implication;
- every finite Boolean truth function.

For negation,

\[
\mathcal O_{\neg q}=\mathcal O_q,
\]

so its obligation hypergraph is unchanged.

## Negative lesson

The unsigned obligation hypergraphs \(\mathcal H_q,\mathcal H_r\) alone are generally insufficient for arbitrary Boolean composition because they omit:

1. orientation/truth labels of the induced bipartitions;
2. separator incidence for pairs that are non-obstructions locally but may become relevant after composition.

Hence a compositional optimizer needs a richer reusable annotation than only local obstruction hyperedges.

## Database significance

This establishes a first exact compositional fragment:

> finite deterministic Boolean EOD queries compose exactly when the planner carries world-level query labels plus reusable evidence-pair incidence.

The next challenge is compression: determine the coarsest annotation that preserves this property without retaining all pairwise world information.
