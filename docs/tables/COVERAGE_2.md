# COVERAGE_2

> The COVERAGE_2 table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow of:** [COVERAGE](COVERAGE.md)  
**Primary key:** `CVG_ID`  
**Columns:** 75  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK | The unique identifier for the coverage record. |
| 2 | `STATUS_C_NAME` | VARCHAR |  | The category number of the status for this coverage record. |
| 3 | `IS_DEDUCT_MET_C_NAME` | VARCHAR |  | Indicates whether the deductible has been met for this coverage. The deductible can be established on the guarantor account or patient level. |
| 4 | `IS_ASGN_CVG_C_NAME` | VARCHAR |  | Indicated whether the provider's assignment status is set to Coverage Assignment for this coverage's payor. |
| 5 | `SIG_ON_FILE_DATE` | DATETIME |  | The date when the signature was filed. |
| 6 | `SIG_ON_FILE_LOC` | VARCHAR |  | The location at which the signature was filed. |
| 7 | `MEDIGAP_AUTH_YN` | VARCHAR |  | Indicates whether the payor for this coverage has Medigap authorization. |
| 8 | `TPL_RESOURCE_CODE` | VARCHAR |  | This column lists the Third Party Liability resource code for a specific plan. This code is either returned in the real-time eligibility response or found on the patient's insurance card. |
| 9 | `THIRD_PARTY_LIAB_YN` | VARCHAR |  | Indicates if there is third-party liability for this coverage. |
| 10 | `BENEFIT_CODE` | VARCHAR |  | The benefit code for this coverage. This can contain any facility-specific benefit code. |
| 11 | `EMPLOYEE_ID_NUM` | VARCHAR |  | The coverage subscriber's employee ID number. |
| 12 | `SCHEDULED_DISCON_DT` | DATETIME |  | The date when the coverage is scheduled to be discontinued. |
| 13 | `SCHEDULED_ACTV_DT` | DATETIME |  | The date when the coverage is scheduled to be activated. |
| 14 | `YR_ALLOW_DOL_TOT` | VARCHAR |  | The yearly dollar limit for payments against this coverage's payor. |
| 15 | `YR_ALLOW_DOL_USE` | VARCHAR |  | The year-to-date payments made against the coverage's payor. |
| 16 | `ORG_FOR_CLM_SUBMIT` | VARCHAR |  | The title or name of the organization to which submitted claims under this coverage will be sent. |
| 17 | `FINANCIAL_CLASS_C_NAME` | VARCHAR | org | The financial class for this coverage. This is only used for CMS claims forms and may not be reliably populated for reporting. Reporting should done using the financial class of the payor specified in this coverage. |
| 18 | `COVERAGE_FAX` | VARCHAR |  | The fax number for this coverage. |
| 19 | `FREE_TXT_PLAN_NAME` | VARCHAR |  | The free-text plan name for this coverage. |
| 20 | `FREE_TXT_PAYOR_NAME` | VARCHAR |  | The free-text payor name for this coverage. |
| 21 | `PLAN_FREE_TEXT` | VARCHAR |  | The format of the coverage's free-text plan. |
| 22 | `TEFRA_PAT_YN` | VARCHAR |  | Indicates whether the patient is TEFRA. A patient is TEFRA if an eligible Medicare beneficiary is covered by a group health plan. |
| 23 | `ADMISSION_SRC_C_NAME` | VARCHAR | org | The category number of the admission source. |
| 24 | `ENROLL_CODE_FBC` | VARCHAR |  | The Federal Employment Program enrollment code. |
| 25 | `GRP_NUMBER` | VARCHAR |  | The group number for the coverage. |
| 26 | `HMO_SITE_NUM` | VARCHAR |  | The site number for the coverage's HMO. |
| 27 | `HMO_SITE_PHONE` | VARCHAR |  | The phone number for the coverage's HMO. |
| 28 | `COPAY_AMOUNT` | VARCHAR |  | The copay amount for the coverage. |
| 29 | `CHAMP_SPON_STATUS_C_NAME` | VARCHAR | org | The CHAMPUS/Tricare sponsor's military status, obtained from the military identification card. |
| 30 | `SERVICE_BRANCH` | VARCHAR |  | The military service branch for a CHAMPUS/Tricare coverage subscriber. |
| 31 | `CHAMP_SPON_BRANCH_C_NAME` | VARCHAR | org | A CHAMPUS/Tricare coverage sponsor's military service branch. |
| 32 | `CHAMP_SPON_GRADE_C_NAME` | VARCHAR | org | A CHAMPUS/Tricare coverage sponsor's military pay grade. |
| 33 | `MCARE_OTHER_INS_CO` | VARCHAR |  | An additional insurance company providing coverage for a Medicare patient. |
| 34 | `MCARE_REC_DIS_YN` | VARCHAR |  | Indicates if a Medicare patient is receiving disability benefit. |
| 35 | `DIS_CVD_BY_EMP_YN` | VARCHAR |  | Indicates if a Medicare patient is receiving disability coverage from their employer. |
| 36 | `MCARE_100_EMP_YN` | VARCHAR |  | Indicates if a Medicare employer has over 100 employees. |
| 37 | `MCARE_AUTO_YN` | VARCHAR |  | Indicates if the illness or injury for this visit is due to an automobile accident. |
| 38 | `MCARE_LIAB_YN` | VARCHAR |  | Indicates if the illness or injury for this visit is due to a liability accident. |
| 39 | `MCARE_WK_COMP_YN` | VARCHAR |  | Indicates if a Medicare visit is covered by Workman's Compensation. |
| 40 | `MCARE_NON_AUTO_YN` | VARCHAR |  | Indicates if the patient's visit is due to an accident not involving automobiles. |
| 41 | `MCARE_BLACK_LUNG_YN` | VARCHAR |  | Indicates whether the illness is covered by the Black Lung program. |
| 42 | `MCARE_VA_YN` | VARCHAR |  | Indicates if the illness is covered by a Veterans' Administration program. |
| 43 | `MCARE_PARENT_EMP_YN` | VARCHAR |  | Indicates whether the patient's parents or guardians are employed. |
| 44 | `MCARE_CVD_GD_YN` | VARCHAR |  | For large group health plans, indicates if the patient is covered by their parent or guardian. |
| 45 | `MCARE_GD_EMP_100_YN` | VARCHAR |  | Indicates whether the employer of this patient's parent or guardian employs over 100 people. |
| 46 | `IS_MCARE_VET_ADMN_C_NAME` | VARCHAR | org | Indicates whether this coverage is for a Veterans' Administration program. |
| 47 | `MCARE_EMPLOYED_YN` | VARCHAR |  | Indicates whether the Medicare patient is employed. |
| 48 | `MCARE_ENRL_HMO_YN` | VARCHAR |  | Indicates if the Medicare patient is enrolled in an HMO. |
| 49 | `MCARE_CVD_EGHP_YN` | VARCHAR |  | Indicates whether the patient is covered by an employer group health plan. |
| 50 | `MCARE_EMP_20_YN` | VARCHAR |  | Indicates whether the Medicare patient is employed by an employer with over 20 employees. |
| 51 | `MCARE_REN_DIAL_YN` | VARCHAR |  | Indicates whether the patient is a renal dialysis patient in the first 12 months of entitlement. |
| 52 | `IS_MCARE_RENAL_DI_C_NAME` | VARCHAR |  | Indicates whether the patient is a renal dialysis patient. |
| 53 | `MCARE_1ST_18MO_YN` | VARCHAR |  | Indicates whether the patient is in the first 18 months of entitlement for renal dialysis. |
| 54 | `MCARE_HOME_DIAL_YN` | VARCHAR |  | Indicates whether the patient is a home dialysis patient. |
| 55 | `MCARE_SELF_EPO_YN` | VARCHAR |  | Indicates whether this patient self-administers EPO. |
| 56 | `MCARE_DISABLE_YN` | VARCHAR |  | Indicates whether a patient's Medicare coverage is due to disability. |
| 57 | `MCARE_SPSE_RET_YN` | VARCHAR |  | Indicates whether a Medicare patient's spouse is retired. |
| 58 | `MCARE_SPOUSE_RET_DT` | DATETIME |  | The date when a Medicare patient's spouse retired. |
| 59 | `MCARE_EMPR_INS_YN` | VARCHAR |  | Indicates whether a Medicare patient is insured by their employer. |
| 60 | `MCARE_RETIRE_YN` | VARCHAR |  | Indicates whether a Medicare patient is retired. |
| 61 | `MCARE_RETIRE_DATE` | DATETIME |  | The date when a Medicare patient retired. |
| 62 | `MCARE_FAM_EMPY_YN` | VARCHAR |  | Indicates whether a Medicare patient's spouse or another family member is employed. |
| 63 | `MCARE_OTHR_CVG_YN` | VARCHAR |  | Indicates whether a Medicare patient is covered because of their spouse or other family member. |
| 64 | `MCARE_SPC_EMP_YN` | VARCHAR |  | Indicates whether a Medicare patient's spouse is employed. |
| 65 | `MCARE_CVG_FRM_SP_YN` | VARCHAR |  | Indicates whether a Medicare patient is covered through their spouse's employer group health plan. |
| 66 | `VERIF_EVS_YN` | VARCHAR |  | Indicates if verification is done through Eligibility Verification Systems (EVS). |
| 67 | `EVS_VERIF_DATE` | DATETIME |  | The date when eligibility was verified with Eligibility Verification Systems (EVS). |
| 68 | `PAYOR_NAME` | VARCHAR |  | The coverage payor's name. |
| 69 | `PAYOR_CITY` | VARCHAR |  | The coverage payor's city. |
| 70 | `EXT_CVG_SRC_ORGANIZATION_ID` | NUMERIC |  | The Organization (DXO) that provided the information for this coverage. |
| 71 | `EXT_CVG_SRC_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 72 | `EXT_CVG_FHIR_IDENT` | VARCHAR |  | The FHIR Id of a coverage record on an external system that was used to create this coverage. |
| 73 | `EXT_CVG_OID` | VARCHAR |  | The OID of a coverage record on an external system that was used to create this coverage. |
| 74 | `EXT_PAYER_NAME` | VARCHAR |  | Payer name received for a coverage from an external payer system. |
| 75 | `EXT_PLAN_NAME` | VARCHAR |  | Plan name received for a coverage from an external payer system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [COVERAGE](COVERAGE.md).

