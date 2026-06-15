# HH_EPSD_CARE_TEAM_HX

> This table contains the history of any edits made to care team member data.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DISCIPLINE_C_NAME` | VARCHAR | org | History of the disciplines of Care Team members. |
| 4 | `START_DATE` | DATETIME |  | History of the start date for Care Team members. |
| 5 | `END_DATE` | DATETIME |  | History of the end dates for Care Team members. |
| 6 | `VISITS_PER_WEEK_CNT` | VARCHAR |  | History for the number of visits per week for Care Team members. |
| 7 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `EDIT_USER_ID` | VARCHAR |  | History of the IDs of users who made edits to the Care Team |
| 9 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | History of the instant edits were made to the Care Team data. |
| 11 | `EDIT_LINE` | INTEGER |  | History of the line number of the Care Team member whose data was edited. This is the line number found in column LINE of HH_EPSD_CARETEAM |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

