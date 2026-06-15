# TX_INVOICES

> This table maps a link from the CLARITY_TDL table via TX_ID to the Invoice tables via INVOICE_ID.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the invoice associated with this transaction. Multiple invoices can be associated with this transaction. |
| 3 | `ETR_BC_TYPE_C_NAME` | VARCHAR |  | Indicates whether the transaction is on a bill or a claim. |
| 4 | `BC_ACCEPT_DATE` | DATETIME |  | The date the bill or claim was accepted. |
| 5 | `INVOICE_NUM` | VARCHAR |  | The invoice number for the transaction. |
| 6 | `INVOICE_ID` | NUMERIC | FK→ | The unique internal identifier of the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

