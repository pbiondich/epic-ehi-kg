# PAT_CARE_REG

> This table contains data for Patient Care Registration. Multiple rows may appear for each registration. Each row represents the data for one registration as it was added, deleted, or modified by a user at a particular point in time.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ROW_IDENTIFIER` | VARCHAR |  | The row identifier is used to group current data and audit trail data that are related to the same Patient Care Registration. In this table, multiple rows may appear with the same row identifier. Each row represents an edit that was made to the particular registration. The most current set of data for the registration can be found by looking at the most recent date and time in the EDIT_DATETIME column. |
| 4 | `USER_ID` | VARCHAR | FK→ | This item holds the User ID of the user who made the change. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `EDIT_DATETIME` | DATETIME (UTC) |  | This item holds the date and time (in UTC) when the change was made. |
| 7 | `TYPE_C_NAME` | VARCHAR | org | The Patient Care Registration Type category ID for the registration. |
| 8 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `START_DATE` | DATETIME |  | The start date on which the registration became effective. |
| 10 | `END_DATE` | DATETIME |  | The end date, after which the registration is no longer effective. |
| 11 | `IS_DELETED_YN` | VARCHAR |  | Y indicates that the user deleted a registration that was made in error. |
| 12 | `COMMENT` | VARCHAR |  | User-entered comments about a registration. |
| 13 | `ADMSN_NOTIF_YN` | VARCHAR |  | Yes indicates that the organization wishes to receive a notification upon the patient's admission. |
| 14 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | An externally assigned identifier for a patient care organization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

