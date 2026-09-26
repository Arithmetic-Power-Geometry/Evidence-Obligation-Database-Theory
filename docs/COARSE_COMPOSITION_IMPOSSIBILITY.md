# Coarse Resolution Summaries Are Not Compositionally Complete

## Coarse signature

For a Boolean query \(f\), define

\[
S_D(f)=
(\operatorname{status},
\operatorname{possibleAnswers},
\operatorname{minimumCost},
|\mathcal O_f|).
\]

This summary records useful local resolution information but forgets which world pairs each evidence operation separates.

## Theorem

There is no function \(F\) such that for all finite deterministic EOD databases and Boolean queries \(q,r\),

\[
S_D(q\land r)=F(S_D(q),S_D(r)).
\]

## Witness

Use four worlds \(w_1,w_2,w_3,w_4\) with

\[
q=(0,0,1,1),\qquad r=(0,1,0,1).
\]

Thus \(q\land r=(0,0,0,1)\).

All evidence operations below have unit cost.

### Database \(D_1\)

\[
e_1=(0,0,0,1),\qquad e_2=(1,1,0,0).
\]

### Database \(D_2\)

\[
f_1=(0,0,1,0),\qquad f_2=(0,0,1,1).
\]

Direct finite evaluation gives, in both databases,

\[
S(q)=(\mathrm{ACQUIRABLY\_RESOLVABLE},\{0,1\},1,4)
\]

and

\[
S(r)=(\mathrm{UNRESOLVABLE},\{0,1\},\bot,4).
\]

However,

\[
S_{D_1}(q\land r)
=
(\mathrm{ACQUIRABLY\_RESOLVABLE},\{0,1\},1,3),
\]

whereas

\[
S_{D_2}(q\land r)
=
(\mathrm{ACQUIRABLY\_RESOLVABLE},\{0,1\},2,3).
\]

Hence the two inputs to any proposed \(F\) are identical while the required outputs differ. Contradiction. ∎

## Interpretation

Local status, possible answers, minimum cost, and obstruction cardinality discard evidence-to-obstruction incidence information needed by composition.

Therefore a compositional EOD optimizer must retain a richer annotation.

## What this theorem does not prove

It does not show that EOD resolution semantics is inherently non-compositional.

It proves only that this **coarse signature** is not compositionally complete.

The constructive next target is to identify a sufficient annotation, with the obstruction/evidence incidence hypergraph as the leading candidate.
