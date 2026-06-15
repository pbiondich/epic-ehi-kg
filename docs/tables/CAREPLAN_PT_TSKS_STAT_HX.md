# CAREPLAN_PT_TSKS_STAT_HX

> This table stores the history items for status changes of patient tasks within a care plan.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PT_TSKS_STAT_HX_C_NAME` | VARCHAR |  | The status of patient tasks within this care plan. |
| 4 | `PT_TSKS_STAT_HX_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the status was changed. |
| 5 | `PT_TSKS_STAT_C_NAME` | VARCHAR |  | The history of statuses of patient-assigned tasks within the care plan. |
| 6 | `PT_TSKS_STAT_RSN_C_NAME` | VARCHAR |  | The history of reasons for the status of patient-assigned tasks within the care plan. |
| 7 | `PT_TSKS_HX_USER_ID` | VARCHAR |  | The history of users who caused the status of patient-assigned tasks within the care plan. |
| 8 | `PT_TSKS_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

