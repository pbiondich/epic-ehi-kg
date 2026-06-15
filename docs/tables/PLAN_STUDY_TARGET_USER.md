# PLAN_STUDY_TARGET_USER

> This table contains the user ID of the user who is applying the study amendment banner above the treatment plan from the Reporting Workbench and the instant of this action.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_TARGET_USER_ID` | VARCHAR |  | The user ID of the user who runs the reporting workbench report and applies the study amendment banner above the treatment plan. |
| 4 | `STUDY_TARGET_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `STUDY_TARGET_USER_UTC_DTTM` | DATETIME (UTC) |  | The instant the user applied the study amendment banner above the treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

