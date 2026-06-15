# INVOICE_HX

> The INVOICE_HX table contains historical information for invoice records.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique ID of the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number of the history date item. |
| 3 | `ACTION_USER_COMMENT` | VARCHAR |  | Comment for an activity performed on an invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

