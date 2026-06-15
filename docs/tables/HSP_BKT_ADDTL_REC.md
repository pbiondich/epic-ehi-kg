# HSP_BKT_ADDTL_REC

> Additional Payment Reconciliation Information This table holds current information sent back by the payor at a later date. This can be after the account has been closed. See table HSP_BKT_REC_HX for the history of these items.

**Primary key:** `BUCKET_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |
| 3 | `ADDTL_NA_AMT` | NUMERIC |  | Additional Payment Reconciliation Information - Not allowed amount |
| 4 | `ADDTL_PAYOR_PMT` | NUMERIC |  | This column stores the payer payment amount. |
| 5 | `ADDTL_NON_CVD_CHGS` | NUMERIC |  | Additional Payment Reconciliation Information - Non-covered charges |
| 6 | `ADDTL_TOT_CHARGES` | NUMERIC |  | This column stores the payer reported amount of total charges. |
| 7 | `ADDTL_REPORT_DATE` | DATETIME |  | This column stores the date on the report from the payer. |
| 8 | `ADDTL_REPT_TYPE_C_NAME` | VARCHAR | org | Additional Payment Reconciliation Information - report type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

