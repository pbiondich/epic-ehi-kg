# V_EHI_PTS_PB_TX_SET_BEF_INV

> This view filters out premium billing payment data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `TRANSACTION_SET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_SET_ID` | VARCHAR | PK | The unique identifier for the set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BEF_INV_AMOUNT` | NUMERIC |  | The invoice amount associated with this transaction set prior being commited. |
| 4 | `BEF_INVOICE_ID` | VARCHAR |  | Invoices associated with this transaction set prior being commited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

