# HSP_BKT_PAYMENT

> This table contains liability bucket payment transaction information.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record with associated payment transaction information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAYMENT_ID` | NUMERIC |  | This column stores the unique identifier for the payment transaction in this liability bucket. |
| 4 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account ID that the liability bucket belongs to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

