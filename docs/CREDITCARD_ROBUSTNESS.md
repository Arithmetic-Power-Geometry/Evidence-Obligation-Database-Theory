# Robustness: cost-quality frontier

This experiment extends the first stopping result with a risk sweep, ground-truth fraud metrics, a second classifier family, paired bootstrap uncertainty, and an ablation.

## Protocol

The chronological 60/20/20 split and B0-B4 feature budgets are unchanged. Policy parameters are selected on validation only. Two classifier families are used:

- class-balanced logistic regression (LR);
- class-weighted histogram gradient boosting (HGB).

The stopping reference remains the B4 decision. Ground-truth precision, recall and F1 are reported separately, preventing low disagreement with B4 from being mistaken for correctness.

## Main finding

The result is a **cost-quality frontier**, not a universal dominance result.

At the 0.10% validation disagreement budget:

| Family | Policy | Mean cost | Test disagreement vs B4 | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|
| LR | confidence | 3.848 | 0.098% | 0.510 | 0.707 | 0.592 |
| LR | maturity | 2.095 | 0.021% | 0.788 | 0.693 | 0.738 |
| HGB | confidence | 1.043 | 0.077% | 0.634 | 0.600 | 0.616 |
| HGB | maturity | 2.034 | 0.011% | 0.881 | 0.693 | 0.776 |

Full-B4 F1 is 0.775 for LR and 0.773 for HGB.

Thus the maturity proxy is simultaneously cheaper and higher-F1 than the strict-risk LR confidence rule in this protocol. For HGB, confidence stopping is cheaper, while maturity stopping retains substantially higher F1. This classifier dependence is evidence against claiming universal cost dominance.

## Bootstrap uncertainty

500 paired transaction-level bootstrap resamples, fixed trained models/policies:

| Family | Policy | Mean cost 95% interval | F1 | F1 95% interval |
|---|---|---|---:|---|
| LR | confidence | [3.843, 3.853] | 0.592 | [0.496, 0.672] |
| LR | maturity | [2.093, 2.097] | 0.738 | [0.649, 0.818] |
| HGB | confidence | [1.041, 1.046] | 0.616 | [0.515, 0.706] |
| HGB | maturity | [2.033, 2.036] | 0.776 | [0.689, 0.848] |

These are empirical bootstrap intervals, not formal guarantees.

## Ablation: remove decision-agreement condition

At the same 0.10% validation constraint, a stability-only rule (probability-change condition without requiring consecutive decisions to agree) gives:

- LR: cost 2.093, disagreement 0.075%, F1 0.635;
- HGB: cost 2.034, disagreement 0.011%, F1 0.776.

For LR, the agreement condition costs almost nothing but raises F1 from 0.635 to 0.738. For HGB it is effectively neutral. This supports retaining agreement as part of the maturity proxy while also showing that its benefit is model-dependent.

## Claim boundary

These results support:

> In this controlled staged-feature benchmark, confidence and evidence-maturity criteria induce materially different cost-quality trade-offs; under strict reference-risk constraints, maturity-aware stopping can preserve substantially more ground-truth decision quality.

They do not establish universal EOD superiority or logical resolution on the fraud dataset. The formal EOD guarantees remain established in the finite deterministic theory/benchmark layer; this real dataset is an empirical proxy layer.

## Remaining high-value work

A semantically staged dataset is now more valuable than additional tuning on this anonymized PCA benchmark. It would test whether the same distinction survives when evidence operations have real acquisition meanings and costs.
