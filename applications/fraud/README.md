# Staged Fraud-Evidence Workload

This application is designed for the IEEE-CIS Fraud Detection data.

The public competition describes two linked sources:

- transaction features in `train_transaction.csv`;
- optional identity features in `train_identity.csv`, joined by `TransactionID`.

Not every transaction has corresponding identity information. That makes the dataset a useful staged-information workload, but this repository does **not** reinterpret the competition as an EOD benchmark without an explicit protocol.

## EOD framing

The target decision is binary fraud/non-fraud. Evidence is partitioned into stages:

1. **core transaction evidence** — amount, product/card/address/time fields;
2. **context evidence** — transaction-side engineered/count/match variables;
3. **identity evidence** — device/network/identity variables where available.

A stage is treated as an evidence capability only when the benchmark protocol explicitly defines:

- what information is hidden before acquisition;
- acquisition cost;
- availability/admissibility;
- the rule mapping acquired evidence to a version-space refinement.

## Baselines

The planned comparison reports separately:

- current-information prediction/confidence;
- fixed acquisition of all available stages;
- EOD fixed obligation;
- EOD adaptive policy;
- oracle/full-information reference.

The goal is not to claim that EOD is a better fraud classifier. The research question is whether EOD can reduce evidence acquisition while preserving a specified decision-resolution criterion.

## Data access

The IEEE-CIS files are governed by Kaggle competition rules and are not redistributed here.

Place accepted local copies under `data/ieee-cis/` and run the adapter. Raw data remains ignored by Git.
