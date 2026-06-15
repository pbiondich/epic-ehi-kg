# HSP_PRE_AR_TX_FLAGS

> This table contains Hospital Billing temporary transaction flag information. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK FK→ | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_FLAGS_C_NAME` | VARCHAR |  | This item is used to store special flags that describe the transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HTT_ID` | [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | sole_pk | high |

