# CARE_PLAN_INT_INFO

> Extracts identifying information about the Care Plan Interventions associated with the treatment plan (ID, day, user, and instant).

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_CP_INT_TRTDAY_ID` | NUMERIC |  | Stores treatment day Care Plan intervention was added from |
| 4 | `IP_CP_INT_USR_ID` | VARCHAR |  | Stores user that added Care Plan intervention from Pathway |
| 5 | `IP_CP_INT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `IP_CP_INT_INST_DTTM` | DATETIME (Local) |  | Stores instant Care Plan intervention was added from Pathway |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

