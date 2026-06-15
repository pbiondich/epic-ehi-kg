# HSP_ACCT_ALT_DRGS

> This table stores the multiple Diagnosis Related Group (DRG) information for the alternate ICD code set when dual coding a hospital account.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALT_DRG_ID_TYPE_ID` | NUMERIC |  | The unique ID of the ID Type associated with this diagnosis related group ID for the alternate code set. |
| 4 | `ALT_DRG_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `ALT_DRG_QLFR_C_NAME` | VARCHAR | org | Additional diagnosis-related group (DRG) Qualifier for the DRG Type and Code for the alternate code set. |
| 6 | `ALT_DRG_ID` | VARCHAR |  | The unique ID of the diagnosis-related group (DRG) code for the alternate code set that is associated with this hospital account. |
| 7 | `ALT_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 8 | `ALT_DRG_BILL_FLG_YN` | VARCHAR |  | Indicates the diagnosis-related group (DRG) that is the primary Billing DRG for the hospital account for the alternate code set. |
| 9 | `ALT_DRG_REIMB` | NUMERIC |  | Stores the diagnosis-related group (DRG) reimbursement for the alternate code set. |
| 10 | `ALT_DRG_MDC_VALUE` | VARCHAR |  | Stores the Major Diagnostic Category (MDC) values for the alternate code set. |
| 11 | `ALT_DRG_WEIGHT` | NUMERIC |  | Stores the diagnosis-related group (DRG) weight for the alternate code set. |
| 12 | `ALT_DRG_PS_C_NAME` | VARCHAR |  | Stores the severity of index (SOI) for the diagnosis-related group (DRG) for the alternate code set. |
| 13 | `ALT_DRG_SHORT_LOS` | VARCHAR |  | Stores the diagnosis-related group (DRG) short length of stay (LOS) for the alternate code set. |
| 14 | `ALT_DRG_LONG_LOS` | VARCHAR |  | Stores the diagnosis-related group (DRG) long length of stay (LOS) for the alternate code set. |
| 15 | `ALT_DRG_AMLOS` | VARCHAR |  | Stores the diagnosis-related group (DRG) arithmetic mean length of stay (LOS) for the alternate code set. |
| 16 | `ALT_DRG_GMLOS` | VARCHAR |  | Stores the diagnosis-related group (DRG) geometric mean length of stay (LOS) for the alternate code set. |
| 17 | `ALT_CST_OTLR_THRSH` | NUMERIC |  | Stores the diagnosis-related group (DRG) cost outlier threshold for the alternate code set. |
| 18 | `ALT_DAY_OTLR_THRSH` | NUMERIC |  | Stores the diagnosis-related group (DRG) day outlier threshold for the alternate code set. |
| 19 | `ALT_OUTLIER_DAYS` | INTEGER |  | Stores the diagnosis-related group (DRG) outlier days for the alternate code set. |
| 20 | `ALT_OTLR_CST_AMT` | NUMERIC |  | Stores the diagnosis-related group (DRG) outlier cost for the alternate code set. |
| 21 | `ALT_OUTLIER_REIMB` | NUMERIC |  | Stores the diagnosis-related group (DRG) outlier reimbursement amount for the alternate code set. |
| 22 | `ALT_PAT_STATUS` | VARCHAR |  | Stores the diagnosis-related group (DRG) reimbursement indicator for the alternate code set. |
| 23 | `ALT_DISP_SHARE_ADJ` | NUMERIC |  | Stores the diagnosis-related group (DRG) disproportionate share amount for the alternate code set. |
| 24 | `ALT_IND_MED_AMT` | NUMERIC |  | Stores the indirect medicated monetary amount for the alternate diagnosis-related group (DRG) on the hospital account. |
| 25 | `ALT_CAPITAL_AMT` | NUMERIC |  | This item stores the diagnosis-related group (DRG) capital amount for the alternate code set. |
| 26 | `ALT_DRG_TOT_CHG` | NUMERIC |  | Stores the diagnosis-related group (DRG) total charges on claim for the alternate code set. |
| 27 | `ALT_DRG_LOS` | INTEGER |  | Stores the diagnosis-related group (DRG) length of stay (LOS) for the alternate code set. |
| 28 | `ALT_NRM_PT_RMB_AMT` | NUMERIC |  | Stores the diagnosis-related group (DRG) normal patient reimbursement for the alternate code set. |
| 29 | `ALT_TG_FED_BLND_RT` | NUMERIC |  | Stores the diagnosis-related group (DRG) target federal blended rate for the alternate code set. |
| 30 | `ALT_DRG_COND_CODE` | INTEGER |  | Stores the diagnosis-related group (DRG) condition code for the alternate code set. |
| 31 | `ALT_DRG_FORMULA` | INTEGER |  | Stores the diagnosis-related group (DRG) formula for the alternate code set. |
| 32 | `ALT_DRG_COMMENT` | VARCHAR |  | Stores the diagnosis-related group (DRG) comment for the alternate code set. |
| 33 | `ALT_DRG_ROM_C_NAME` | VARCHAR |  | Stores the risk of mortality (ROM) for the diagnosis-related group (DRG) for the alternate code set. |
| 34 | `ALT_OL_REIMB_AMT` | NUMERIC |  | Stores the diagnosis-related group (DRG) outlier amount for the alternate code set. |
| 35 | `ALT_OUTLIER_TYPE` | NUMERIC |  | Stores the diagnosis-related group (DRG) outlier type for the alternate code set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

