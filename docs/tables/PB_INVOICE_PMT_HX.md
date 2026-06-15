# PB_INVOICE_PMT_HX

> Stores the list of account transactions and amounts for Premium Billing invoices.

**Primary key:** `PB_INVC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing invoice. |
| 2 | `LINE` | INTEGER | PK | Line counter for the payment on the invoice. |
| 3 | `POST_DATE` | DATETIME |  | Date payment was posted on the invoice. |
| 4 | `PB_ACT_TX_ID` | VARCHAR | shared | The unique ID of premium billing account transaction associated with the payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

