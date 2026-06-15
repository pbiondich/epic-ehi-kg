# IP_WORKLIST_COMP

> This table provides information on work list tasks.

**Primary key:** `TASK_ID`, `LINE`  
**Columns:** 42  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique identifier for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMP_ON_TIME` | DATETIME (Local) |  | The instant a work list task was completed. |
| 4 | `COMP_USER_ID` | VARCHAR |  | The unique ID of the user completing a work list task. For automatically completed episode tasks, this will be blank. |
| 5 | `COMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SCHED_TIME` | DATETIME (Local) |  | The instant the work list task was scheduled. |
| 7 | `CANC_USER_ID` | VARCHAR |  | The unique ID of the user canceling a work list task. |
| 8 | `CANC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `INSTANCE_STATUS_C_NAME` | VARCHAR |  | The current instance status category ID for the task record. |
| 10 | `ANCHOR_SCHED_I_DTTM` | DATETIME (Local) |  | If this task was created from an anchored order, this is the due time of the anchor order related to this task due time |
| 11 | `NOTIFICATION_GRP_C_NAME` | VARCHAR | org | The notification group category ID for the task. |
| 12 | `SCHED_TIME_UTC_DTTM` | DATETIME (UTC) |  | The instant the work list task was scheduled in UTC. |
| 13 | `COMPLETED_IN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number (CSN) of the patient contact in which the task was completed. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 14 | `TASK_COMP_DATE` | DATETIME |  | The date the user indicates the task was completed |
| 15 | `OUTCOME_C_NAME` | VARCHAR | org | The task outcome category ID for the task. |
| 16 | `REMOVED_IN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number (CSN) of the patient contact from which a user removed the task. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 17 | `UNCOMPLETED_IN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number (CSN) of the patient contact from which a user undid the completion action for the task. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 18 | `TASK_NOTE_ID` | VARCHAR |  | The unique identifier of the note record for the comment associated with a specific task instance. |
| 19 | `TASK_RESPONSIBLE_USER_ID` | VARCHAR |  | The responsible user assigned to an instance of a care plan task. |
| 20 | `TASK_RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `TASK_RESPONSIBLE_IB_POOL_ID` | NUMERIC |  | The responsible pool assigned to an instance of a care plan task. |
| 22 | `TASK_RESPONSIBLE_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 23 | `EDIT_SOURCE_LINE` | INTEGER |  | If this task instance was created by editing an existing instance, this value is the line number of the previous version of this task instance. |
| 24 | `EDIT_NEXT_LINE` | INTEGER |  | If this task instance was subsequently edited, this line is the location of the next version of this task instance. |
| 25 | `ORIG_SCHED_DTTM` | DATETIME (Local) |  | The instant a task instance was first scheduled. |
| 26 | `MOVE_COUNT` | INTEGER |  | The number of times a task instance has been moved relative to this version of the instance. |
| 27 | `LAST_MOVE_USER_ID` | VARCHAR |  | The user attributed to the last move of this task instance. |
| 28 | `LAST_MOVE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `COMP_TIME_UTC_DTTM` | DATETIME (UTC) |  | The instant a work list task was completed in UTC. |
| 30 | `PLANNED_COMP_DATE` | DATETIME |  | Date when a task is planned to be performed, as distinct from when the task is due. |
| 31 | `TASK_SKIP_RSN_C_NAME` | VARCHAR | org | The category value reason for skipping the task. |
| 32 | `TASK_SKIP_RSN_TXT` | VARCHAR |  | The free-text reason for skipping a task. |
| 33 | `COMP_PROXIMITY_C_NAME` | VARCHAR |  | Proximity data for the task |
| 34 | `COMP_SOURCE_C_NAME` | VARCHAR |  | This item stores information about what context the task was completed from. |
| 35 | `COMP_LATENCY_SECONDS` | INTEGER |  | The number of seconds late that a safety check task was completed. If the task was completed before its due time, no value will be set. |
| 36 | `COMP_LATENCY_MINUTES` | INTEGER |  | The number of minutes late that a safety check task was completed. This is the difference in minutes of the row's due time and completion time. If the due time falls after the completion time, no value will be recorded. |
| 37 | `TASK_NONPROX_RSN_C_NAME` | VARCHAR | org | The category value ID for the reason why a user completed the task out of range. |
| 38 | `TASK_NONPROX_RSN_TEXT` | VARCHAR |  | The free text reason why a user completed the task out of range. |
| 39 | `UNTIMED_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant in UTC of the untimed task window where the untimed task is considered relevant and displayed to clinicians. |
| 40 | `UNTIMED_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant in UTC of the untimed task window where the untimed task is considered relevant and displayed to clinicians. |
| 41 | `UNTIMED_IS_SCHED_YN` | VARCHAR |  | This item determines if an untimed task is considered to have been scheduled, such that it should be treated as a normal scheduled task based on its I LTK 520 scheduled instant. |
| 42 | `TASK_COMP_METHOD_C_NAME` | VARCHAR |  | This item stores information about the method used to complete this task. While I LTK 502 is used to track the activity or client this task was completed from, this item tracks how the user completed it, such as manually or by using ambient documentation workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMPLETED_IN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `REMOVED_IN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `UNCOMPLETED_IN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

