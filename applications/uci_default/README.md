# UCI Default of Credit Card Clients — semantic evidence workload

Validated source file: `default of credit card clients.xls`.

- 30,000 clients
- 25 columns including target
- 6,636 defaults (22.12%)
- zero missing values

Unlike the anonymized PCA fraud benchmark, this dataset permits interpretable progressive evidence blocks.

## Evidence stages

- P0 — profile/capacity: LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE
- P1 — repayment status: P0 + PAY_0, PAY_2..PAY_6
- P2 — bill history: P1 + BILL_AMT1..BILL_AMT6
- P3 — payment history: P2 + PAY_AMT1..PAY_AMT6

These blocks have semantic meaning, but their unit acquisition costs are experimental abstractions rather than measured institutional costs.

The dataset has no event-time variable suitable for a chronological split. The frozen protocol therefore uses a deterministic stratified 60/20/20 train/validation/test split (seed 2026). This difference from the first benchmark must be reported.
