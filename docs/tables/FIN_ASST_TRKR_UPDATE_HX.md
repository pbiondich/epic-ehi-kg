# FIN_ASST_TRKR_UPDATE_HX

> This table contains information related to the financial assistance tracker record's update history. Whenever any of the following details of a program tracker are changed or added, a row is added to this table. 1. Status 2. Decision date 3. Approval start date 4. Approval end date 5. Note 6. Source 7. Method 8. Medications.

**Primary key:** `FIN_ASST_TRACKER_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance program tracker record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant when the update was made. |
| 4 | `UPDATE_USER_ID` | VARCHAR |  | The unique ID of the user who made the update. |
| 5 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UPDATE_STATUS_C_NAME` | VARCHAR | org | The category ID of the program tracker status after the update was made. |
| 7 | `UPDATE_DECISION_DATE` | DATETIME |  | The decision date after the update was made. |
| 8 | `UPDATE_START_DATE` | DATETIME |  | The approval start date after the update was made. |
| 9 | `UPDATE_END_DATE` | DATETIME |  | The approval end date after the update was made. |
| 10 | `UPDATE_NOTE` | VARCHAR |  | The note added when the update was made. |
| 11 | `UPDATE_RESP_USER_ID` | VARCHAR |  | History of Responsible User (I FNT 58). |
| 12 | `UPDATE_RESP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `UPDATE_PROGRAM_SOURCE_C_NAME` | VARCHAR | org | History of the source specified for this program tracker after an update was made to the tracker. |
| 14 | `UPDATE_PROGRAM_METHOD_C_NAME` | VARCHAR | org | History of the method specified for this program tracker after an update was made to the tracker. |
| 15 | `UPDATE_NOTE_ID` | VARCHAR |  | ID of the note record that contains the comment entered as part of the update. |
| 16 | `REG_HX_EVENT_ID` | NUMERIC |  | Prelude history event containing more metadata about this entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

