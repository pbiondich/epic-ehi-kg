# LAB_EVENT_HX

> This table contains the lab follow-up task event history that audits the events and actions that were taken on follow-up tasks.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_EVENTHX_TYPE_C_NAME` | VARCHAR | org | The event history type category number for the follow-up task history event. |
| 4 | `LAB_EVENTHX_DT_DTTM` | DATETIME (Attached) |  | The date and time when the event occurred. |
| 5 | `LAB_EVENTHX_USR_ID` | VARCHAR |  | The unique identifier of the user who is associated with this event. |
| 6 | `LAB_EVENTHX_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LAB_EVENTHX_CMT` | VARCHAR |  | The comments associated with this event. |
| 8 | `LAB_EVENTHX_ORD_ID` | NUMERIC |  | The unique identifier of the order record that is associated with this event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

