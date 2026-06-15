# PR_EST_FAC_FEES

> The facility fees information for the price estimate. Facility fees are generated in Resolute Hospital Billing.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 38  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CODE_TYPE_C_NAME` | VARCHAR |  | Category to indicate which type of code (DRG/ICD/CPT) was used when preparing the estimate. |
| 4 | `DRG_CODE_ID` | VARCHAR |  | Contains the DRG code upon which the estimate for the facility fees is based. |
| 5 | `DRG_CODE_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 6 | `ICD_CODE_ID` | VARCHAR |  | The ICD code upon which the estimate for the facility fees is based. |
| 7 | `ICD_CODE_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 8 | `CPT_CODE` | VARCHAR |  | Stores the CPT code upon which the hospital fees estimate is based. |
| 9 | `LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 10 | `ACCT_CLASS_C_NAME` | VARCHAR | org | Account class for this facility fee estimate. |
| 11 | `BILLED_AMT` | NUMERIC |  | Estimated charge amount for an Hospital Billing (HB) historical case estimate. |
| 12 | `ALLOWED_AMT` | NUMERIC |  | The estimated allowed amount for the facility fees. |
| 13 | `SELF_PAY_AMT` | NUMERIC |  | The estimated self-pay amount for the facility fees. |
| 14 | `SERVICE_TYPE_ID` | VARCHAR | FK→ | The benefit service type used to determine benefit information for the facility fees section. This information comes from the benefit record attached to the estimate. Use the PR_EST_INFO table, BENEFITS_INFO_ID column to link this data. |
| 15 | `SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 16 | `ACTUAL_DISCOUNT_AMT` | NUMERIC |  | The estimated discount amount for the facility fees. |
| 17 | `SYSTEM_DISCOUNT_AMT` | NUMERIC |  | The system-calculated discount amount for the facility fees. |
| 18 | `SYS_CHG_AMT` | NUMERIC |  | The system-calculated charge amount for a Hospital Billing (HB) historical case estimate. |
| 19 | `SYS_ALLOWED_AMT` | NUMERIC |  | The system-calculated allowed amount for a Hospital Billing (HB) historical case estimate. |
| 20 | `HB_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 21 | `HB_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 22 | `BASE_CLASS_C_NAME` | VARCHAR |  | Base class for this facility fee estimate. |
| 23 | `HB_MEDIAN_CHARGES` | NUMERIC |  | Median charge amount from historical cases. |
| 24 | `HB_MEDIAN_ALLOWED` | NUMERIC |  | Median allowed amount from historical cases. |
| 25 | `HB_CONTRACT_ID` | NUMERIC |  | The reimbursement contract calculated for a Hospital Billing context. |
| 26 | `HB_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 27 | `HB_OVRIDE_CONTRACT_ID` | NUMERIC |  | The reimbursement contract manually selected to find historical data in a Hospital Billing context. |
| 28 | `HB_OVRIDE_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 29 | `HB_OVRIDE_BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 30 | `HB_OVRIDE_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 31 | `HB_OVRIDE_FIN_CL_C_NAME` | VARCHAR | org | The financial class category ID in an Hospital Billing context for the patient estimate. |
| 32 | `FAC_ADDL_LINE` | INTEGER |  | This item holds a line number in the PR_EST_ADDL_INFO table, which stores additional information about the charge line. |
| 33 | `SELF_PAY_DISCNT_CONTRACT_ID` | NUMERIC |  | The reimbursement discount contract calculated as part of a self-pay discount. |
| 34 | `SELF_PAY_DISCNT_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 35 | `SELF_PAY_DISCNT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 36 | `SELF_PAY_DISCNT_SCOPE_C_NAME` | VARCHAR |  | Scope used to find median case for self-pay discount by contract calculation. |
| 37 | `SELF_PAY_DISCNT_MEDIAN_AMT` | NUMERIC |  | Median contractual amount to apply as part of a self-pay discount. |
| 38 | `REPRESENT_HSP_ACCOUNT_ID` | NUMERIC |  | The representative Hospital Account used during the calculation of the context line. For HB Case contexts, the historical median Hospital Account used to calculate amounts will be saved. For HB Procedure contexts, the representative Hospital Account used to create a simulated claim will be saved. This item does not store the Hospital Account used to find related procedure information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_TYPE_ID` | [BENEFIT_SVC_TYPE](BENEFIT_SVC_TYPE.md) | sole_pk | high |

