# HSP_ACCT_CPT_CODES

> This table contains hospital account CPT(R) codes from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple CPT™ codes can be stored in one hospital account, each CPT™ code will have a unique line number. |
| 3 | `CPT_CODE` | VARCHAR |  | A CPT™ code stored in the hospital account. |
| 4 | `CPT_CODE_DATE` | DATETIME |  | A date associated with a CPT™ code stored in the hospital account. |
| 5 | `CPT_PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `CPT_EVENT_NUMBER` | INTEGER |  | The event number associated with a CPT™ code stored in the hospital account. Event number are used to associate CPT™ codes with procedure codes. |
| 7 | `CPT_MODIFIERS` | VARCHAR |  | A modifier or modifiers associated with a CPT™ code stored in the hospital account. |
| 8 | `LMRP_CODE` | VARCHAR |  | A Local Medical Review Policy (LMRP) code associated with a CPT™ code stored in the hospital account. |
| 9 | `CPT_CODE_DESC` | VARCHAR |  | The description of a CPT® code stored in the hospital account. |
| 10 | `PX_APC_FAC_RMB_AMT` | NUMERIC |  | The monetary reimbursement amount for the procedure Ambulatory Payment Classification (APC) FAC on the hospital account. |
| 11 | `PX_OCE_EDIT_CODE` | VARCHAR |  | The procedure Outpatient Code Editor (OCE) edit code for the hospital account. |
| 12 | `PX_APC_CODE` | VARCHAR |  | The procedure Ambulatory Payment Classification (APC) code for the hospital account. |
| 13 | `PX_HCFA_PAYMT_AMT` | NUMERIC |  | The procedure Health Care Payment and Remittance Advice (HCFA) monetary payment amount for the hospital account. |
| 14 | `PX_COPAY_AMT` | NUMERIC |  | The monetary copay amount for the procedure on the hospital account. |
| 15 | `PX_REV_CODE_ID` | NUMERIC |  | The unique ID of the revenue code. |
| 16 | `PX_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 17 | `CPT_EXCLD_RPT_YN` | VARCHAR |  | Indicates whether to exclude CPT codes from clinical reporting. This is frequently used to filter out procedures copied over during an account merge to prevent double counting. |
| 18 | `CPT_QUANTITY` | INTEGER |  | Quantity of the CPT(R)/HCPCS code. Hospital accounts created prior to Epic 2014 have a null value in this column which implies a quantity of 1. |
| 19 | `CPT_POS_TYPE_C_NAME` | VARCHAR | org | Stores the Place of Service (POS) Type value for a coded CPT on an account.. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

