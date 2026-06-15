# INV_COND_CODE

> This table holds the condition codes sent out on professional billing claims.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | Returns the line count value for multiple or related response items. |
| 3 | `CONDITION_CODE_C_NAME` | VARCHAR | org | Condition Code to print on claims. |
| 4 | `INV_NUM_COND_PTR100` | INTEGER |  | Stores an index into the invoice line for the invoice number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

