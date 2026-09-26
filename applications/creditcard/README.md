# Credit Card Fraud — Progressive Evidence-Budget Workload

Dataset: ULB/Kaggle credit-card fraud benchmark (`creditcard.csv`).

Validated local copy used during development:

- 284,807 rows;
- 31 columns;
- target: `Class`;
- 492 fraud transactions (0.1727%);
- no missing values;
- predictors: `Time`, `Amount`, and anonymized PCA components `V1`–`V28`.

## Scientific limitation

The V-features are anonymized PCA components. They do not represent separately identifiable tests, devices, identity checks, or investigations.

Therefore this workload is used only as a **controlled progressive feature-budget proxy** for evidence acquisition. It must not be described as a real staged investigation process.

## Chronological protocol

Sort by `Time` and split without shuffling:

- first 60%: training;
- next 20%: validation;
- final 20%: test.

For the validated local copy this yields:

| split | rows | fraud |
|---|---:|---:|
| train | 170,884 | 360 |
| validation | 56,961 | 57 |
| test | 56,962 | 75 |

## Evidence-budget stages

To avoid inventing semantic meanings for PCA coordinates, stages are defined purely by feature budget:

- B0: `Time, Amount`;
- B1: B0 + `V1..V7`;
- B2: B1 + `V8..V14`;
- B3: B2 + `V15..V21`;
- B4: B3 + `V22..V28`.

These are computational acquisition stages only. The ordering is fixed before outcome evaluation and is not claimed to reflect real-world acquisition cost.

## Publication role

This dataset can support:

- progressive-information experiments;
- cost/sensitivity analysis;
- confidence-vs-additional-evidence comparisons;
- chronological robustness checks.

It cannot by itself validate the real operational meaning of evidence obligations. A semantically staged dataset remains desirable for the final paper.
