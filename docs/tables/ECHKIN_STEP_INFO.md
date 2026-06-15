# ECHKIN_STEP_INFO

> This table contains eCheck-In information for a specific appointment.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `INCLUDED_STEP_C_NAME` | VARCHAR |  | The step of the eCheck-In workflow. |
| 7 | `ECHKIN_STEP_STAT_C_NAME` | VARCHAR |  | The status of the specific step mentioned in the eCheck-In workflow. |
| 8 | `STEP_COMPLETED_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant (in UTC) the step was completed in the eCheck-In workflow |
| 9 | `MYPT_ID` | VARCHAR | shared | Stores the MyChart user ID that did the eCheck-In step. |
| 10 | `STEP_ACTION_C_NAME` | VARCHAR |  | The category ID for the action taken on an eCheck-In step. |
| 11 | `STEP_COMP_ECHKIN_PHASE_C_NAME` | VARCHAR |  | The eCheck-In phase when this eCheck-In step was marked as completed. |
| 12 | `ECHKIN_PREARRIVAL_STAT_C_NAME` | VARCHAR |  | This defines the status of a step during the pre-arrival phase of the just-in-time eCheck-In workflow. This tracks whether a step was shown to a patient and completed before arriving for their visit. |
| 13 | `ECHKIN_POSTARRIVAL_STAT_C_NAME` | VARCHAR |  | This defines the status of a step during the post-arrival phase of the just-in-time eCheck-In workflow. This tracks whether a step was shown to a patient and completed after arriving for their visit, such as while sitting in the waiting room or the exam room. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

