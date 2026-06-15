# HSP_ACCT_MULT_DRGS

> This table contains multiple diagnosis related group information for hospital accounts.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 36  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID with associated Single Billing Office information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DRG_ID_TYPE_ID` | NUMERIC |  | From the list of diagnosis-related group (DRG) filed to the hospital account, the unique ID of DRG code set for this row. |
| 4 | `DRG_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `DRG_MPI_CODE` | VARCHAR |  | This column extracts the Master Patient Index (MPI) IDs of diagnosis-related group (DRG) codes entered in the Multiple DRG grid of Hospital Billing - Coding for each Hospital Account. The MPI IDs shown here will be the IDs that correspond to the DRG MPI Type extracted in the DRG_ID_TYPE_ID column. |
| 6 | `DRG_REIMBURSEMENT` | NUMERIC |  | From the list of diagnosis-related groups (DRGs) filed to the hospital account, the expected reimbursement amount for the DRG in this row. |
| 7 | `DRG_MDC_VALUE` | VARCHAR |  | From the list of diagnosis-related group (DRG) filed to the hospital account, the Major Diagnostic Category value for the DRG in this row. |
| 8 | `DRG_WEIGHT` | NUMERIC |  | From the list of DRGs filed to the hospital account, the weight for the DRG in this row. |
| 9 | `DRG_PS_NAME` | VARCHAR |  | From the list of diagnosis-related groups (DRGs) filed to the hospital account, the severity of illness (SOI) category ID associated with the DRG in this row. |
| 10 | `DRG_ROM_NAME` | VARCHAR |  | The Risk of Mortality (ROM) category ID associated with the DRG is in this row. Epic Released Entries: 0- Refinement not possible 1- Minor 2- Moderate 3- Major 4- Extreme 5- Principal Dx Used for SOI/ROM Calc 6- Excluded 7- Duplicate Diagnosis 8- Excluded Complication of Care |
| 11 | `DRG_SHORT_LOS` | VARCHAR |  | The unique identifier for the treatment plan record. |
| 12 | `DRG_LONG_LOS` | VARCHAR |  | From the list of diagnosis-related group (DRG) filed to the hospital account, the long length of stay for the DRG in this row. |
| 13 | `DRG_AMLOS` | VARCHAR |  | From the list of DRGs filed to the hospital account, the arithmetic mean length of stay for the DRG in this row. |
| 14 | `DRG_GMLOS` | VARCHAR |  | From the list of diagnosis-related group (DRG) filed to the hospital account, the geometric mean length of stay for the DRG in this row. |
| 15 | `DRG_CST_OTLR_THRSH` | NUMERIC |  | The diagnosis-related group (DRG) cost outlier threshold for the hospital account. |
| 16 | `DRG_DAY_OTLR_THRSH` | NUMERIC |  | The diagnosis-related group (DRG) day outlier threshold for the hospital account. |
| 17 | `DRG_NRM_PT_RMB_AMT` | NUMERIC |  | The normal patient reimbursal amount for diagnosis-related group (DRG) on the hospital account. |
| 18 | `DRG_TG_FED_BLND_RT` | NUMERIC |  | The target fed blended rate for DRG on the hospital account. |
| 19 | `DRG_COND_CODE` | NUMERIC |  | The diagnosis-related group (DRG) condition code on the hospital account. |
| 20 | `DRG_FORMULA` | NUMERIC |  | The diagnosis-related group (DRG) formula information on the hospital account. |
| 21 | `DRG_LOS` | INTEGER |  | The diagnosis-related group (DRG) LOS for the hospital account. |
| 22 | `DRG_PAT_STATUS` | VARCHAR |  | The patient status for the diagnosis-related group (DRG) on the hospital account. |
| 23 | `DRG_ISP_SHR_AJ_AMT` | NUMERIC |  | The dispensed share adjustment amount for the diagnosis-related group (DRG) on the hospital account. |
| 24 | `DRG_INDIR_MED_AMT` | NUMERIC |  | The indirect medicated monetary amount for the diagnosis-related group (DRG) on the hospital account. |
| 25 | `DRG_CAPITAL_AMT` | NUMERIC |  | The capital monetary amount for the DRG on the hospital account. |
| 26 | `DRG_OTLR_RMB_AMT` | NUMERIC |  | The outlier reimbursement monetary amount for the diagnosis-related group (DRG) on the hospital account. |
| 27 | `DRG_CHG_CLM_AMT` | NUMERIC |  | The total diagnosis-related group (DRG) charges on claim for this DRG on this hospital account. |
| 28 | `DRG_OUTLIER_TYPE` | INTEGER |  | The outlier type for the diagnosis-related group (DRG) on the hospital account. |
| 29 | `DRG_OUTLIER_DAYS` | INTEGER |  | The number of outlier days for the diagnosis-related group (DRG) on the hospital account. |
| 30 | `DRG_OTLR_CST_AMT` | NUMERIC |  | The monetary outlier cost for the diagnosis-related group (DRG) on the hospital account. |
| 31 | `DRG_OUTLIER_REIMB` | NUMERIC |  | The outlier reimbursement for the diagnosis-related group (DRG) on the hospital account. |
| 32 | `DRG_CMT` | VARCHAR |  | The comment associated with the diagnosis-related group (DRG) on the hospital account. |
| 33 | `DRG_QLFR_C_NAME` | VARCHAR | org | Additional diagnosis-related group (DRG) Qualifier for the DRG Type and Code. |
| 34 | `DRG_BILLING_FLAG_YN` | VARCHAR |  | Indicates the diagnosis-related group (DRG) that is the primary Billing DRG for the hospital account. |
| 35 | `DRG_ECCS` | NUMERIC |  | The ECCS (episode clinical complexity score) associated with the DRG. |
| 36 | `DRG_IS_CMI_EXCLUD_YN` | VARCHAR |  | Indicates whether a DRG code from a DRG type is excluded from CMI calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

