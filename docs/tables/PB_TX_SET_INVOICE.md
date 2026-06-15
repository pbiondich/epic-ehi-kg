# PB_TX_SET_INVOICE

> The PB_TX_SET_INVOICE table lists invoices associated with a premium billing payment transaction set.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | The line count for the invoice on the transaction set. |
| 3 | `PB_INVC_ID` | VARCHAR | FK→ | The unique ID of the invoice associated with the transaction set. |
| 4 | `INVOICE_PORTION_C_NAME` | VARCHAR |  | The invoice portion covered by this transaction set. |
| 5 | `INVOICE_BILL_DATE` | DATETIME |  | This field stores the date of the current or future invoice associated with this line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

