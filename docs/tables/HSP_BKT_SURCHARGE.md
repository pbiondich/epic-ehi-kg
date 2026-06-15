# HSP_BKT_SURCHARGE

> Holds information regarding percentages applied to buckets based on the date ranges of the bucket's charges.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFFECTIVE_DT` | DATETIME |  | Stores the effective date in the HSD that stored the settings used to calculate the surcharge. |
| 4 | `SURCHARGE_PERCENT` | NUMERIC |  | Percent used to calculate surcharge |
| 5 | `AMOUNT` | NUMERIC |  | This item stores the amount used for the surcharge for a date range. |
| 6 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account on the liability bucket record. |
| 7 | `SURCHARGABLE_AMT` | NUMERIC |  | This item stores the amount that the surcharge is applied to on the bucket. |
| 8 | `SRCHG_CREDIT_AMT` | NUMERIC |  | This item returns the total amount of surcharge credit transactions posted against a bucket. |
| 9 | `SRCHG_XFER_IN` | NUMERIC |  | Stores the total amount of surcharge that has transferred into a liability bucket. |
| 10 | `SRCHG_XFER_OUT` | NUMERIC |  | Stores the total amount of surcharge transferred out of a liability bucket. |
| 11 | `TAX_HAR_CER_RULE_ID` | VARCHAR |  | The unique Id of the general rule that was last used to generate tax charges. If the tax charges on this bucket generated due to multiple account rules then this contains no rule. |
| 12 | `TAX_HAR_CER_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

