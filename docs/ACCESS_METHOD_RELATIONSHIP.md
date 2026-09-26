# EOD and Access-Method Answerability

## Scope

This note compares the finite deterministic EOD core with a deliberately explicit finite access-interface abstraction. It does **not** claim equivalence with every formalism called access methods in the database literature.

## Finite access-interface model

Let

\[
A=(W,H,M,\rho)
\]

where:

- \(W\) is a finite set of admissible worlds;
- \(H\) is the current observation history;
- \(M\) is a set of callable access methods;
- \(\rho_m(w)\) is the deterministic response returned by method \(m\) in world \(w\).

For query \(q:W\to Y\), an access policy is successful when every response branch terminates in a set of worlds on which \(q\) is constant.

This abstraction intentionally captures the information-discrimination core and omits richer relational constraints, bindings, result bounds, and access syntax.

## Theorem 1 — Qualitative translation

For every finite deterministic EOD instance

\[
D=(W,H,E,\Omega,C,\Gamma)
\]

and query \(q\), construct an access-interface instance \(A_D\) by:

- retaining \(W,H,q\);
- creating one method \(m_e\) for every admissible \(e\in E_\Gamma\);
- defining \(\rho_{m_e}(w)=\Omega_e(w)\).

Then an adaptive EOD policy resolves \(q\) iff the corresponding access policy resolves \(q\).

### Proof

Both executions begin with the same current world set. Under corresponding evidence operation/method \(e\), outcome \(o\) refines the current set to

\[
\{w:\Omega_e(w)=o\}
=
\{w:\rho_{m_e}(w)=o\}.
\]

Induction over response histories therefore gives identical remaining-world sets at every corresponding node. Terminality is the same condition—constancy of \(q\)—so success is preserved. ∎

## Consequence

Qualitative future answerability alone is **not** sufficient to distinguish finite deterministic EOD from an access-interface view.

Therefore EOD must not claim novelty merely because it asks whether future information can resolve a query.

## Theorem 2 — Costed translation under enriched access methods

Extend the access-interface model with a cost \(c(m)\) and copy

\[
c(m_e)=C(e).
\]

Then corresponding policies have identical path costs. Hence minimum worst-case resolution cost is preserved.

### Consequence

Cost-aware adaptive resolution is also representable once access methods are enriched with the same costs.

Cost alone is therefore not an expressiveness separation.

## Theorem 3 — Admissibility translation

Static EOD admissibility can be represented by omitting inadmissible evidence operations from \(M\). Therefore static authorization/admissibility alone is not a separation either.

History-dependent admissibility remains outside this finite static theorem.

## What is not established by these translations

The translations above do not establish that standard database access-method formalisms natively return:

1. the complete query-relative obstruction object;
2. all minimal evidence obligations;
3. a minimum-cost obligation as a typed query result;
4. an inseparable query-disagreeing pair as an impossibility certificate;
5. a compositional algebra over these objects.

But failure to be *native* is an API/semantic-design distinction, not automatically an expressive-power distinction. These objects may be derivable by meta-level analysis of the access model.

## Surviving contribution after the access-method attack

The defensible EOD thesis is now:

> EOD is a database-native **resolution semantics and algebra** that reifies future answerability artifacts—obstructions, obligations, policies, and impossibility witnesses—as typed query results over a state containing both current evidence and evidence capability.

This is a claim about database abstraction, compositional semantics, optimization targets, and certificates. It is not a claim that access methods or sensing plans cannot encode the same finite information.

## Next formal target

The strongest remaining theory question is **compositionality**:

Can resolution objects be composed through relational operators without re-solving the complete world-level problem?

A positive result would be database-specific and much more significant than another planning equivalence.
