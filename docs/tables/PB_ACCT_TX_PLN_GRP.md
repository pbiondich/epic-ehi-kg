# PB_ACCT_TX_PLN_GRP

> The PB_ACCT_TX_PLN_GRP table includes a list of employer groups associated with a premium billing account transaction.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium account transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter of the employer group associated with the premium account transaction. |
| 3 | `PLAN_GRP_ID` | VARCHAR | FK→ | The unique ID of the employer group associated with the transaction. |
| 4 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |

