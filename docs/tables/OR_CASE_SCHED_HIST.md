# OR_CASE_SCHED_HIST

> The OR_CASE_SCHED_HIST table contains OR management system case scheduling history.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the OR scheduling history information. |
| 3 | `ROOM_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `HIST_DATE` | DATETIME (Local) |  | The date on which the case was scheduled. |
| 5 | `HIST_SCHED_USER_ID` | VARCHAR |  | The ID of the user that scheduled the case. |
| 6 | `HIST_SCHED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HIST_SCHED_TIME` | DATETIME (Local) |  | The time at which the user scheduled the case. |
| 8 | `MATCH_SRVC_BLOCK_C_NAME` | VARCHAR | org | Stores the matching service block ID of the schedule instance if the match type is a service block. |
| 9 | `SCHEDULING_SOURCE_C_NAME` | VARCHAR |  | The source activity or workflow associated with this entry in the scheduling history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

