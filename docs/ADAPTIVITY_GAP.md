# Strict Adaptivity Gap in EOD

## Definition

Let \(C^*_{\mathrm{fix}}(D,q)\) be the minimum cost of a fixed non-adaptive evidence set that guarantees resolution, and let \(C^*_{\mathrm{ad}}(D,q)\) be the minimum worst-case cost of an adaptive evidence policy.

Define the adaptivity gap

\[
G(D,q)=\frac{C^*_{\mathrm{fix}}(D,q)}{C^*_{\mathrm{ad}}(D,q)}.
\]

## Proposition — Strict adaptivity advantage

There exists a finite deterministic EOD instance for which

\[
G(D,q)>1.
\]

### Witness

Let four worlds have four distinct query answers:

\[
q(w_i)=i,\qquad i=1,2,3,4.
\]

Let three unit-cost binary evidence operations have outcomes

| world | A | B | C |
|---|---:|---:|---:|
| w1 | 0 | 0 | 0 |
| w2 | 0 | 0 | 1 |
| w3 | 0 | 1 | 0 |
| w4 | 1 | 0 | 1 |

### Fixed obligation

No pair among \(\{A,B,C\}\) distinguishes all four worlds:

- \(A,B\) leave \(w_1,w_2\) identical;
- \(A,C\) leave \(w_1,w_3\) identical;
- \(B,C\) leave \(w_2,w_4\) identical.

Therefore every fixed resolving obligation requires all three operations:

\[
C^*_{\mathrm{fix}}=3.
\]

### Adaptive policy

Acquire \(C\) first.

If \(C=0\), the remaining worlds are \(\{w_1,w_3\}\), which \(B\) separates.

If \(C=1\), the remaining worlds are \(\{w_2,w_4\}\), which \(A\) separates.

Thus every branch resolves after exactly two unit-cost operations:

\[
C^*_{\mathrm{ad}}=2.
\]

Hence

\[
\boxed{G(D,q)=\frac32}.
\]

This is a strict worst-case advantage, not merely an expected-cost or early-stopping effect.

## Interpretation

A fixed obligation must buy evidence sufficient for mutually exclusive future branches simultaneously. An adaptive policy waits for the first outcome and buys only the evidence relevant to the branch actually entered.

This establishes that adaptive EOD semantics can change the minimum guaranteed evidence cost.
