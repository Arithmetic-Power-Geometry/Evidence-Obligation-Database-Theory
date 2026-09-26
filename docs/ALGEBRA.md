# EOD Algebra

The finite deterministic EOD algebra separates **current knowledge**, **resolution obstruction**, **evidence capability**, **future obligation**, **state transition**, and **certification**.

Let \(\mathbb D=(W,H,E,\Omega,C,\Gamma)\) and \(q:W\to Y\).

## 1. VIEW

\[
\operatorname{VIEW}(\mathbb D,q)
=
\left(V_H,\{q(w):w\in V_H\}\right).
\]

**Type**

\[
\mathrm{DB}\times\mathrm{Query}\to\mathrm{QueryView}.
\]

It exposes current possible worlds and answers but says nothing by itself about future answerability.

## 2. OBSTRUCT

\[
\operatorname{OBSTRUCT}(\mathbb D,q)
=
\{\{u,v\}\subseteq V_H:q(u)\neq q(v)\}.
\]

**Type**

\[
\mathrm{DB}\times\mathrm{Query}\to\mathcal P(\mathrm{Pair}).
\]

The empty obstruction is equivalent to current query resolution.

## 3. SEPARATE

For evidence operation \(e\),

\[
\operatorname{SEPARATE}(\mathbb D,e)
=
\{\{u,v\}\subseteq V_H:\Omega_e(u)\neq\Omega_e(v)\}.
\]

The query-relative form intersects this with \(\operatorname{OBSTRUCT}(\mathbb D,q)\).

**Type**

\[
\mathrm{DB}\times\mathrm{EvidenceOp}\to\mathcal P(\mathrm{Pair}).
\]

## 4. OBLIGATE

\[
\operatorname{OBLIGATE}(\mathbb D,q)
=
\arg\min_{X\subseteq E_\Gamma}
\sum_{e\in X}C(e)
\]

subject to

\[
\operatorname{OBSTRUCT}(\mathbb D,q)
\subseteq
\bigcup_{e\in X}\operatorname{SEPARATE}(\mathbb D,e).
\]

If no such \(X\) exists, OBLIGATE returns no finite sufficient obligation.

**Type**

\[
\mathrm{DB}\times\mathrm{Query}
\to
\mathrm{Obligation}\cup\{\bot\}.
\]

## 5. ACQUIRE

If operation \(e\) produces outcome \(o\),

\[
\operatorname{ACQUIRE}(\mathbb D,e,o)=\mathbb D'
\]

where

\[
V_{H'}=\{w\in V_H:\Omega_e(w)=o\}.
\]

**Type**

\[
\mathrm{DB}\times\mathrm{EvidenceOp}\times\mathrm{Outcome}\to\mathrm{DB}.
\]

This is the principal state-transition operator.

## 6. CERTIFY

\[
\operatorname{CERTIFY}(\mathbb D,q)
\]

returns exactly one of:

\[
\mathrm{AnswerCertificate}(a),
\]

\[
\mathrm{EvidenceObligation}(X,C(X)),
\]

or

\[
\mathrm{ImpossibilityCertificate}(u,v).
\]

**Type**

\[
\mathrm{DB}\times\mathrm{Query}\to\mathrm{Certificate}.
\]

## Algebraic laws

### Law 1 — Resolution law

\[
\operatorname{OBSTRUCT}(\mathbb D,q)=\varnothing
\iff
\operatorname{CERTIFY}(\mathbb D,q)
\text{ is an AnswerCertificate}.
\]

### Law 2 — Acquisition refinement

For a feasible observed outcome,

\[
V_{\operatorname{ACQUIRE}(D,e,o)}
\subseteq
V_D.
\]

### Law 3 — Obstruction contraction

For any acquisition consistent with the current state,

\[
\operatorname{OBSTRUCT}(\operatorname{ACQUIRE}(D,e,o),q)
\subseteq
\operatorname{OBSTRUCT}(D,q).
\]

### Law 4 — Idempotence of repeated identical evidence

If \(D'=\operatorname{ACQUIRE}(D,e,o)\), then

\[
\operatorname{ACQUIRE}(D',e,o)
\]

has the same version space as \(D'\).

### Law 5 — Commutativity of compatible deterministic observations

For deterministic evidence operations \(e,f\) and jointly feasible outcomes \(o_e,o_f\),

\[
V_{\operatorname{ACQUIRE}(\operatorname{ACQUIRE}(D,e,o_e),f,o_f)}
=
V_{\operatorname{ACQUIRE}(\operatorname{ACQUIRE}(D,f,o_f),e,o_e)}.
\]

Thus compatible deterministic acquisitions commute at the level of version-space semantics.

## Why this matters

The algebra makes EOD more than an output convention. It provides operators over a database state whose semantics explicitly include future evidence capability.

The next extension is an adaptive operator in which OBLIGATE returns a branching policy rather than a fixed evidence set.
