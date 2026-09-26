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
- [ ] At least one realistic public-data workload.
- [ ] Strong implementation baselines appropriate to that workload.
- [ ] Ablation study.
- [ ] Expanded systematic prior-art audit of access-limited query answering, acquisitional DBs, epistemic planning/sensing, active information acquisition, and provenance.
- [ ] Stronger formal relationship theorem: embedding, equivalence, or separation against the closest established formalism.
- [ ] Independent reproducibility run from a clean release.
- [ ] Figures/tables generated from frozen artifacts.

## Current assessment

The project has crossed from a conceptual proposal into a theorem-backed executable research prototype.

It is **not yet appropriate to label it Q1-ready** because the application evidence, baseline evaluation, and closest-formalism comparison are not complete.

The manuscript should be frozen only after the unchecked items above are resolved.
