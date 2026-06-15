# POC_INFO

> This table contains no-add single item information for the Plan of Care (POC) master file.

**Primary key:** `RECORD_ID`  
**Columns:** 37  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status, such as active or soft-deleted. |
| 3 | `POC_CREATED_IN_DTTM` | DATETIME (Local) |  | This item contains the instant at which the POC was created. |
| 4 | `POC_REFRESHED_DTTM` | DATETIME (Local) |  | This item contains the instant at which the POC was last refreshed with up-to-date patient info. |
| 5 | `POC_LAST_SAVED_DTTM` | DATETIME (Local) |  | This item contains the instant at which the POC was last saved with user-entered information. |
| 6 | `POC_COMPLETED_DTTM` | DATETIME (Local) |  | This item contains the instant at which the POC was filed and/or sent. |
| 7 | `PLAN_OF_CARE_C_NAME` | VARCHAR |  | This item contains the POC type. |
| 8 | `UPDATE_POC_ID` | NUMERIC |  | This item contains a pointer to the POC being updated. |
| 9 | `EPISODE_SEQ_NUM` | INTEGER |  | This item contains the parent POC sequence number. |
| 10 | `UPDATE_SEQ_NUM` | INTEGER |  | This item contains the child POC sequence number. |
| 11 | `EPISODE_ID` | NUMERIC | FK→ | This item contains the link to the episode in which the POC was created. |
| 12 | `CARE_PLAN_CSN` | NUMERIC |  | The contact serial number of the care plan contact that contains the care plan information pulled into the POC. |
| 13 | `CARE_PLAN_INFO_C_NAME` | VARCHAR |  | If the POC contains care plan visit information, problems, or both. |
| 14 | `POC_MEDS_CSN` | NUMERIC |  | The contact serial number of the patient contact that contains the medications list for the POC. |
| 15 | `RECORD_CREATION_DT` | DATETIME |  | This item stores the date the record was created. |
| 16 | `EPSD_ELECTION_DATE` | DATETIME |  | The date of hospice election. |
| 17 | `EPSD_EFFECTIVE_DATE` | DATETIME |  | The date the hospice agency began taking care of the patient. |
| 18 | `TRIAGE_CODE_C_NAME` | VARCHAR | org | The patient's triage code, as documented in the episode. |
| 19 | `POC_START_DT` | DATETIME |  | Start date for a hospice plan of care. The plan of care is effective until the next POC/POC update's start date. |
| 20 | `POC_END_DT` | DATETIME |  | Virtual item which returns the end date of a hospice plan of care. This is determined based on other plans of care (and, sometimes, the episode discharge date). Typically a hospice plan of care will end whenever a subsequent plan of care is created. A plan of care update will end when a subsequent plan of care update is created. |
| 21 | `POC_CODE_STATUS` | VARCHAR |  | The patient code status when the plan of care is completed. |
| 22 | `DISPLAY_NM` | VARCHAR |  | This item contains the display name for a plan of care. |
| 23 | `STAT_C_NAME` | VARCHAR |  | This item contains the current status of a plan of care. |
| 24 | `SPOC_WORKFLOW_C_NAME` | VARCHAR | org | This item contains the type for the current plan. This may be useful for classification and reporting upon different types of plans. |
| 25 | `SPOC_TYPE_C_NAME` | VARCHAR | org | Indicates the type of plan a POC represents within a given workflow |
| 26 | `PAT_ID` | VARCHAR | FK→ | This item contains the patient ID for whom the current plan has been created. |
| 27 | `SPOC_SIGNED_DATE` | DATETIME |  | The date the last required participant signed the plan. |
| 28 | `TEMPLATE_YN` | VARCHAR |  | This item is true if a plan is a template agreement. Template agreements are not agreements for any particular patient, but are used, temporarily, to contain information used to create multiple agreements which may be on different patients. |
| 29 | `TEMPLATE_POC_ID` | NUMERIC |  | This item links an agreement to the template agreement from which it was copied. |
| 30 | `POC_RATIFIED_INST_DTTM` | DATETIME (UTC) |  | Contains the instant at which the POC was ratified. |
| 31 | `POC_RATIFIED_YN` | VARCHAR |  | This item indicates if the agreement is ratified or not. A blank value indicates that no decision has been made. A value of 1 (true) indicates that the agreement is ratified. A value of 2 (false) indicates that a decision was made to not ratify the agreement. |
| 32 | `PLAN_UNDER_REVIEW_YN` | VARCHAR |  | Whether the hospice POC is under review. While under review the POC cannot be signed. |
| 33 | `CODE_STATUS_CMT` | VARCHAR |  | The patient code status comment when the plan of care is completed. |
| 34 | `HH_ASMNT_CSN_ID` | NUMERIC |  | The unique contact serial number of the assessment contact used to populate the home health Plan of Care. |
| 35 | `HH_CERT_PER_CSN_ID` | NUMERIC |  | The unique contact serial number of the encounter that created the certification period associated with the home health Plan of Care. |
| 36 | `POC_AUTO_CREATED_YN` | VARCHAR |  | Indicates whether the Plan of Care has been automatically created. 'Y' Indicates that this Plan of Care was automatically created. 'N' or NULL indicate that it was manually created. |
| 37 | `HH_POC_CONVERTED_YN` | VARCHAR |  | Indicates whether the home health Specialty Plan of Care record corresponds to an old plan and was created out of the conversion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

