# CMGMT_EPISODE_HX

> The history tracks changes made to the case episode for auditing purposes.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | Stores the action taken by the user. |
| 4 | `ACTION_USER_ID` | VARCHAR |  | Stores the user that updated the case episode. |
| 5 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ASSOC_VALUE_RAW_DATA` | VARCHAR |  | Stores the new value or record associated with the action taken on the case episode. |
| 7 | `REMOVING_USER_ID` | VARCHAR |  | Stores the user that removed the associated value (I HSB 18440) from the case episode. |
| 8 | `REMOVING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | Stores the date and time (UTC) on which the history action was taken. |
| 10 | `REMOVED_UTC_DTTM` | DATETIME (UTC) |  | Store the date and time (UTC) on which the associated value (I HSB 18440) was removed from the case episode. |
| 11 | `ACTION_LOCAL_DTTM` | DATETIME (Local) |  | Stores the date and time (system default time) on which the history action was taken. |
| 12 | `REMOVED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the date and time (system default time) on which the associated value (I HSB 18440) was removed from the case episode. |
| 13 | `CASE_TEAM_LINE` | INTEGER |  | Store a line from the case team, if the history value (I HSB 18440) is associated with the case team. |
| 14 | `ACTION_ENC_CSN_ID` | NUMERIC | FK→ | Case Management History Item - The encounter that set the value on the case episode, if the history value (I HSB 18440) is associated with an encounter. |
| 15 | `REMOVING_ENC_CSN_ID` | NUMERIC | FK→ | Case Management History Item - The encounter that removed the value on the case episode, if the history value (I HSB 18440) is associated with an encounter. |
| 16 | `ASSOC_CMGMT_TYPE_C` | INTEGER |  | When the action taken by the user is 1-Update Case Type, this column holds the associated case type value. This column is derived from the Assoc_Value_Raw_Data column. |
| 17 | `ASSOC_CMGMT_STATUS_C` | INTEGER |  | When the action taken by the user is 2-Update Case Status, this column holds the associated case status value. This column is derived from the Assoc_Value_Raw_Data column. |
| 18 | `ASSOC_CMGMT_ENROLLING_STEP_C` | INTEGER |  | When the action taken by the user is 3-Update Enrolling Step, this column holds the associated enrolling step value. This column is derived from the Assoc_Value_Raw_Data column. |
| 19 | `ASSOC_CMGMT_CLOSED_REASON_C` | INTEGER |  | When the action taken by the user is 5-Update Closed Reason, this column holds the associated closed reason value. This column is derived from the Assoc_Value_Raw_Data column. |
| 20 | `ASSOC_REVIEW_DUE_DATE` | DATETIME |  | When the action taken by the user is 6-Update Review Due Date, this column holds the associated review due date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 21 | `ASSOC_REV_FREQ_UNIT_C` | INTEGER |  | When the action taken by the user is 7-Update Review Frequency Unit, this column holds the associated review frequency unit value. This column is derived from the Assoc_Value_Raw_Data column. |
| 22 | `ASSOC_REV_FREQ_LENGTH` | INTEGER |  | When the action taken by the user is 8-Update Review Frequency Length, this column holds the associated review frequency length value. This column is derived from the Assoc_Value_Raw_Data column. |
| 23 | `ASSOC_CMGMT_SENSITIVITY_C` | INTEGER |  | When the action taken by the user is 9-Update Sensitivity, this column holds the associated sensitivity value. This column is derived from the Assoc_Value_Raw_Data column. |
| 24 | `ASSOC_CMGMT_TRACKING_STATUS_C` | INTEGER |  | When the action taken by the user is 12-Update Tracking Status, this column holds the associated tracking status value. This column is derived from the Assoc_Value_Raw_Data column. |
| 25 | `ASSOC_CMGMT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 26 | `ASSOC_CMGMT_END_DATE` | DATETIME |  | When the action taken by the user is 14-Update End Date, this column holds the associated end date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 27 | `ASSOC_CMGMT_START_DATE` | DATETIME |  | When the action taken by the user is 10-Update Start Date, this column holds the associated start date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 28 | `ASSOC_CMGMT_DECLINE_REASON_C` | INTEGER |  | When the action taken by the user is 13-Update Declined Reason, this column holds the associated declined reason value. This column is derived from the Assoc_Value_Raw_Data column. |
| 29 | `ASSOC_CMGMT_MED_PRBLM_LIST_ID` | NUMERIC |  | When the action taken by the user is 15-Update Linked Medications, this column holds the associated medication ID value. This column is derived from the Assoc_Value_Raw_Data column. |
| 30 | `ASSOC_CMGMT_SSP_CHANGED_LINE` | INTEGER |  | The line number in CMGMT_SUPPORT_TYPE_HX that contains a copy of the previous support & services provided. The updated support and services provided will be in the next line of CMGMT_SUPPORT_TYPE_HX, or in I HSB 64050 if there are no more lines. |
| 31 | `ASSOC_CMGMT_REFERRAL_ID` | NUMERIC |  | When the action taken by the user is 19-Link Referral, this column holds the associated referral. |
| 32 | `ASSOC_CMGMT_CLAIM_ID` | NUMERIC |  | When the action taken by the user is 20-Link Claim, this column holds the associated claim. |
| 33 | `ASSOC_CMGMT_EFF_DATE` | DATETIME |  | When the action taken by the user is 21 - Update Effective Date, this column holds the associated effective date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 34 | `ASSOC_CMGMT_TERMINATION_DATE` | DATETIME |  | When the action taken by the user is 22 - Update Termination Date, this column holds the associated termination date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 35 | `ASSOC_CMGMT_TRTMNT_TEAM_REL_C` | VARCHAR |  | When the action taken by the user is 23 - Update Relationship, this column holds the associated case team relationship value. This column is derived from the Assoc_Value_Raw_Data column. |
| 36 | `ASSOC_CMGMT_IS_PRIMARY_YN` | VARCHAR |  | When the action taken by the user is 24 - Update Primary, this column holds the associated Primary? value. This column is derived from the Assoc_Value_Raw_Data column. |
| 37 | `ASSOC_CMGMT_PROBLEM_LIST_ID` | NUMERIC |  | When the action taken by the user is 25-Update Linked Problems, this column holds the associated problem ID value. This column is derived from the Assoc_Value_Raw_Data column. |
| 38 | `ASSOC_CMGMT_MED_INFO_LINE` | INTEGER |  | The line number in EPSD_ASSOC_MEDS_HX that contains a copy of the previous associated medications information provided. The updated associated medications information provided will be in the next line of EPSD_ASSOC_MEDS_HX, or in I HSB 48004 and 48007-48009 if there are no more lines. |
| 39 | `ASSOC_CMGMT_COMPLEXITY_C` | INTEGER |  | When the action taken by the user is 27-Update Complexity, this column holds the associated complexity value. This column is derrived from the Assoc_Value_Raw_Data column. |
| 40 | `ASSOC_RXMA_EPISODE_ID` | NUMERIC |  | When the action taken by the user is 1200-Update Medication Access Linked Clinical Episode, this column holds the associated Medication Access linked clinical episode value. This column is derived from the Assoc_Value_Raw_Data column. |
| 41 | `ASSOC_RXMA_CLS_C` | INTEGER |  | When the action taken by the user is 1201-Update Medication Access Linked Class, this column holds the associated Medication Access linked class value. This column is derived from the Assoc_Value_Raw_Data column. |
| 42 | `ASSOC_RXMA_BLOCK_DEF_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 43 | `ASSOC_RXMA_DCN_DATE` | DATETIME |  | When the action taken by the user is 1203-Update Medication Access Decision Due Date, this column holds the associated Medication Access decision due date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 44 | `ASSOC_RXMA_TX_START_DATE` | DATETIME |  | When the action taken by the user is 1204-Update Medication Access Treatment Start Date, this column holds the associated Medication Access treatment start date value. This column is derived from the Assoc_Value_Raw_Data column. |
| 45 | `ASSOC_RXMA_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 46 | `ASSOC_RXMA_REFERRAL_ID` | NUMERIC |  | When the action taken by the user is 1206-Update Medication Access Linked Authorization, this column holds the associated Medication Access linked authorization value. This column is derived from the Assoc_Value_Raw_Data column. |
| 47 | `ASSOC_RXMA_SOC_INFO_LINE` | INTEGER |  | The line number in RXMA_SITE_OF_CARE_HX that contains a copy of the previous site of care information provided. The updated site of careinformation provided will be in the next line of RXMA_SITE_OF_CARE_HX, or in I HSB 48830-48836 if there are no more lines. |
| 48 | `UPDATE_METHOD_C_NAME` | NUMERIC |  | Case Management History Item - This item stores the method of the corresponding history action. |
| 49 | `ASSOC_RXMA_VALID_THRU_DATE` | DATETIME |  | When the action taken by the user is 1208-Update Medication Access Valid Through Date, this column holds the associated Medication Access valid through date value. This column is derived from the Assoc_Value_Raw_Data column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACTION_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `REMOVING_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

