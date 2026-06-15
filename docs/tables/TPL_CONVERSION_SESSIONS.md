# TPL_CONVERSION_SESSIONS

> This table contains information about treatment plan conversion sessions.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONVSESS_FROM_DAY` | INTEGER |  | The line in Treatment Day ID (I TPL 5000) of the first day in this conversion session. |
| 4 | `CONVSESS_TO_DAY` | INTEGER |  | The line in Treatment Day ID (I TPL 5000) of the day after the last day in this session. This can be blank if the session includes the last day in the plan. |
| 5 | `CONVSESS_STATUS_C_NAME` | VARCHAR |  | The status of a conversion session for this plan. |
| 6 | `CONVSESS_TYPE_C_NAME` | VARCHAR |  | The type of a conversion session for a plan, whether inpatient or outpatient. |
| 7 | `CONVSESS_ACT_UTC_DTTM` | DATETIME (UTC) |  | The instant this conversion session action was done. |
| 8 | `CONVSESS_ACT_USR_ID` | VARCHAR |  | The user who took this conversion session action. |
| 9 | `CONVSESS_ACT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

