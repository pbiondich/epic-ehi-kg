# CAREPLAN_TIMEMARK

> This table contains information about Care Plan Review / Documentation data.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier for the care plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TIMEMARK_USER_ID` | VARCHAR |  | User who made a care plan action. |
| 4 | `TIMEMARK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `TIMEMARK_DTTM` | DATETIME (Local) |  | Instant a care plan action was made. |
| 6 | `TIMEMARK_ACTION_C_NAME` | VARCHAR |  | Action made on the care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

