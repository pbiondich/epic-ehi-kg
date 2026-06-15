# PB_DTL_TX_INVC_NUM

> The PB_DTL_TX_INVC_NUM table contains the list of invoices for the detailed premium billing account transaction.

**Primary key:** `PB_TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TX_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing detailed transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter of the invoice on the detailed transaction. |
| 3 | `PB_INVC_ID` | VARCHAR | FK→ | The unique ID of the invoice on the detailed transaction. |
| 4 | `INV_AMT` | NUMERIC |  | Amount of the detailed transaction that appeared on the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |
| `PB_TX_ID` | [PB_DTL_TX](PB_DTL_TX.md) | sole_pk | high |

