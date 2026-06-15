# HSP_CLP_REV_CODE

> This table contains the revenue code list for the claim print records associated with the hospital account/liability bucket.

**Primary key:** `CLAIM_PRINT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record associated with a single hospital account or liability bucket. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date for the creation of the record in internal format. (There is only one contact date per claim print record.) |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `UB_MIN_SERVICE` | DATETIME |  | The minimum service date for the claim print record. |
| 5 | `UB_MAX_SERVICE` | DATETIME |  | The maximum service date for the claim print record. |
| 6 | `UB_CHARGES` | NUMERIC |  | The uniform billing charges on the claim |
| 7 | `UB_MODIFIER` | VARCHAR |  | The modifier for the claim print record. |
| 8 | `UB_CPT_CODE` | VARCHAR |  | The uniform billing current procedural terminology code on the claim print record. |
| 9 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the hospital account associated with this claim print record. |
| 10 | `CM_PHY_OWN_ID` | VARCHAR |  | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| 11 | `REV_CODE_EXT` | VARCHAR |  | The external uniform billing revenue code. |
| 12 | `UB_REV_CD_DESC` | VARCHAR |  | The description of the uniform billing line. |
| 13 | `UB_HIPPS_CD` | VARCHAR |  | The uniform billing line health insurance prospective payment system code. |
| 14 | `UB_QTY` | VARCHAR |  | The uniform billing line quality. |
| 15 | `UB_NON_CVD_AMT` | NUMERIC |  | The non-covered amount for the uniform billing line. |
| 16 | `UB_LMRP_CD` | VARCHAR |  | The uniform billing local coverage determination code. |
| 17 | `UB_HCPCS_RATE` | VARCHAR |  | The uniform billing healthcare common procedure coding system code and modifier or rate. |
| 18 | `UB_CODE_TYPE_C_NAME` | VARCHAR | org | The code type for the uniform billing claim line. If there is no code type this field will be blank. |
| 19 | `UB_PRIOR_AUTH` | VARCHAR |  | The prior authorization number for the uniform billing line. |
| 20 | `UB_RFL_NUM` | VARCHAR |  | The uniform billing line referral number. |
| 21 | `UB_REND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `UB_LINE_SRC_C_NAME` | VARCHAR |  | The category of the line source for the uniform billing line. |
| 23 | `UB_REIMB_AMT` | NUMERIC |  | The reimbursement amount for the uniform billing line. |
| 24 | `UB_REIMB_CNTRCT_AMT` | NUMERIC |  | The reimbursement contract amount for the uniform billing line. |
| 25 | `UB_SVC_DATE` | DATETIME |  | The service date of the uniform billing service line. |
| 26 | `UB_MOLDX_TEST_CODE` | VARCHAR |  | The auxiliary procedure code for a uniform billing line. |
| 27 | `UB_AUXPX_CD_TYPE_C_NAME` | VARCHAR |  | The type of auxiliary procedure code when one is applicable to a uniform billing line. |
| 28 | `UB_AUTH_ID` | NUMERIC |  | Stores the hospital billing charge level linked authorization ID. |
| 29 | `UB_REF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

