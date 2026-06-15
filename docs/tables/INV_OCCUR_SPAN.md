# INV_OCCUR_SPAN

> This table holds the occurrence span codes sent out on professional billing institutional claims.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | Returns the line count value for multiple or related response items. |
| 3 | `OCCURRENCE_SPAN_C_NAME` | VARCHAR | org | The Occurrence Span Code. |
| 4 | `OCCUR_SPAN_FROM_DT` | DATETIME |  | The Occurrence Span Code From Date. |
| 5 | `OCCUR_SPAN_TO_DT` | DATETIME |  | The Occurrence Span Code To Date. |
| 6 | `INV_NUM_SPAN_PTR100` | INTEGER |  | The index of invoice lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

