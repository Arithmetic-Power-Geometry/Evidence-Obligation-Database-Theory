# Credit-card progressive evidence: first frozen results

## Protocol

- 284,807 transactions, chronological order by `Time`.
- 60/20/20 train/validation/test split.
- Same classifier family at every stage: standardized class-balanced logistic regression.
- Classification threshold chosen independently at each stage by maximum validation F1.
- Test set untouched during fitting and threshold selection.
- B0 = Time+Amount; each later budget adds seven anonymized PCA coordinates.

## Test results

| Stage | Features | PR-AUC | ROC-AUC | Precision | Recall | F1 | TP | FP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B0 | 2 | 0.0018 | 0.5818 | 0.0000 | 0.0000 | 0.0000 | 0 | 72 |
| B1 | 9 | 0.3133 | 0.9677 | 0.3936 | 0.4933 | 0.4379 | 37 | 57 |
| B2 | 16 | 0.7124 | 0.9837 | 0.5729 | 0.7333 | 0.6433 | 55 | 41 |
| B3 | 23 | 0.7438 | 0.9828 | 0.9800 | 0.6533 | 0.7840 | 49 | 1 |
| B4 | 30 | 0.7439 | 0.9820 | 0.9259 | 0.6667 | 0.7752 | 50 | 4 |

## High-confidence reversal diagnostic

Define raw high confidence as model probability <=0.01 or >=0.99. Compare the stage decision with the final B4 decision.

| Stage | high-confidence cases | later reversed | reversal rate |
|---|---:|---:|---:|
| B1 | 8,409 | 59 | 0.7016% |
| B2 | 9,392 | 42 | 0.4472% |
| B3 | 12,045 | 6 | 0.0498% |

## Interpretation

Additional information is highly valuable through B2/B3; B4 adds almost no PR-AUC over B3 in this particular protocol. High raw confidence is not identical to information maturity: some highly confident early decisions reverse after later features are supplied.

This is a **diagnostic**, not yet evidence that EOD outperforms a stopping baseline. The next analysis must compare stopping policies at matched error/risk and report acquisition cost.

## Limitation

V1-V28 are anonymized PCA components. Feature budgets are a controlled proxy for staged evidence, not semantically distinct real-world investigations.
