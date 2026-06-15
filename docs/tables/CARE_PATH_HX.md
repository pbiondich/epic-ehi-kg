# CARE_PATH_HX

> Historical information for Care Path episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_STEP_IDENT` | INTEGER |  | History of care path steps on which the patient has been, where the most recent step is considered the active care path step. |
| 4 | `HX_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The time, stored as UTC, when the patient moved to a step on a care path and that step was made active. |
| 5 | `HX_USER_ID` | VARCHAR |  | User that moved the patient to a step on a Care Path. |
| 6 | `HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HX_LINK_IDENT` | INTEGER |  | This item stores the care path link that was used to move the patient to this care path step. |
| 8 | `HX_ALERT_ID` | NUMERIC |  | This item networks to historical information about the advisory that moved the patient to a step on a care path. |
| 9 | `HX_EFFECTIVE_DATE` | DATETIME |  | The effective date for the care path step as entered by the user when manually moving the patient to that step on the care path. |
| 10 | `HX_INSTANT_LOCAL_DTTM` | DATETIME (Local) |  | The time, stored as local time, when the patient moved to a step on a care path and that step was made active. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

