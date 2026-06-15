# INVOICE_APC_TX

> The INVOICE_TX table contains information about the transactions that appear on the invoice.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique ID of the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number of the payment classification line. Multiple pieces of information can be associated with this record. |
| 3 | `APC_LINE` | INTEGER |  | The line number of the transaction record in the payment classification items. |
| 4 | `ETR_LINE` | INTEGER |  | The line number in the transaction record for the bill history group to which this invoice applies. |
| 5 | `TX_ID` | NUMERIC | shared | The ID of the transaction record that appears on the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

