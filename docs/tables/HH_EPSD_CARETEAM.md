# HH_EPSD_CARETEAM

> This table contains Home Health episode-level care team information. It stores information entered by a user in the care team table on the Care Team form of Home Health Intake.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CARE_TM_DSCPLN_C_NAME` | VARCHAR | org | Discipline category list selection for the care team member. Links to category table ZC_DISCIPLINE. |
| 4 | `CARE_TEAM_START_DT` | DATETIME |  | Start date for the care team member. |
| 5 | `CARE_TEAM_END_DT` | DATETIME |  | End date for the care team member. |
| 6 | `CARE_TEAM_VISIT` | VARCHAR |  | This column stores the user entered number of visits per week for the care team member. |
| 7 | `CARE_TEAM_USER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

