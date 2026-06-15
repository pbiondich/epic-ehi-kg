# PB_TX_SET_CREDIT

> The PB_TX_SET_CREDIT table specifies the premium billing detailed transactions credited for a payment transaction set.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | Line counter for the credit on the transaction set. |
| 3 | `CR_PB_TX_ID` | VARCHAR |  | The unique ID of the detailed premium billing transaction associated with the credit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

