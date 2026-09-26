# Matched-risk evidence-stopping experiment

## Question

Can a staged policy stop before the full B4 feature budget while keeping its decisions close to the fixed B4 reference?

## Controls

- Same chronological 60/20/20 split as the first experiment.
- Same model family and stage definitions.
- All policy parameters selected on validation only.
- Test set evaluated once after policy selection.
- Maximum validation disagreement budget with B4: 0.10%.
- Stage cost: B0=0, B1=1, B2=2, B3=3, B4=4.

## Policies

### Always B4

Acquire every feature block. Cost = 4.

### Confidence-only

Stop at the earliest stage satisfying a validation-selected extreme-probability threshold; otherwise continue.

### Maturity-aware proxy

From B2 onward, stop when:

1. the current and previous stage decisions agree; and
2. the change in model probability is below a validation-selected stability threshold.

Otherwise continue to B4.

This is deliberately called a **proxy**. It is not the formal EOD minimum-obligation algorithm and does not provide a logical guarantee of resolution.

## Frozen test result

| Policy | Mean evidence cost | Disagreement vs B4 | Saving vs B4 |
|---|---:|---:|---:|
| Always B4 | 4.000 | 0.000% | 0.0% |
| Confidence-only | 2.316 | 0.051% | 42.1% |
| Maturity-aware proxy | 2.212 | 0.088% | 44.7% |

At the common validation risk budget, the maturity-aware proxy uses about

\[
(2.316-2.212)/2.316 \approx 4.5\%
\]

less evidence than confidence-only on test.

## Interpretation

The result supports a narrow empirical statement:

> Under this controlled progressive-feature proxy and matched validation disagreement constraint, a stability/maturity-aware stopping rule can reduce average evidence acquisition relative to confidence-only stopping.

It does **not** establish that formal EOD is superior to confidence stopping, because:

- B4 is a model-based reference, not ground-truth resolution;
- V1-V28 are anonymized PCA coordinates, not semantic evidence operations;
- the maturity rule is empirical rather than the formal obstruction/obligation engine;
- only one dataset/model family is represented.

## Next required analysis

1. compare policies directly against ground-truth fraud labels, not only B4;
2. sweep several risk budgets and report cost-risk curves;
3. bootstrap uncertainty intervals;
4. repeat with at least one additional classifier family;
5. add a semantically staged dataset before making operational claims.
