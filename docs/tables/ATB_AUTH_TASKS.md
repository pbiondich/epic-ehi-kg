# ATB_AUTH_TASKS

> This table contains data for authorization tasks. One row represents a task.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TASK_ID_REF` | VARCHAR |  | Unique reference ID that can be used to point to a certain line in the tasks related group. |
| 4 | `AUTH_TASK_TYPE_C_NAME` | VARCHAR |  | Represents the type of task that must be completed in order to complete the associated authorization objective. |
| 5 | `AUTH_TASK_STATUS_C_NAME` | VARCHAR |  | Represents the status of the task on a given line of the tasks related group. |
| 6 | `DISPLAY_STRING` | VARCHAR |  | User-facing string explaining the steps required for this task to be completed. |
| 7 | `TASK_OBJ_ID_REF` | VARCHAR |  | Contains the reference ID of the objective that this task is a requirement for. |
| 8 | `CAN_MANUALLY_RESOLVE_YN` | VARCHAR |  | Stores whether or not a task can be manually resolved. If No or empty, it can only be resolved by automated validations running again. |
| 9 | `PYR_DV_ERROR_TYPE_C_NAME` | VARCHAR |  | For tasks created from a payer-provided validation, stores the type of data validation error that created this task. |
| 10 | `TASK_CREATION_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant that this task was created, in the UTC timezone. |
| 11 | `TASK_CREATION_USER_ID` | VARCHAR |  | Stores the user responsible for creating this task. |
| 12 | `TASK_CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `TASK_COMPLETION_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant that this task was created. Instant is stored formatted in UTC timezone. |
| 14 | `TASK_COMPLETION_USER_ID` | VARCHAR |  | Stores the user responsible for completing the task. |
| 15 | `TASK_COMPLETION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `GRDRL_SETTING_ID` | NUMERIC |  | Contains the ID of the guardrail record that is responsible for creating this task. |
| 17 | `GRDRL_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 18 | `GENERATION_RULE_ID` | VARCHAR |  | Contains the ID of the rule record that is responsible for creating this task. |
| 19 | `GENERATION_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 20 | `SECONDARY_DISPLAY_CONTENT` | VARCHAR |  | The secondary display content to show with the task when displayed to a user. This does not contribute towards the task fingerprint. When displaying the task, if this item is not populated, the system will attempt to calculate the secondary display content dynamically. |
| 21 | `TSK_TYP_MSG_CODE_C_NAME` | VARCHAR |  | This item contains a category value specific to the individual validation or check that results in this task being created. Used as a sort of categorization of the task's display message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

