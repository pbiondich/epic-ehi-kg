# HSP_CLP_CMS_LINE

> This table contains claim line information for claims associated with the hospital account/liability bucket. For uniform medical billing (UB) claims, this table contains pre-processing charge information, which is used in the creation of UB claim lines. Post-processing claim line data for UB claims is stored in the HSP_CLP_REV_CODE table. For CMS claims, this table contains the post-processing claim line data.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 42  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim record associated with a single hospital account or liability bucket. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `REIMB_AMT` | NUMERIC |  | Stores the reimbursement amount for claim line. |
| 4 | `REIMB_METHOD_C_NAME` | VARCHAR |  | Stores the reimbursement method. |
| 5 | `FROM_SERV_DT` | DATETIME |  | Stores the from date for a claim line. For services that do not span multiple days, the service date will be held here. |
| 6 | `TO_SERV_DT` | DATETIME |  | Stores the through date for a claim line. |
| 7 | `POS_TYPE_PER_TX` | VARCHAR |  | Stores the place of service type per transaction. |
| 8 | `TOS_C_NAME` | VARCHAR | org | Stores the type of service for the claim line. |
| 9 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 10 | `PROC_DESC` | VARCHAR |  | Stores the procedure description. |
| 11 | `HCPCS_CODES` | VARCHAR |  | Stores the Healthcare Common Procedure Coding System code for the claim line. |
| 12 | `PROF_CLM_MODIFIERS` | VARCHAR |  | Stores modifiers on the claim line. |
| 13 | `DX_MAP` | VARCHAR |  | Comma-delimited list of diagnosis pointers for the claim line. |
| 14 | `QUANTITY` | NUMERIC |  | Stores the quantity associated with the claim line. |
| 15 | `OVRD_REV_CODE_ID` | NUMERIC |  | Stores the override revenue code. |
| 16 | `OVRD_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 17 | `CHARGE_AMT` | NUMERIC |  | Stores the charge amount for the claim line. |
| 18 | `INS_DUE_AMT` | NUMERIC |  | Stores the insurance amount due for the claim line. |
| 19 | `PAT_DUE_AMT` | NUMERIC |  | Stores the patient amount due for the claim line. |
| 20 | `NON_CVD_AMT` | NUMERIC |  | Stores the non-covered amount for the claim line. |
| 21 | `PAYMENT_AMT` | NUMERIC |  | Stores the payment amount for the claim line. |
| 22 | `INSURANCE_PAID_AMT` | NUMERIC |  | Stores the insurance amount paid for the claim line. |
| 23 | `PAT_PAID_AMT` | NUMERIC |  | Stores the patient amount paid for the claim line. |
| 24 | `ADJUSTMENT_AMT` | NUMERIC |  | Stores the adjustment amount for the claim line. |
| 25 | `PRINT_DESCRIPTIO_YN` | VARCHAR |  | This controls procedure description printing for professional claims. |
| 26 | `REV_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 27 | `DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 28 | `PX_START_DT` | DATETIME |  | Start date for timed procedures. |
| 29 | `PX_STOP_DT` | DATETIME |  | Stop date for timed procedures. |
| 30 | `PX_START_TM` | DATETIME (Local) |  | Start time for timed procedures. |
| 31 | `PX_STOP_TM` | DATETIME (Local) |  | Stop time for timed procedures. |
| 32 | `LINE_COMMENT` | VARCHAR |  | Comment for the line. |
| 33 | `LINE_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 34 | `CMS_CODE_TYPE_C_NAME` | VARCHAR | org | Stores the code type for the transaction level Healthcare Common Procedure Coding System code override. If a procedure has been assigned to the line without setting the override, this column will be left blank. |
| 35 | `CMS_REND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 36 | `CMS_MOLDX_TEST_CODE` | VARCHAR |  | Holds the auxiliary procedure code for a CMS line. |
| 37 | `CMS_AUXPX_CD_TYPE_C_NAME` | VARCHAR |  | Holds the type of auxiliary procedure code when one is applicable to a CMS line. |
| 38 | `CMS_PRIOR_AUTH` | VARCHAR |  | Stores the prior-authorization number for a service line. |
| 39 | `CMS_REF_NUM` | VARCHAR |  | Stores the referral number for a service line. |
| 40 | `CMS_LINKED_AUTH_ID` | NUMERIC |  | Stores the professional billing charge level linked authorization ID. |
| 41 | `CMS_MEDICARE_PAID_AMT` | NUMERIC |  | For eMedNY 150003 claims, this is the amount that Medicare paid for this service line. This appears in field 24K (SVC_LN_INFO_2.LN_MCR_PAID_AMT). The EMEDNY_MEDICARE_PLANS profile variable can be used to control which coverages count as Medicare coverages. |
| 42 | `INVOICE_GRP_LN` | VARCHAR |  | The group line number on the invoice record that corresponds to the data in INVOICE_CLM_LN. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

