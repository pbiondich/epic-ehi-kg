# FRM_IMP_SAFETY

> This table stores implant safety-related information for screening forms, including the implants' IDs, MRI safety status, safety comments, last editing user, and last editing time.

**Primary key:** `SCREENING_FORM_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCREENING_FORM_ID` | NUMERIC | PK | The unique identifier for the screening form record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMPLANT_ID` | VARCHAR | shared | The unique ID of the patient's implant. |
| 4 | `IMPLANT_SAFETY_STATUS_C_NAME` | VARCHAR | org | The implant safety status category ID for the timeout record associated with the patient. |
| 5 | `IMPLANT_SAFETY_CMT_NOTE_ID` | VARCHAR |  | The unique ID of the implant safety status comments (HNO). |
| 6 | `IMPLANT_SAFETY_AUD_USER_ID` | VARCHAR |  | Tracks the user who last edited the implant safety status. |
| 7 | `IMPLANT_SAFETY_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `IMPLANT_SAFETY_AUD_DTTM` | DATETIME (UTC) |  | Tracks the last time a user updated the implant safety status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

