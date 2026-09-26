# Greedy EOD Obligation Algorithm

For explicit finite non-adaptive EOD, the obstruction universe is

\[
U=\mathcal O_q(H).
\]

Each admissible evidence operation \(e\) covers

\[
S_e\cap U.
\]

Therefore minimum fixed evidence obligation is a weighted set-cover instance.

The scalable baseline implemented here repeatedly selects the operation maximizing

\[
\frac{|S_e\cap U_{\mathrm{uncovered}}|}{C(e)}.
\]

For positive costs, the classical weighted set-cover analysis gives the standard logarithmic approximation guarantee relative to the optimum over this explicit obstruction universe:

\[
C_{\mathrm{greedy}}
\le
H_{|U|}\,C^*,
\]

where \(H_n\) is the \(n\)-th harmonic number.

The guarantee is inherited from weighted set cover; it is not claimed as a new approximation theorem. The EOD contribution is the reduction of query resolution obligations to this obstruction-cover representation and its use as an executable resolution planner.
