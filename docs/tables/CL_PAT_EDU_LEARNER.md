# CL_PAT_EDU_LEARNER

> Enterprise reporting table for Contact specific Learner items in Patient education Record.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique ID for the patient education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line count for contact specific learner items in the patient education record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date for contact specific learner items in patient education record.. Store in external format. |
| 5 | `LEARNER_KEY` | VARCHAR |  | The key for contact specific learner items in patient education record. |
| 6 | `LEARNER_C_NAME` | VARCHAR | org | The learner category for contact specific learner items in patient education record. |
| 7 | `READINESS_C_NAME` | VARCHAR | org | The learner readiness category for contact specific learner items in patient education record. |
| 8 | `TEACHING_METHOD` | VARCHAR |  | The method of teaching for contact specific learner items in patient education record. |
| 9 | `RESPONSE` | VARCHAR |  | The learner response for contact specific learner items in patient education record. |
| 10 | `TAUGHT_BY_USER_ID` | VARCHAR |  | The teaching user ID for contact specific learner items in patient education record. It is stored in internal ID format and is linked to the user master file. |
| 11 | `TAUGHT_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `TAUGHT_AT_INS` | DATETIME (Local) |  | Date/Time stamp for the instance of teaching for contact specific learner items in patient education record. |
| 13 | `STATUS_C_NAME` | VARCHAR |  | The status category for contact specific learner items in patient education record. |
| 14 | `ENTER_BY_USER_ID` | VARCHAR |  | User ID of the user who added the point associated with the row of learning. |
| 15 | `ENTER_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `ENTER_AT_INS` | DATETIME (Local) |  | The data entry instant for contact specific learner items in patient education record. |
| 17 | `LEARNER_COMMENT` | VARCHAR |  | The learner's comment- contact specific. |
| 18 | `DELETED_BY_USER_ID` | VARCHAR |  | The ID number of the user who deleted the contact specific learner items in the patient education record. |
| 19 | `DELETED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `DELETED_AT_INS` | DATETIME (Local) |  | The instant of deletion for contact specific learner items in patient education record. |
| 21 | `TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 22 | `TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 23 | `POINTS_IED_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 24 | `MY_POINTS_HNO_ID` | VARCHAR |  | The first part of the unique ID of the patient education My Point record that is associated with this row of documentation. My Point is a patient education point created on the fly and does not have an education (IED) record associated with it. Note that this column is only populated for My Point records. This column is frequently used (along with MY_POINTS_HNO_DAT) to link to tables such as CL_PAT_EDU_POINT (via MY_POINT_HNO_ID) and CL_PATEDU_CNTCT_PT (via CNT_MYPOINT_HNO_ID). |
| 25 | `MY_POINTS_HNO_DAT` | VARCHAR |  | The second part of the unique ID of the patient education My Point record that is associated with this row of documentation. My Point is a patient education point created on the fly and does not have an education (IED) record associated with it. Note that this column is only populated for My Point records. This column is frequently used (along with MY_POINTS_HNO_ID) to link to tables such as CL_PAT_EDU_POINT (via MY_POINT_HNO_DAT) and CL_PATEDU_CNTCT_PT (via CNT_MYPOINT_HNO_DA). |
| 26 | `LRNR_FIRST_DOSE_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 27 | `TITLE_CONTACT_DATE_REAL` | INTEGER |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. The contact date will be for the title education row that was documented on. This can be used along with the TITLE_ID column to join with tables such as IP_EDU_OT_DATA in order to retrieve information for a specific title contact. |
| 28 | `TOPIC_CONTACT_DATE_REAL` | INTEGER |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. The contact date will be for the topic education row that was documented on. This can be used along with the TOPIC_ID column to join with tables such as IP_EDU_OT_DATA in order to retrieve information for a specific topic contact. |
| 29 | `POINT_CONTACT_DATE_REAL` | INTEGER |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. The contact date will be for the point education row that was documented on. This can be used along with the POINTS_IED_ID column to join with tables such as IP_EDU_OT_DATA in order to retrieve information for a specific point contact. |
| 30 | `CURRENT_ENC_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 31 | `ORIGINATING_SRC_MODE_C_NAME` | VARCHAR |  | The modality which started this learner documentation. Supported modalities: Manual - Learner documentation through traditional means (the education activity, education activity in rover) Ambient - The documentation started as an ambient recording MyChart - The learner initiated the documentation in MyChart Interface - The education documentation orginated from a third party interface |
| 32 | `FILING_WKFL_C_NAME` | VARCHAR |  | Tracks the workflow that was used to file learner documentation. |
| 33 | `WKFL_SESSION_ID` | NUMERIC |  | When suggested from an Ambient Voice Recognition Session this contains the session ID. |
| 34 | `WKFL_SESSION_CONTACT_DATE_REAL` | NUMERIC |  | When suggested from an Ambient Voice Recognition Session this contains the session DAT. |
| 35 | `WKFL_SESSION_LINE` | INTEGER |  | When suggested from an Ambient Voice Recognition Session this contains the session line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

