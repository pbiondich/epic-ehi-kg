# PB_INVOICE_PREV

> Stores a list of previous payment transactions on the premium billing account for the premium billing invoice.

**Primary key:** `PB_INVC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing invoice. |
| 2 | `LINE` | INTEGER | PK | Line counter for the previous payment ID on the invoice. |
| 3 | `PREV_PB_ACT_TX_ID` | VARCHAR |  | The unique ID of the premium billing account transaction associated with payment received between the last invoice and this invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

