# HSP_BKT_DSCNT_ADJ

> This table consists of only one multiple-response item, Self Pay Discount Adjustment IDs (I HLB 940). The item is a list of active self-pay discount adjustment transaction (HTR) record IDs on a self-pay liability bucket.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SP_DSCNT_ADJ_TX_ID` | NUMERIC |  | This is the list of active self pay discount adjustments posted to the self pay bucket. |
| 4 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

