# Semantic-stage replication: UCI Default of Credit Card Clients

## Why this dataset

The first real-data benchmark used anonymized PCA coordinates and therefore could only represent evidence acquisition as a controlled feature-budget proxy. This second dataset supplies interpretable blocks: profile/capacity, repayment status, bill history, and payment history.

## Protocol

- 30,000 observations; 6,636 defaults (22.12%); no missing values.
- No event-time variable is available for chronological evaluation, so a deterministic stratified 60/20/20 split is used (seed 2026).
- Same classifier family for the first pass: standardized class-balanced logistic regression.
- Stage thresholds selected by validation F1 only.
- Test set used only for final evaluation.

## Results

| Stage | Meaning | PR-AUC | ROC-AUC | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|
| P0 | profile/capacity | 0.3071 | 0.6316 | 0.2895 | 0.6511 | 0.4008 |
| P1 | + repayment status | 0.5197 | 0.7381 | 0.5575 | 0.5222 | 0.5393 |
| P2 | + bill history | 0.5150 | 0.7355 | 0.5371 | 0.5298 | 0.5334 |
| P3 | + payment history | 0.5185 | 0.7385 | 0.4847 | 0.5735 | 0.5254 |

Repayment status supplies the dominant information gain. Later blocks add little ranking performance under this model.

## Decision evolution

Relative to the full P3 decision:

- P0 differs on 36.10% of test clients;
- P1 differs on 6.68%;
- P2 differs on 5.35%.

Mean absolute probability difference from P3 contracts from 0.1224 at P0 to 0.0370 at P1 and 0.0281 at P2.

## Cross-dataset conclusion

The exact extreme-confidence reversal diagnostic from the PCA benchmark does not replicate: this logistic model yields almost no probabilities outside [0.1,0.9]. Therefore an arbitrary confidence cutoff should not be promoted as a universal result.

What does replicate at a broader level is that decisions and scores evolve materially as additional evidence becomes available, and that later evidence can have diminishing predictive value even while some individual decisions continue to change.

This supports studying query/decision-relative evidence sufficiency rather than equating a fixed amount of acquired data or an arbitrary confidence threshold with maturity.

## Claim boundary

This remains an empirical analogue of EOD, not a logical resolution proof. Acquisition costs are not observed real-world costs, and the train/test split is stratified rather than temporal.
