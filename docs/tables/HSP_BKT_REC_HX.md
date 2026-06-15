# HSP_BKT_REC_HX

> Additional Payment Reconciliation Information History table. This table stores a history of the amounts from HSP_BKT_ADDTL_REC, which has the current values.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_C_NAME` | VARCHAR |  | Additional Payment Reconciliation Information - Source of the change |
| 4 | `INSTANT_OF_ENTRY_TM` | DATETIME (Local) |  | Additional Payment Reconciliation Information - Instant when the information was updated |
| 5 | `ADDTL_NA_AMT_HX` | NUMERIC |  | Additional Payment Reconciliation Information - Not allowed amount history |
| 6 | `ADDTL_PAYOR_PMT_HX` | NUMERIC |  | This column stores the payer payment amount history. |
| 7 | `ADDTL_N_CVD_CHGS_HX` | NUMERIC |  | Additional Payment Reconciliation Information - Non-covered charges history |
| 8 | `ADDTL_TOT_CHGS_HX` | NUMERIC |  | This column stores the payer reported amount of total charges history. |
| 9 | `ADDTL_REPT_HX_DATE` | DATETIME |  | This column stores the date on the report from the payer history. |
| 10 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |
| 11 | `ADDTL_TYPE_HX_C_NAME` | VARCHAR | org | Additional Payment Reconciliation Information - report type history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

