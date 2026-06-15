# HH_EPSD_CARE_TEAM_INFO_HX

> This table stores the audit trail information for the editing of Care Team information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TEAM_ASSIGNMENT_C_NAME` | VARCHAR | org | The audit trail of care team assignments populating column Team_ASSIGNMENT_C on table HH_EPSD_INFO |
| 4 | `EDIT_USER_ID` | VARCHAR |  | The audit trail of user IDs that edited the column TEAM_ASSIGNMENT_C on table HH_EPSD_INFO |
| 5 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | The audit trail of the instant changes were made to column TEAM_ASSIGNMENT_C on table HH_EPSD_INFO. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

