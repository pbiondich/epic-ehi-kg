# PATHWAY_STATUS

> This table displays the status of the pathway (active, completed, or discontinued).

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique ID of the treatment plans record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STATUS_C_NAME` | VARCHAR | org | This is the pathway status which can be Active, Completed or Discontinued. |
| 4 | `UPDATE_BY_USER_ID` | VARCHAR |  | The user who updated the pathway status. |
| 5 | `UPDATE_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UPDATE_AT_DATETIME` | DATETIME (Local) |  | Stores the date and time when the pathway status was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

