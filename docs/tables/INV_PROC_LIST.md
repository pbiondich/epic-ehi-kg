# INV_PROC_LIST

> This table holds a list of procedures associated with the invoice.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The internal ID of the invoice number. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_CODES_UB` | VARCHAR |  | The procedure code. This item is only set on UB claims. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `INV_EXT_ID` | VARCHAR |  | The unique external ID of the invoice number. |
| 6 | `INV_NUM_100_GRP_LN` | INTEGER |  | Claim line number that the diagnosis entry applies to. This is the line number that links the INV_PROC_LIST table with the LINE column in the INV_BASIC_INFO table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

