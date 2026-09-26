# Manuscript-freeze readiness audit

This is an internal research-quality checklist, not a journal-ranking or acceptance claim.

## Formal core completed

- [x] Explicit finite EOD semantics and resolution trichotomy.
- [x] Capability-Separation Theorem and executable witness.
- [x] Typed EOD algebra.
- [x] Exact fixed and adaptive planners.
- [x] Strict worst-case adaptivity-gap witness.
- [x] Greedy obstruction-cover planner with inherited weighted-set-cover guarantee.
- [x] EOD-MEO NP-completeness via cost-preserving Weighted Set Cover reduction.
- [x] Conditional-sensing representation theorem.
- [x] Qualitative and costed access-method translations.
- [x] Coarse-composition impossibility theorem.
- [x] Obligation-hypergraph representation theorem.
- [x] Signed annotation with exact Boolean composition.

## Reproducibility and empirical layer completed

- [x] Automated regression tests and CI workflow.
- [x] Deterministic synthetic benchmark harness.
- [x] Exhaustive small-instance audit harness.
- [x] ULB/Kaggle credit-card progressive feature-budget benchmark.
- [x] Cost-risk stopping comparison.
- [x] Two classifier families.
- [x] Ground-truth fraud metrics.
- [x] Bootstrap uncertainty analysis.
- [x] Stopping-rule ablation.
- [x] Second public dataset with semantically interpretable evidence blocks: UCI Default of Credit Card Clients.
- [x] Cross-dataset replication analysis with explicit negative/non-replicating findings retained.

## Claim discipline

The project does **not** claim novelty for possible worlds, active sensing, adaptive information acquisition, minimum-cost test selection, weighted set cover, or access-method planning. The finite adaptive planner has an explicit cost-preserving representation as a sensing problem.

The defensible contribution is narrower: a database-native resolution semantics and algebra in which evidence capability is part of state and unresolved queries can denote typed obstruction, obligation, policy, and impossibility objects, together with formal results about their complexity and composition.

The real-data experiments are empirical analogues of evidence acquisition. They do not constitute logical EOD resolution guarantees.

## Release-critical items

- [x] Full Apache License 2.0 text.
- [x] Copyright/NOTICE.
- [x] CITATION.cff prepared for 1.0.0.
- [x] Package metadata prepared for 1.0.0.
- [x] Obsolete composition scaffold retired in favor of exact witness.
- [x] Hypergraph/composition APIs exported.
- [ ] Inspect a clean CI run against the final v1.0 tree.
- [ ] Generate final manuscript figures/tables directly from frozen artifacts.
- [ ] Perform final literature/prior-art audit immediately before manuscript submission.

## Current assessment

The repository now contains a manuscript-capable technical package: formal semantics, theorems, algorithms, reproducibility infrastructure, controlled real-data experiments, a semantically staged replication dataset, uncertainty analysis, and explicit limitations.

The remaining work is release verification and manuscript production rather than adding new theory, datasets, or model tuning. A journal's quartile does not imply acceptance, so this checklist should not be interpreted as an acceptance prediction.
