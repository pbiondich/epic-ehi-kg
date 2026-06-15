# V_EHI_PTS_PB_TX_SET_INVOICE

> This view filters out premium billing payment data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | The line count for the invoice on the transaction set. |
| 3 | `INV_TX_SET_AMT` | NUMERIC |  | The invoice amount associated with the transaction set. |
| 4 | `INVOICE_PAYMENT_AMOUNT` | NUMERIC |  | This field stores the payment amount for this invoice. |
| 5 | `INVOICE_ADJ_AMOUNT` | NUMERIC |  | This field stores the adjustment amount for this invoice. |
| 6 | `PB_INVC_ID` | VARCHAR | FK→ | The unique ID of the invoice associated with the transaction set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

