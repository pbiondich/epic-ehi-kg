# PAT_ADDENDUM_INFO

> This table contains the encounter addendum information from the Addendum Added Date (I EPT 18123) and Addendum Added User (I EPT 18129) items.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LINE` | INTEGER | PK | The line count for the items. |
| 5 | `ADDENDUM_DATE_TIME` | DATETIME (Local) |  | The date and time when the addendum of the patient encounter is created. |
| 6 | `ADDENDUM_USER_ID` | VARCHAR |  | The unique ID of the system user who has created the addendum for the patient encounter. |
| 7 | `ADDENDUM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ADDENDUM_STARTED_UTC_DTTM` | DATETIME (UTC) |  | This is the UTC instant when an addendum was started. If blank, then the Addendum Finished Date and Addendum Finished Time (ADDENDUM_DATE_TIME) is the started instant as well as the signed instant. |
| 9 | `ADDENDUM_STARTED_USER_ID` | VARCHAR |  | The unique user identifier that started the addendum. If blank, then the Addendum Finished User (ADDENDUM_USER_ID) was the user that started the addendum as well as signed it. |
| 10 | `ADDENDUM_STARTED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `SOURCE_WORKFLOW_C_NAME` | VARCHAR |  | This is the current platform that is allowed to edit the open addendum. This is only set for open addenda started on Rover. |
| 12 | `ADDENDUM_OPEN_YN` | VARCHAR |  | Stores whether the addendum is open and has not yet been signed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

