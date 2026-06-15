# PAT_ENC_MSP

> This table contains the Medicare Secondary Payor Information from the Patient (EPT) master file. The encounters with MSP information are the only ones extracted into this table.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 33  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `SUPPLIED_BY` | VARCHAR |  | The name of the person who supplied the information for the Medicare Secondary Payor questionnaire (MSPQ). |
| 4 | `RELATION_PAT_C_NAME` | VARCHAR | org | The category ID for the relationship to the patient of the person who supplied the information for the MSPQ. |
| 5 | `PAT_RETIRE_DATE` | DATETIME |  | The date of retirement for the patient. |
| 6 | `MSP_USER` | VARCHAR |  | The name of the user who last accessed the Medicare Secondary Payor Questionnaire (MSPQ) for this contact. |
| 7 | `LAST_ACCESS_DATE` | DATETIME |  | The date and time that the Medicare Secondary Payor Questionnaire (MSPQ) for this contact was last accessed. |
| 8 | `NA_HEALTH_BEN_YN_NAME` | VARCHAR |  | Indicates whether the patient is eligible for Native American healthcare benefits. Y indicates that the patient is eligible for Native American healthcare benefits. N indicates that the patient is not eligible for Native American healthcare benefits. A null value indicates this item was not filled out. |
| 9 | `NA_RESERVATION_C_NAME` | VARCHAR | org | The Native American reservation category ID for the Medicare Secondary Payor questionnaire (MSPQ). |
| 10 | `IS_ACCIDENT_C_NAME` | VARCHAR | org | Indicates whether the patient has been in an accident. |
| 11 | `IS_CVG_VET_BEN_C_NAME` | VARCHAR | org | Indicates whether the Department of Veterans Affairs (DVA) authorized and agreed to pay for care at this facility or the patient would like the DVA to be contacted for such authorization. |
| 12 | `IS_OVER_100_EMP_C_NAME` | VARCHAR | org | Indicates whether the patient's Group Health Plan (GHP) is sponsored by an employer with 100 or more employees. |
| 13 | `IS_NON_ERSD_C_NAME` | VARCHAR | org | Indicates whether the patient is entitled to Medicare because of disability other than End Stage Renal Disease. |
| 14 | `IS_BLACK_LUNG_C_NAME` | VARCHAR | org | Indicates whether the patient is entitled to benefits under the Black Lung Program. |
| 15 | `IS_CVD_EGHP_C_NAME` | VARCHAR |  | If the patient has employer group health plan (EGHP) coverage based on own or family member's current or former employment. |
| 16 | `IS_END_STAGE_RNL_C_NAME` | VARCHAR | org | Indicates whether the patient is entitled to Medicare because of End Stage Renal Disease. |
| 17 | `IS_NONWORK_ACC_C_NAME` | VARCHAR |  | Indicates whether the illness or injury is the result of a non work-related accident. |
| 18 | `IS_WORKERS_COMP_C_NAME` | VARCHAR |  | Indicates whether the illness or injury is covered by workers' compensation. |
| 19 | `IS_OTHER_EMPLYD_C_NAME` | VARCHAR |  | Indicates whether the spouse or other family member is currently employed. |
| 20 | `IS_PAT_EMPLYD_C_NAME` | VARCHAR |  | Indicates whether the patient is currently employed. |
| 21 | `IS_PAT_SPSE_RET_C_NAME` | VARCHAR |  | Indicates whether the patient or spouse is retired. |
| 22 | `IS_PHS_C_NAME` | VARCHAR |  | Indicates whether the services are covered by a Public Health Service or Research Program. |
| 23 | `IS_VET_BEN_C_NAME` | VARCHAR | org | Indicates whether patient is entitled to benefits under the Department of Veterans Affairs. |
| 24 | `IS_OVER_20_EMP_C` | VARCHAR |  | Indicates whether the patient's Group Health Plan (GHP) is sponsored by an employer with 20 or more employees. |
| 25 | `MSP_COMPLTN_USER_ID` | VARCHAR |  | The unique ID of the user who last completed the Medicare Secondary Payor Questionnaire (MSPQ) for this contact. |
| 26 | `MSP_COMPLTN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `MSP_COMPLETE_DATE` | DATETIME |  | The date when the Medicare Secondary Payor Questionnaire (MSPQ) was last opened and completed. |
| 28 | `MSP_STATUS_C_NAME` | VARCHAR | org | The Completion Status category number for the Medicare Secondary Payor Questionnaire (MSPQ). |
| 29 | `IS_AGE_ENTITLED_YN` | VARCHAR |  | Indicates whether the patient is entitled to benefits based on age. |
| 30 | `IS_PRVSN_APPLY_YN` | VARCHAR |  | Indicates whether the patient is entitled to benefits based on the working aged or disability provision. |
| 31 | `IS_DUAL_ENTITLED_YN` | VARCHAR |  | Indicates whether the patient is entitled to Medicare based on a combination of either ESRD and age, or ESRD and disability. |
| 32 | `SOURCE_ORGANIZATION_ID` | NUMERIC |  | Holds the DXO of the Epic instance that this MSP info came from. |
| 33 | `SOURCE_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

