# HSP_BKT_SPLIT_CLMS

> This table contains information about split claims associated with liability buckets.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPLIT_INV_NO` | VARCHAR |  | The invoice number for the split claim associated with this bucket. |
| 4 | `SPLIT_FORM` | VARCHAR |  | The form used for the split claim associated with this bucket. |
| 5 | `SPLIT_CHG_TOT` | NUMERIC |  | The charge total for the split claim associated with this bucket. |
| 6 | `SPLIT_CLP_ID` | NUMERIC |  | This column stores the unique identifier for the claim print for the claims split that is associated with this bucket. |
| 7 | `SPLIT_ORIG_FORM` | VARCHAR |  | The original form used for the claim associated with this bucket. |
| 8 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

