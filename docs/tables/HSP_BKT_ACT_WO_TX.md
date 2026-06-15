# HSP_BKT_ACT_WO_TX

> This table contains the unique IDs of contractual allowance write off transactions that are associated with liability buckets. This list doesn't include expected not-allowed auto write-offs that are posted due to expected reimbursement calculations prior to payment.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACT_ALLOWD_HTR_ID` | NUMERIC |  | This column stores the unique identifier for the contractual allowed write-off transaction that is associated with this liability bucket. |
| 4 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

