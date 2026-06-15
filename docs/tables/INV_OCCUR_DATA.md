# INV_OCCUR_DATA

> This table holds the occurrence codes sent out on professional billing claims.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | Returns the line count value for multiple or related response items. |
| 3 | `OCCURRENCE_CODE_C_NAME` | VARCHAR | org | The occurrence code category. |
| 4 | `OCCURRENCE_DT` | DATETIME |  | The occurrence code date. |
| 5 | `INV_NUM_OCC_PTR100` | INTEGER |  | The index of invoice lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

