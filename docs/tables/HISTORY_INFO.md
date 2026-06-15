# HISTORY_INFO

> The HISTORY_INFO table contains notes and activities history information.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HISTORY_DATE` | DATETIME |  | The date when history information stored in the system. |
| 4 | `HISTORY_TIME` | DATETIME (Local) |  | The time when history information stored in the system. |
| 5 | `HISTORY_USER_ID` | VARCHAR |  | The unique ID of the user record who created this history row. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `HISTORY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HISTORY_DESCRIPTION` | VARCHAR |  | The description of this history information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

