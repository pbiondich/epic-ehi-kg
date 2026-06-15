# PLAN_DEVIATION_INFO

> This table holds plan-level deviation info for oncology treatment plans, including deviation instant, deviation user, and deviation change type.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the oncology treatment plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEVIATION_UTC_DTTM` | DATETIME (UTC) |  | This stores the instants the plan deviated from the protocol. |
| 4 | `DEVIATION_USER_ID` | VARCHAR |  | Stores the users who made the treatment plan deviations |
| 5 | `DEVIATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DEVIATION_ACTION_TYPE_C_NAME` | VARCHAR | org | This is the change action type of the plan deviation, for example, creating a blank plan, or creating a plan that is not from a suggested protocol, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

