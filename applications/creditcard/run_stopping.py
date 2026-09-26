"""Matched-risk early-stopping experiment.

Compares confidence-only and maturity-aware proxy stopping against always-B4.
All stopping parameters are selected on validation data. B4 is the fixed
reference decision. This is an empirical proxy experiment, not a formal EOD
guarantee.
"""
# See docs/CREDITCARD_STOPPING_RESULTS.md for the frozen protocol/results.
# Implementation intentionally follows run_progressive.py: chronological split,
# standardized class-balanced logistic regression, validation-selected stage
# thresholds. Candidate policies are grid-searched on validation under a fixed
# maximum disagreement budget with B4, then evaluated once on test.
#
# confidence-only:
#   stop at earliest stage s where p_s <= low or p_s >= high.
#
# maturity-aware:
#   from B2 onward, stop when current and previous stage decisions agree and
#   abs(p_s - p_{s-1}) <= delta; otherwise continue to B4.
#
# Publication use should regenerate the CSV artifacts from the local dataset.
