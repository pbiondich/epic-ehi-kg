# SOCIAL_CARE_TRACKER

> This table contains information about Social Care decisions, which are stored as tracker records.

**Primary key:** `FIN_ASST_TRACKER_ID`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier for the decision record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category ID for the decision. |
| 3 | `FIN_ASST_PROGRAM_ID` | NUMERIC | FK→ | The unique ID of the financial assistance program for the decision. |
| 4 | `FIN_ASST_PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |
| 5 | `FIN_ASST_CASE_ID` | NUMERIC | FK→ | The unique ID of the financial assistance case associated with the decision. |
| 6 | `STATUS_C_NAME` | VARCHAR | org | The status category ID for the decision. |
| 7 | `START_DATE` | DATETIME |  | The date when the decision was approved. |
| 8 | `END_DATE` | DATETIME |  | The end date for the decision. |
| 9 | `DECISION_VALID_C_NAME` | VARCHAR |  | The validity type category ID for the decision. |
| 10 | `DECISION_NOTE_ID` | VARCHAR |  | The unique ID of the note for the decision. |
| 11 | `REC_CREATION_DATE` | DATETIME |  | The date when the decision was created. |
| 12 | `INST_OF_UPDATE_1_DTTM` | DATETIME (Local) |  | Stores the instant the record was last locked/unlocked. |
| 13 | `DECISION_NEGATIVE_YN` | VARCHAR |  | Indicates whether the decision tracker is negative, which denies application for support. |
| 14 | `PARENT_TRACKER_ID` | NUMERIC |  | The unique ID of the service decision a related decision is linked to. |
| 15 | `RESPONSIBLE_USER_ID` | VARCHAR |  | The unique ID for the responsible user for the decision. |
| 16 | `RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `DECISION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 18 | `DECISION_COST_CENTER` | VARCHAR |  | The cost center string generated for the decision. |
| 19 | `REG_ENCOUNTER_CSN_ID` | NUMERIC |  | The unique contact serial number of the special encounter that stores registration information related to the service decision. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |
| `FIN_ASST_PROGRAM_ID` | [FIN_ASST_PROGRAM](FIN_ASST_PROGRAM.md) | sole_pk | high |
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

