# COVERAGE_3

> The COVERAGE_3 table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow of:** [COVERAGE](COVERAGE.md)  
**Primary key:** `CVG_ID`  
**Columns:** 57  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK | The unique identifier for the coverage record. |
| 2 | `PAYOR_STATE_C_NAME` | VARCHAR | org | The state of the coverage payer. |
| 3 | `PAYOR_ZIP` | VARCHAR |  | The ZIP code of the coverage payer. |
| 4 | `PAYOR_PHONE` | VARCHAR |  | The phone number of the coverage payer. |
| 5 | `PAYOR_CLAIM_OFC_NUM` | VARCHAR |  | The claim office number of the coverage payer. |
| 6 | `REF_PROV_NAME_ID` | VARCHAR |  | The name of the Health Maintenance Organization's referring physician. |
| 7 | `REF_PROV_NAME_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 8 | `REF_PROV_CITY` | VARCHAR |  | The city of the Health Maintenance Organization's referring physician. |
| 9 | `REF_PROV_ZIP` | VARCHAR |  | The ZIP code of the Health Maintenance Organization's referring physician. |
| 10 | `AUTH_NUM` | VARCHAR |  | The authorization number for this coverage. |
| 11 | `AUTHORIZATION_DTTM` | DATETIME |  | The authorization date and time for this coverage. |
| 12 | `AUTH_PERSON` | VARCHAR |  | The name of the person who authorized services for this coverage. |
| 13 | `VERIF_DATETIME` | DATETIME |  | The date and time when authorization was obtained. |
| 14 | `MED_ASSIST_CARD` | VARCHAR |  | The medical assistance card number. |
| 15 | `MED_ASSIST_CODE_C_NAME` | VARCHAR | org | The medical assistance code. |
| 16 | `MED_ASSIST_STATUS` | VARCHAR |  | The medical assistance status. |
| 17 | `MED_ASSIST_COV_CODE` | VARCHAR |  | The medical assistance coverage code. |
| 18 | `IS_CVG_VA_PROG_YN_NAME` | VARCHAR | org | Indicates if the coverage is for a Veterans' Administration program. |
| 19 | `IS_MC_PROGRAM_YN` | VARCHAR |  | Indicates whether the coverage is for a managed care program. |
| 20 | `MC_PRIM_PROV` | VARCHAR |  | The primary provider for a managed care coverage. |
| 21 | `MC_AUTH_NUM` | VARCHAR |  | The authorization number for a managed care coverage. |
| 22 | `MC_AUTH_PHONE_NUM` | VARCHAR |  | The authorization phone number for a managed care coverage. |
| 23 | `TYPE_OF_COVERAGE_C_NAME` | VARCHAR | org | The type of coverage. |
| 24 | `ALSO_HAS_MCARE_YN` | VARCHAR |  | Indicates whether the coverage subscriber also has Medicare. |
| 25 | `MAJOR_MEDICAL_C_NAME` | VARCHAR | org | Indicates whether the patient has Major Medical coverage. |
| 26 | `MCAID_GRP_NO_SUF_C_NAME` | VARCHAR | org | The two letters at the end of the recipient number on the Medicaid card. |
| 27 | `CHAMPUS_RANK` | VARCHAR |  | The CHAMPUS/Tricare rank. |
| 28 | `CHAMPUS_GRADE` | VARCHAR |  | The CHAMPUS/Tricare grade. |
| 29 | `BC_BS_CNTRCT_ACCT_C_NAME` | VARCHAR | org | The contract account name on a Blue Cross/Blue Shield insurance card. |
| 30 | `MAC_PROV_PHONE_NUM` | VARCHAR |  | The phone number for the primary provider. |
| 31 | `MAC_AUTH_CNCT_PRSN` | VARCHAR |  | The person who provided authorization information for this visit. |
| 32 | `MAC_COMMENT` | VARCHAR |  | Comments regarding authorization or denial. |
| 33 | `MAC_PMP_AUTH_C_NAME` | VARCHAR |  | The authorization for this visit. |
| 34 | `MCARE_RR_SUB_NO_P_C_NAME` | VARCHAR | org | The subscriber number for this managed care coverage. |
| 35 | `RECIPROCITY_NO` | VARCHAR |  | The reciprocity number for this coverage. |
| 36 | `MAC_AUTH_ENT_PRSN` | VARCHAR |  | The person who entered the authorization number for this managed care coverage. |
| 37 | `THERAPY_TYPE_C_NAME` | VARCHAR | org | The therapy type for this coverage. |
| 38 | `THERAPY_PLAN_DATE` | DATETIME |  | The date when the therapy plan was established. |
| 39 | `THERAPY_START_DT` | DATETIME |  | The date when the therapy started. |
| 40 | `LAST_MENSTRUAL_DATE` | VARCHAR |  | The patient's last menstrual date. |
| 41 | `AUTH_VALID_FROM_DT` | DATETIME |  | The date when the authorization became valid. |
| 42 | `AUTH_VALID_TO_DATE` | DATETIME |  | The date when the authorization became invalid. |
| 43 | `COMMERCIAL_AUTH_NUM` | VARCHAR |  | The commercial authorization number. |
| 44 | `COMM_AUTH_PRSN` | VARCHAR |  | The person who authorized the commercial coverage. |
| 45 | `MC_COBRA_STATUS_YN` | VARCHAR |  | Indicated whether a managed care coverage has Consolidated Omnibus Budget Reconciliation Act status. |
| 46 | `MC_COBRA_DATE` | DATETIME |  | The date when a managed care coverage received Consolidated Omnibus Budget Reconciliation Act status. |
| 47 | `PB_ACCT_CREATED_YN` | VARCHAR |  | Indicates whether a premium billing account was created for this coverage. |
| 48 | `ALTR_CVG_ATTN` | VARCHAR |  | The alternate name of the organization to which claims submitted under this coverage can be sent. |
| 49 | `ALTR_CITY` | VARCHAR |  | The alternate city to which claims under this coverage can be sent. |
| 50 | `ALTR_STATE_C_NAME` | VARCHAR |  | The alternate state to which claims submitted under this coverage can be sent. |
| 51 | `ENROLL_REASON_REG_C_NAME` | VARCHAR | org | The enrollment reason category number for this subscriber with this particular payer or plan. |
| 52 | `EXT_UPD_TYPE_C_NAME` | VARCHAR |  | This item stores what kind of change was requested by the external user. |
| 53 | `EXT_UPDATE_COMMENT` | VARCHAR |  | This item stores the comment that accompanies the external update request. |
| 54 | `ENROLL_RECV_DATE` | DATETIME |  | The enrollment received date for this coverage. |
| 55 | `PRIOR_LIS_DATE` | DATETIME |  | The most recent LIS period date. |
| 56 | `ALT_TRANSPLANT_PAYER_OPT_C_NAME` | VARCHAR | org | Use this item in conjunction with Alternate Payer configuration in the Plan record to help automate claims processing to alternate transplant payers when the relationship between Primary Plan and Alternate Payer/Plan is not 1:1. |
| 57 | `PB_PAID_THROUGH_DATE` | DATETIME |  | The date at which the coverage's premium has been fully paid through. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [COVERAGE](COVERAGE.md).

