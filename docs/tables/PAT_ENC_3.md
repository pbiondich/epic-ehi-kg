# PAT_ENC_3

> This table supplements the PAT_ENC and PAT_ENC_2 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN`  
**Columns:** 37  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CHKOUT_USER_ID` | VARCHAR |  | The unique ID number of the user who completed the check out process for the patient for this encounter. If the encounter has not been checked out, this field will appear as "null." This ID may be encrypted. |
| 4 | `CHKOUT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ENC_BILL_AREA_ID` | NUMERIC |  | The bill area which should be assigned to charges created from this encounter. The available bill areas to choose from will be determined based on lists in the provider and department records. |
| 6 | `ENC_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 7 | `RX_CHG_ADMIT_FLG_C_NAME` | VARCHAR |  | This item contains the status of charge suppression for the patient. 1 indicates all charges are being suppressed. 2 indicates suppressed charges are now dropped. 3 indicates some or all charges are currently being suppressed. |
| 8 | `DX_UNIQUE_COUNTER` | VARCHAR |  | The number of unique diagnoses associated with this patient encounter. Unique diagnoses are stored in item EPT 18425, which is extracted by the DX_UNIQUE column in the PAT_ENC_DX table. |
| 9 | `HP_DEFAULTED_YN` | VARCHAR |  | Whether the hospital problem was automatically populated from the list of admission diagnoses. This column will have a Y if the problem was populated from an admission diagnosis and an N otherwise. |
| 10 | `IP_CP_LAST_VAR_DTTM` | DATETIME (Local) |  | The date and time the last care plan variance was documented. |
| 11 | `READY_QUT_SMOKING_C_NAME` | VARCHAR |  | This column is used to indicate whether patient is ready to quit smoking. |
| 12 | `COUNSELING_GIVEN_C_NAME` | VARCHAR |  | This column is used to indicate whether smoking counseling is given. |
| 13 | `COMMAUTO_SENDER_ID` | VARCHAR |  | The unique user ID of the sender of the automatically generated communications. |
| 14 | `COMMAUTO_SENDER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `BENEFIT_ID` | NUMERIC |  | The benefit record used to store discrete information about the patient's insurance benefits for this encounter. |
| 16 | `PREPAY_DUE_AMT` | NUMERIC |  | The amount of pre-payment that is due for this visit. |
| 17 | `PREPAY_AMT_FROM_C_NAME` | VARCHAR |  | The activity that set the pre-payment due amount. |
| 18 | `PREPAY_PAID_AMT` | NUMERIC |  | The pre-payment amount that has been collected for this visit. |
| 19 | `PREADMSN_TESTING_DT` | DATETIME |  | The preadmission testing date. |
| 20 | `SMK_CESS_USER_ID` | VARCHAR |  | The last user to modify the Smoking Cessation items for the encounter. |
| 21 | `SMK_CESS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `SMK_CESS_DTTM` | DATETIME (UTC) |  | Indicates whether Instant Smoking Cessation items were modified for an encounter. |
| 23 | `DO_NOT_BILL_INS_YN` | VARCHAR |  | Indicates if a visit is marked as Do Not Bill Insurance. |
| 24 | `SELF_PAY_VISIT_YN` | VARCHAR |  | Indicates whether a visit is self-pay. |
| 25 | `REFERRAL_TYPE_C_NAME` | VARCHAR | org | The means by which the patient learned about the organization. |
| 26 | `SCHOOL` | VARCHAR |  | The patient's school. |
| 27 | `COPAY_NUM_UNITS` | INTEGER |  | The number of units used to calculate the copay for this encounter. |
| 28 | `COPAY_AMT_PER_UNIT` | NUMERIC |  | The copay per each copay unit for this encounter. |
| 29 | `COPAY_LASTCALC_DT` | DATETIME |  | The date the copay was last calculated for this encounter. |
| 30 | `COPAY_OVERRIDDEN_YN` | VARCHAR |  | Indicates whether the user has overridden the copay amount for this encounter. |
| 31 | `OB_TOTAL_WT_GAIN` | NUMERIC |  | This column contains the patient's total weight gain in ounces as of the encounter if the patient had a weight documented on the encounter and a pregnancy episode with a pregravid weight linked to the encounter. |
| 32 | `MEDICAID_GROUP_NAME` | VARCHAR |  | Item to store the name of a group defined by a Medicaid program. |
| 33 | `STUDENT_STATUS_C_NAME` | VARCHAR | org | Tracks a patient's student status for a given encounter. |
| 34 | `MEDICAID_GROUP_ID` | VARCHAR |  | Item to store the identifier of a group defined by a Medicaid program. |
| 35 | `EXTERNAL_REF_ID` | VARCHAR |  | The reference ID from an external organization for the patient visit. |
| 36 | `OUTCOME_C_NAME` | VARCHAR | org | The clinical outcome of an encounter. The value of this item will then be used to determine the appropriate RTT/waiting status for the encounter. It is primarily applicable to the UK and Denmark. |
| 37 | `HSPC_NO_ADM_C_NAME` | VARCHAR | org | The Hospice Reason for Non-Admit category ID for the hospice episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

