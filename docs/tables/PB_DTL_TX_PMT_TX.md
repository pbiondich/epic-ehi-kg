# PB_DTL_TX_PMT_TX

> The PB_DTL_TX_PMT_TX table contains payments received for the detailed premium billing account transaction.

**Primary key:** `PB_TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TX_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing detailed transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter of the payment on the detailed transaction. |
| 3 | `PB_ACT_TX_ID` | VARCHAR | shared | The unique ID of the premium billing account transaction on which payment was received for this detailed transaction. |
| 4 | `PMT_AMT` | NUMERIC |  | Amount of the payment received for the detailed transaction. |
| 5 | `PMT_REMAIN` | NUMERIC |  | Remaining amount of the detailed transaction after payment. |
| 6 | `PAYMENT_REV_LINE` | INTEGER |  | Payment reversed line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_TX_ID` | [PB_DTL_TX](PB_DTL_TX.md) | sole_pk | high |

