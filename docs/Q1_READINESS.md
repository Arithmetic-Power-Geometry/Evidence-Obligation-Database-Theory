# Q1-readiness audit

This is an internal research-quality checklist, not a journal-ranking claim.

## Completed

- [x] Explicit finite semantics.
- [x] Resolution trichotomy.
- [x] Capability-separation theorem.
- [x] Executable theorem witness.
- [x] Typed EOD algebra.
- [x] Exact fixed obligation engine.
- [x] Exact adaptive policy engine.
- [x] Strict worst-case adaptivity-gap witness.
- [x] Greedy scalable planner.
- [x] Explicit complexity/cover formulation.
- [x] Deterministic synthetic benchmark generator.
- [x] Automated regression tests.
- [x] Continuous-integration reproducibility workflow.
- [x] Machine-readable benchmark output.

## Still required before manuscript freeze

- [ ] CI benchmark results inspected and frozen into a tagged release.
- [ ] Larger scaling study with confidence intervals across instance families.
- [~] Realistic public-data workload scaffolded on IEEE-CIS; execution/results still required.
- [ ] Strong implementation baselines appropriate to that workload.
- [ ] Ablation study.
- [~] Closest-neighbor matrix added; access-method answerability and epistemic planning identified as highest-risk formal collisions; deeper proof-level comparison still required.
- [x] Exact finite representation theorem against conditional sensing: deterministic adaptive EOD policies correspond cost-preservingly to sensing policies. This narrows the novelty claim; access-method translation remains open.
- [ ] Independent reproducibility run from a clean release.
- [ ] Figures/tables generated from frozen artifacts.

## Current assessment

The project has crossed from a conceptual proposal into a theorem-backed executable research prototype, and its adaptive finite fragment now has an explicit representation relationship to established sensing/planning machinery.

It is **not yet appropriate to label it Q1-ready** because the application evidence, baseline evaluation, and closest-formalism comparison are not complete.

The manuscript should be frozen only after the unchecked items above are resolved.
