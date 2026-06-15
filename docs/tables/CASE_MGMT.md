# CASE_MGMT

> The CASE_MGMT table is the master table for reporting on case data. This table includes foreign keys to other tables containing information about the case, such as employer, coverage, and diagnosis information.

**Primary key:** `CASE_ID`  
**Columns:** 73  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID assigned to the case record. |
| 2 | `CASE_NAME` | VARCHAR |  | The name of the case. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient linked to the case record. |
| 4 | `CASE_TYPE_C_NAME` | VARCHAR | org | The category value assigned to classify the case record and determine default case priorities. |
| 5 | `CASE_STATUS_C_NAME` | VARCHAR |  | The category value associated with the status of the case. |
| 6 | `PRIORITY_ID` | NUMERIC | FK→ | The unique ID of the priority record assigned to the case. |
| 7 | `PRIORITY_ID_PRIORITY_NAME` | VARCHAR |  | The name of the priority record. |
| 8 | `MANAGER_USER_ID` | VARCHAR |  | The unique ID of the user who is assigned this case. |
| 9 | `MANAGER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ROSTER_ID` | VARCHAR | FK→ | The unique ID of the roster to which this case belongs. |
| 11 | `ROSTER_ID_ROSTER_NAME` | VARCHAR |  | The name of the roster. |
| 12 | `RAW_BD_ADJST` | NUMERIC |  | The manual adjustment to the case’s total number of raw days. |
| 13 | `CONV_BD_ADJST` | NUMERIC |  | The manual adjustment to the case’s total number of converted days. |
| 14 | `RAW_RFL_BD_TOT` | NUMERIC |  | The sum of raw bed days for all the referrals linked to the case. |
| 15 | `CONV_RFL_BD_TOT` | NUMERIC |  | The sum of converted bed days for all the referrals linked to the case. |
| 16 | `CASE_RAW_TOTAL` | NUMERIC |  | The sum of raw bed days for all the referrals linked to the case and any adjustments entered for raw days. |
| 17 | `TOTAL_COST_OF_CASE` | NUMERIC |  | The dollar amount representing the sum of the claims, charges and adjustments linked to this case. |
| 18 | `DATE_REPORTED` | DATETIME |  | The date the accident was reported. |
| 19 | `DAYS_OF_TREATMENT` | NUMERIC |  | The number of days of treatment that the patient underwent as a result of the injury. |
| 20 | `HOURS_ON_CASE` | NUMERIC |  | The hours spent by the cost tracking manager on the case. |
| 21 | `CARRIER_ID` | VARCHAR | FK→ | The unique ID of the carrier record linked to this case record. |
| 22 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 23 | `EMPLOYER_ID` | VARCHAR | FK→ | This is the unique ID of the employer record linked to this case record if Patient Employer Linked Free Text or Linked to Employer(I EAF 6410) is set to 1. This is free text if I EAF 6410 is set to 2. |
| 24 | `EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 25 | `ACCIDENT_TYPE_C_NAME` | VARCHAR | org | The category value assigned to the case record to explain the type of accident that resulted in the creation of this case. |
| 26 | `INJURY_TYPE_C_NAME` | VARCHAR | org | The category value assigned to the case record to explain the type of injury arising out of the accident. |
| 27 | `INJURY_DATE` | DATETIME |  | The date the patient was injured. |
| 28 | `TREATMENT_DATE` | DATETIME |  | The date the patient started treatment for the injury. |
| 29 | `WORK_DAYS_MISSED` | FLOAT |  | The number of days of work missed by the patient. |
| 30 | `DISCHARGE_LOCATION` | VARCHAR |  | The free text describing the location from which the patient is released after treatment. |
| 31 | `CLASSIFIER_ID` | VARCHAR | FK→ | The unique ID of the classifier record that triggered the case creation message for this case. |
| 32 | `CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 33 | `TRG_DIAGNOSIS_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 34 | `TRG_DIAG_COMP_ID` | VARCHAR |  | The unique ID of the diagnosis component record (if any) that triggered the case creation message for this case. |
| 35 | `TRG_DIAG_COMP_ID_COMPONENT_NAME` | VARCHAR |  | The name of the component |
| 36 | `TRG_PROCEDURE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 37 | `TRG_PROC_COMP_ID` | VARCHAR |  | The unique ID of the procedure component (if any) that triggered the case creation message for this case. |
| 38 | `TRG_PROC_COMP_ID_COMPONENT_NAME` | VARCHAR |  | The name of the component |
| 39 | `TRG_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 40 | `TRG_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 41 | `LOB_ID` | VARCHAR | FK→ | The case line of business. |
| 42 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 43 | `TRG_MIN_AGE` | INTEGER |  | The minimum age threshold set in the case classifier that generated the case create message for this case. |
| 44 | `TRG_MAX_AGE` | INTEGER |  | The maximum age threshold set in the case management classifier that generated the case create message for this case. |
| 45 | `TRG_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 46 | `TRG_SPEC_C_NAME` | VARCHAR | org | The specialty of the provider (if any) that triggered the case creation message for this case. |
| 47 | `TRG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 48 | `TRG_LOB_ID` | VARCHAR |  | The unique ID of the Line of Business (if any) that triggered the case creation message for this case. |
| 49 | `TRG_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 50 | `TRG_PRIM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 51 | `ESCALATION_DATE` | DATETIME |  | The escalation date of the case. |
| 52 | `EOW_MESSAGE_ID` | VARCHAR |  | The In Basket message ID for the case. |
| 53 | `EOW_STATUS_C_NAME` | VARCHAR |  | The In Basket message status for the case. |
| 54 | `CASE_CONV_TOTAL` | INTEGER |  | Case level converted bed days total. |
| 55 | `TRG_REVCODE_ID` | NUMERIC |  | Displays the revenue code matched in a case classifier, resulting in a case create In Basket message. The associated case was created from this In Basket message. |
| 56 | `TRG_REVCODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 57 | `TRG_REV_COMP_ID` | VARCHAR |  | Displays the revenue code component matched in a case classifier, resulting in a case created In Basket message. The associated case was created from this In Basket message. |
| 58 | `TRG_REV_COMP_ID_COMPONENT_NAME` | VARCHAR |  | The name of the component |
| 59 | `TRG_COMPON_GRP_ID` | VARCHAR |  | Specifies the trigger component group. |
| 60 | `TRG_COMPON_GRP_ID_COMPONENT_GRP_NAME` | VARCHAR |  | The name of the component group |
| 61 | `TRG_ICD_PX_ID` | VARCHAR |  | The unique ID of the ICD Procedure Code (if any) that triggered the case creation message for this case. |
| 62 | `TRG_ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 63 | `TRG_APPLY_TO_C_NAME` | VARCHAR |  | Specify whether this case should apply to referrals, AP claims or both. The default (blank value) is referrals. |
| 64 | `TRG_RFL_TYPE_C_NAME` | VARCHAR | org | The type of referral (if any) that triggered the case creation message for this case. |
| 65 | `TRG_DRG_ID` | VARCHAR |  | The unique ID of the Diagnosis Related Group (DRG) code (if any) that triggered the case creation message for this case. |
| 66 | `TRG_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 67 | `TRG_DRG_COMP_ID` | VARCHAR |  | The unique ID of the Diagnosis Related Group (DRG) component (if any) that triggered the case creation message for this case. |
| 68 | `TRG_DRG_COMP_ID_COMPONENT_NAME` | VARCHAR |  | The name of the component |
| 69 | `TRG_CVG_PRIM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 70 | `TIME_OF_TREATMENT_TM` | DATETIME (Local) |  | Holds the time of treatment for accident information. |
| 71 | `WORK_COMP_CLAIM_NUM` | VARCHAR |  | Workers' compensation claim number associated with the case. |
| 72 | `WORK_COMP_CARRIER` | VARCHAR |  | Workers' compensation carrier associated with the case. |
| 73 | `TPA_ADMINISTRATOR` | VARCHAR |  | Name of the third party administrator. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `CLASSIFIER_ID` | [CLASSIFIER](CLASSIFIER.md) | sole_pk | high |
| `EMPLOYER_ID` | [CLARITY_EEP](CLARITY_EEP.md) | sole_pk | high |
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PRIORITY_ID` | [CASE_PRIORITY](CASE_PRIORITY.md) | sole_pk | high |
| `ROSTER_ID` | [CASE_ROSTER](CASE_ROSTER.md) | sole_pk | high |

