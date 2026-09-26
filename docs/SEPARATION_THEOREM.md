# Capability-Separation Theorem

## Purpose

This note isolates the first formal separation result for Evidence-Obligation Database Theory (EOD).

The result is deliberately precise. It does **not** claim that a relational or incomplete database cannot encode evidence-operation metadata. Instead, it shows that **current possible-world/query-answer semantics alone is insufficient to determine future answerability**.

## Definitions

For an EOD database \(\mathbb D\), evidence history \(H\), and query \(q\), define its **current query view**

\[
\operatorname{CQV}(\mathbb D,q)
=
\left(V_H,\; q|_{V_H}\right).
\]

Two databases are **current-query equivalent** for \(q\), written

\[
\mathbb D_1\equiv_q^{\mathrm{cur}}\mathbb D_2,
\]

when they have the same current version space and the same query value on every remaining world.

Define the **resolution status**

\[
\operatorname{RS}(\mathbb D,q)
\in
\{\mathrm{RESOLVED},\mathrm{ACQUIRABLY\_RESOLVABLE},\mathrm{UNRESOLVABLE}\}.
\]

## Theorem — Capability Separation

There exist finite EOD databases \(\mathbb D_+\) and \(\mathbb D_-\) and a query \(q\) such that

\[
\mathbb D_+\equiv_q^{\mathrm{cur}}\mathbb D_-,
\]

but

\[
\operatorname{RS}(\mathbb D_+,q)
\neq
\operatorname{RS}(\mathbb D_-,q).
\]

Therefore resolution status is **not a function of the current query view alone**.

### Construction

Let

\[
W=\{u,v\},
\qquad
H=\varnothing,
\]

and let

\[
q(u)=0,\qquad q(v)=1.
\]

Both databases therefore have

\[
V_H=\{u,v\}
\]

and the same current possible answers

\[
\{0,1\}.
\]

For \(\mathbb D_+\), include an admissible evidence operation \(e_+\) with

\[
\Omega_{e_+}(u)=0,
\qquad
\Omega_{e_+}(v)=1.
\]

Thus \(e_+\) separates the only query-disagreeing pair \(\{u,v\}\). Hence

\[
\operatorname{RS}(\mathbb D_+,q)
=
\mathrm{ACQUIRABLY\_RESOLVABLE}.
\]

For \(\mathbb D_-\), let every admissible evidence operation \(e\) satisfy

\[
\Omega_e(u)=\Omega_e(v).
\]

No admissible operation separates \(\{u,v\}\). Hence

\[
\operatorname{RS}(\mathbb D_-,q)
=
\mathrm{UNRESOLVABLE}.
\]

Yet their current query views are identical. Therefore current query information does not determine future answerability. ∎

## Corollary — Evidence capability carries logical information

Any semantics intended to determine EOD resolution status must contain information beyond

\[
(V_H,q|_{V_H}).
\]

In particular, it must encode enough of the admissible evidence capability

\[
(E,\Omega,\Gamma)
\]

to determine whether query-disagreeing worlds can be separated.

## Corollary — Same uncertainty, different futures

Two databases can expose exactly the same current uncertainty while differing in whether that uncertainty can ever be resolved.

This is the central distinction EOD makes explicit:

\[
\boxed{\text{same current knowledge}\;\not\Rightarrow\;\text{same future answerability}}
\]

## What this theorem does and does not prove

### It proves

- future answerability is not determined by the current possible answers alone;
- evidence capability contains semantically relevant information;
- an EOD state must distinguish systems that a current-query view identifies.

### It does not prove

- that EOD cannot be implemented on a relational DBMS;
- that no prior formalism can encode evidence capability;
- that EOD is strictly more expressive than every incomplete or acquisitional database language;
- historical novelty of the complete EOD model.

Those stronger claims require formal translations and literature-backed separation results.

## Executable witness

Run:

```bash
python experiments/capability_separation.py
```

The program constructs \(\mathbb D_+\) and \(\mathbb D_-\), verifies identical current query views, and shows their distinct EOD resolution statuses.
