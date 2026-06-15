# TPL_CAREPLAN_GOALS

> This table lists the Care Plan Goals associated with each treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_CP_GOAL_ID` | VARCHAR |  | Stores Care Plan Goal ID added from Pathway |
| 4 | `IP_CP_GL_TRTDAY_ID` | NUMERIC |  | Stores Treatment Day Goal was added from. |
| 5 | `IP_CP_GOAL_USER_ID` | VARCHAR |  | The user that added Care Plan goal from Pathway. |
| 6 | `IP_CP_GOAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `IP_CP_GOAL_DTTM` | DATETIME (Local) |  | The instant that the Care Plan goal was added from Pathway. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

