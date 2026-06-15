# PB_TX_SET_PLAN_GRP

> The PB_TX_SET_PLAN_GRP table lists employer groups associated with a premium billing payment transaction set.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | Line counter for the plan group on the transaction set. |
| 3 | `PLAN_GRP_ID` | VARCHAR | FK→ | The unique ID of the plan group associated with the transaction set. |
| 4 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |

