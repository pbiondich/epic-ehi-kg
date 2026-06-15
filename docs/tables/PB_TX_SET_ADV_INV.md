# PB_TX_SET_ADV_INV

> The PB_TX_SET_ADV_INV table contains the advices for invoice of this PB transaction set.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | Line counter for the advice for invoice on the transaction set. |
| 3 | `ADVFOR_PB_INVC_ID` | VARCHAR |  | The unique ID of the adviced invoice on the transaction set. Used when defining custom transaction set advice from a batch utility record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

