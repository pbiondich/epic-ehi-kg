# HH_TRIAGE_CODE_HX

> This table contains audit history of the triage code for a patient during a home care episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRIAGE_CODE_C_NAME` | VARCHAR | org | Auditing history of the triage code for a patient during a home care episode. |
| 4 | `EDIT_USER_ID` | VARCHAR |  | Auditing history of the ID of the user who edited the triage code for a patient during a home care episode. |
| 5 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Auditing history of the instant at which edits were made to the triage code for a patient during a home care episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

