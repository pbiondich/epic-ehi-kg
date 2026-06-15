# PLAN_STUDY_VERSION_INFO

> This table contains the associated study version information of the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_VERSION` | VARCHAR |  | The information about the current and past versions of the treatment plan. |
| 4 | `STUDY_VERSION_UPDATED_UTC_DTTM` | DATETIME (UTC) |  | The instant the study version associated with a treatment plan was updated to a new version. |
| 5 | `STUDY_VERSION_NO_CHANGE_RSN_C_NAME` | VARCHAR | org | The reason entered when not changing the treatment plan. |
| 6 | `STUDY_VERSION_NO_CHANGE_CMT` | VARCHAR |  | The comments entered when not changing the treatment plan. |
| 7 | `STUDY_VER_UPDATED_BY_USER_ID` | VARCHAR |  | The user ID for the user who updated the associated version of the treatment plan. |
| 8 | `STUDY_VER_UPDATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

