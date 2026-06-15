# HSP_BKT_INV_NUM

> This table contains hospital liability bucket invoice numbers information from the Hospital Liability Buckets (HLB) master file.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple invoices can be associated with a liability bucket, each invoice will have a unique line number. |
| 3 | `INVOICE_NUMBER` | VARCHAR |  | An invoice number associated with the liability bucket. |
| 4 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

