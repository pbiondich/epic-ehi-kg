# FRM_STATUS

> This table stores status and update information for screening forms, including form status and last editing user and time.

**Primary key:** `SCREENING_FORM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCREENING_FORM_ID` | NUMERIC | PK | The unique identifier for the screening form record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FRM_STATUS_C_NAME` | VARCHAR |  | The screening form status category ID for the screening form. |
| 4 | `STATUS_AUD_USER_ID` | VARCHAR |  | The users who updated or edited the screening form. |
| 5 | `STATUS_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `STATUS_AUD_DTTM` | DATETIME (UTC) |  | The times when the screening form was updated or edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

