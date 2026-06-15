# RECONCILE_CLSD_TX

> This table contains information on closed A/R Transactions (ETR) charges for claim reconciliation records.

**Primary key:** `CLAIM_REC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_REC_ID` | VARCHAR | PK FK→ | The unique ID of the claim reconciliation record. |
| 2 | `LINE` | INTEGER | PK | The line count of the closed transaction (ETR) record. |
| 3 | `REC_CLOSED_TX_ID` | NUMERIC |  | The closed transaction (ETR) record's ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_REC_ID` | [RECONCILE_CLM](RECONCILE_CLM.md) | sole_pk | high |

