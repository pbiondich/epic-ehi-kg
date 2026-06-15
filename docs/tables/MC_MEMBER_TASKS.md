# MC_MEMBER_TASKS

> This table contains information about health plan member tasks.

**Primary key:** `TASK_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `TASK_CONTEXT_C_NAME` | VARCHAR |  | The task context category ID for the task. |
| 3 | `TASK_TYPE_C_NAME` | VARCHAR |  | The task type category ID for the task. |
| 4 | `SOURCE_TEMPLATE_RECORD_ID` | VARCHAR |  | The unique ID of the task template record (LTT) associated with this task. |
| 5 | `SOURCE_TEMPLATE_RECORD_ID_RECORD_NAME` | VARCHAR |  | This column displays the name of the task template record. |
| 6 | `SOURCE_TASK_ID` | NUMERIC |  | The unique ID of the source task record (LTR) associated with this task. |
| 7 | `SOURCE_TASK_ID_TASK_NAME` | VARCHAR |  | The name of the task record. |
| 8 | `TASK` | VARCHAR |  | The task to be performed. |
| 9 | `START_INSTANT_LOCAL_DTTM` | DATETIME (Local) |  | The start instant for a task in local format. |
| 10 | `END_DATE` | DATETIME |  | The date when the task is marked as completed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

