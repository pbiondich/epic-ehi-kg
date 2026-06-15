# AUTO_TASK_AUDIT

> This table contains the audit history for tasks that have been created or updated by the Event Engine. This table stores the following audit history for a task: triggering event, event source, event contact serial number (CSN), event time, and action taken on the task.

**Primary key:** `TASK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique identifier for the task instance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADT_EVENT_C_NAME` | VARCHAR |  | Audit table for automatically created outpatient tasks - the event that created the task. |
| 4 | `EVENT_SOURCE_C_NAME` | VARCHAR |  | The category ID for the source of the event that triggered the automatic task change. |
| 5 | `EVENT_CSN_ID` | NUMERIC |  | The unique contact serial number of the patient encounter that corresponds with the event that triggered the automatic task change. |
| 6 | `EVENT_TIME_UTC_DTTM` | DATETIME (UTC) |  | Audit table for automatically created outpatient tasks - the timestamp of the event that created the task. |
| 7 | `ACTION_C_NAME` | VARCHAR |  | Audit table for automatically created outpatient tasks - the action the event took on the task. |
| 8 | `RX_FILL_ACTION_TYPE_C_NAME` | VARCHAR | org | Audit table for automatically created outpatient tasks - the prescription fill status that created the task. |
| 9 | `SRC_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `AUDIT_EXT_ENC_REF` | VARCHAR |  | Within the audit table for automatically created episode tasks, this item stores the base DXR reference ID of the external encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

