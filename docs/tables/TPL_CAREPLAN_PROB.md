# TPL_CAREPLAN_PROB

> This table lists the Care Plan Problems associated with each treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_CP_PROB_ID` | VARCHAR |  | The Care Plan problem ID. |
| 4 | `IP_CP_PRB_TRTDAY_ID` | NUMERIC |  | The treatment day record the care plan problem was added from. |
| 5 | `IP_CP_PRB_USR_ID` | VARCHAR |  | The user that added the care plan problem from Pathway. |
| 6 | `IP_CP_PRB_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `IP_CP_PRB_DTTM` | DATETIME (Local) |  | The instant the care plan problem was added from Pathway. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

