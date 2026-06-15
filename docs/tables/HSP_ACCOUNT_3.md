# HSP_ACCOUNT_3

> This table contains hospital account information from the Hospital Accounts Receivable (HAR) master file. This third hospital account table has the same basic structure as HSP_ACCOUNT and HSP_ACCOUNT_2, but was created as a third table to prevent the other tables from getting any larger. This table will exclude professional billing accounts in classic PB self-pay service areas.

**Overflow of:** [HSP_ACCOUNT](HSP_ACCOUNT.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 61  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the hospital account. |
| 2 | `ISS_TRAUMA` | INTEGER |  | The trauma "Injury Severity Score" (1-75) |
| 3 | `ADMIT_TYPE_EPT_C_NAME` | VARCHAR | org | Admit type as stored on patient record. |
| 4 | `PAT_STS_EPT_C_NAME` | VARCHAR | org | Patient Status as stored on patient record. |
| 5 | `PMTPLN_EST_INIT_BAL` | NUMERIC |  | This column stores the initial estimated payment plan balance for the hospital account. |
| 6 | `IP_ADMIT_DATE_TIME` | DATETIME (Local) |  | This column indicates the inpatient admission date and time associated with the hospital account. This can differ from the admission date and time and represents the date and time a patient was admitted with an IP base class. |
| 7 | `NEW_CANCER_YNU` | VARCHAR |  | This column stores a yes/no/unknown record of whether or not a patient's cancer is new. |
| 8 | `HYPERALIMENT_DAYS` | INTEGER |  | This column stores the number of days that a patient received hyperalimentation therapy. |
| 9 | `BAD_DEBT_FLAG_YN` | VARCHAR |  | Bad Debt Flag. This flag determines if an account's non-prebilled balance is in bad debt. This is only used if account-based bad debt is used. |
| 10 | `PAT_HOUSE_NUM` | VARCHAR |  | House number in the address in patient demographic information on a hospital account. Added to support international address formats. |
| 11 | `FAC_TRANS_FROM_C_NAME` | VARCHAR | org | The facility the patient was transferred from prior to their stay. |
| 12 | `FAC_TRANS_TO_C_NAME` | VARCHAR |  | The facility the patient was transferred to after their stay. |
| 13 | `TISSUE_REMOVED_YN` | VARCHAR |  | This item represents if tissue was removed during surgery. |
| 14 | `READMIT_RLTD_YN` | VARCHAR |  | This item represents if the patient was readmitted for a related reason. |
| 15 | `WNDCARE_PRVD_YN` | VARCHAR |  | This item represents if wound care was provided during this visit. |
| 16 | `OSHPD_ADM_SITE_C_NAME` | VARCHAR | org | The OSHPD admission site category number for this hospital account. This data is populated by coders in the abstracting activity. The abstracting activity must be configured to include this field to use this. |
| 17 | `OSHPD_LIC_SITE_C_NAME` | VARCHAR | org | The OSHPD licensure of site category number for this hospital account. This data is populated by coders in the abstracting activity. The abstracting activity must be configured to include this field to use this. |
| 18 | `OSHPD_RTE_ADM_C_NAME` | VARCHAR | org | The OSHPD route of admission category number for this hospital account. This data is populated by coders in the abstracting activity. The abstracting activity must be configured to include this field to use this. |
| 19 | `OSHPD_TYP_CARE_C_NAME` | VARCHAR | org | The OSHPD patient's type of care category number for this hospital account. This data is populated by coders in the abstracting activity. The abstracting activity must be configured to include this field to use this. |
| 20 | `HAS_OPEN_OVRP_BD_YN` | VARCHAR |  | Indicates whether the hospital account has open overpayment records. |
| 21 | `EBC_BIRTH_DT_TM` | DATETIME |  | The date and time of birth on the electronic birth certificate for the child that is associated with this hospital account. |
| 22 | `HH_HSB_ID` | NUMERIC |  | This column stores the unique identifier for the home health summary block that is associated with this hospital account. |
| 23 | `SELF_PAY_YN` | VARCHAR |  | Indicates whether this hospital account is self-pay. |
| 24 | `EBC_LAST_MENSES_FT` | VARCHAR |  | The date of the mother's last normal menses prior to the birth. |
| 25 | `SBO_SPLIT_HAR_ID` | NUMERIC |  | This column stores the unique identifier for a mixed hospital account used with splits in shared-mode single billing office. This will be populated on professional billing-only hospital accounts that were created as the result of splitting a mixed hospital account. |
| 26 | `BILL_DRG_QLFR_C_NAME` | VARCHAR | org | This column stores the additional diagnosis-related group (DRG) qualifier for the billing DRG type and code. |
| 27 | `ACTUAL_COPAY_AMT` | NUMERIC |  | For all insurance buckets of the last coverage in the filing order, the total copay specified by insurance on payments. |
| 28 | `ACTUAL_COINS_AMT` | NUMERIC |  | For all insurance buckets of the last coverage in the filing order, the total coinsurance specified by insurance on payments. |
| 29 | `ACTUAL_DED_AMT` | NUMERIC |  | For all insurance buckets of the last coverage in the filing order, the total deductible specified by insurance on payments. |
| 30 | `SBO_BILL_AREA_ID` | NUMERIC |  | The bill area associated with the PB HAR. When set this indicates we are splitting PB HARs by bill area. |
| 31 | `SBO_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 32 | `MYC_LST_ST_VW_DTTM` | DATETIME (UTC) |  | This column stores the date and time when this Hospital Billing statement was last viewed in MyChart for this hospital account. If you are using hospital account-level statements, this field will be updated when that specific hospital account statement is viewed in MyChart. If you are using guarantor-level statements, then this field will be updated when a guarantor statement that includes this hospital account is viewed in MyChart. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 33 | `MYC_LST_DB_VW_DTTM` | DATETIME (UTC) |  | This column stores the date and time when a Hospital Billing detail bill was last viewed in MyChart for this hospital account. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 34 | `MYC_LST_LTR_VW_DTTM` | DATETIME (UTC) |  | This column stores the date and time when a Hospital Billing letter was last viewed in MyChart for this hospital account. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 35 | `CDI_SPECIALIST_ID` | VARCHAR |  | Stores the person responsible for the CDI process. |
| 36 | `CDI_SPECIALIST_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `CDI_START_DATE` | DATETIME |  | Stores the date the CDI review started. |
| 38 | `CDI_LAST_RVW_DATE` | DATETIME |  | Stores the last date the CDI review was done. |
| 39 | `CDI_DRG_CHANGED_YN` | VARCHAR |  | This column indicates whether the clinical documentation improvement (CDI) queries resulted in a DRG change. |
| 40 | `CDI_INITIAL_DRG_ID` | VARCHAR |  | Stores the initial DRG before the CDI review is complete. |
| 41 | `CDI_INITIAL_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 42 | `CDI_INITIAL_REIMB` | NUMERIC |  | Stores the expected reimbursement based on the initial DRG. |
| 43 | `CDI_INITIAL_DRG_WT` | NUMERIC |  | Stores the initial DRG weight. |
| 44 | `CDI_WORKING_DRG_ID` | VARCHAR |  | Stores the working DRG assigned by the CDI specialist. |
| 45 | `CDI_WORKING_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 46 | `CDI_WORKING_REIMB` | NUMERIC |  | Stores the expected reimbursement based on the working DRG. |
| 47 | `CDI_WORKING_DRG_WT` | NUMERIC |  | Stores the working DRG weight. |
| 48 | `CDI_PRIMARY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 49 | `CDI_DRG_MATCH_YN` | VARCHAR |  | Indicates whether the final DRG selected by the coder matches the working DRG specified by the CDI specialist. |
| 50 | `BP_DIASTOLIC` | NUMERIC |  | Diastolic Blood Pressure |
| 51 | `PULSE` | NUMERIC |  | The pulse for the patient on the hospital account. This is an abstracting item. The data can be configured to copy from the first pulse taken on the primary contact. |
| 52 | `BP_SYSTOLIC` | NUMERIC |  | Systolic Blood Pressure |
| 53 | `PRELIM_COD_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 54 | `COD_RECORD_ID` | NUMERIC |  | This column stores the unique identifier for the coding record for CDI that is associated with the hospital account. |
| 55 | `CMS_OP_ESRD_STRT_DT` | DATETIME |  | This column stores the date the patient started to receive maintenance dialysis treatments for end-stage renal disease (ESRD). |
| 56 | `CMS_OP_ESRD_DX_G_DT` | DATETIME |  | The first date that the acute comorbidity of gastrointestinal bleeding was present during maintenance dialysis treatments for ESRD. |
| 57 | `CMS_OP_ESRD_DX_B_DT` | DATETIME |  | This column stores the first date the acute comorbidity of bacterial pneumonia was present during maintenance dialysis treatments for end-stage renal disease (ESRD). |
| 58 | `CMS_OP_ESRD_DX_P_DT` | DATETIME |  | The first date that the acute comorbidity of pericarditis was present during maintenance dialysis treatments for ESRD. |
| 59 | `BILLING_DRG_SRC_C_NAME` | VARCHAR |  | This virtual item displays the source code set of the billing DRG. |
| 60 | `NYS_PROC_STRT_DTTM` | DATETIME |  | The start date and time that the ambulatory surgery patient entered the operating room exclusive of pre-op (preparation) and post-op (recovery) time. This is used for New York SPARCS reporting. |
| 61 | `NYS_PROC_END_DTTM` | DATETIME |  | The end date and time that the ambulatory surgery patient left the operating room exclusive of pre-op (preparation) and post-op (recovery) time. This is used for New York SPARCS reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [HSP_ACCOUNT](HSP_ACCOUNT.md).

