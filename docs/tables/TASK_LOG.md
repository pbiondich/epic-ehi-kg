# TASK_LOG

> This table extracts the related table Task Log: Instant (I LTK 81900), which contains the log of actions that happened on a task.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TASK_LOG_INST_DTTM` | DATETIME (UTC) |  | The instant in UTC the action was done. |
| 4 | `TASK_LOG_ACTION_TYPE_C_NAME` | VARCHAR |  | The type of action logged. |
| 5 | `TASK_LOG_ACTION_C_NAME` | VARCHAR |  | The action that was done on the task. |
| 6 | `MYPT_ID` | VARCHAR | shared | The MyChart user (WPR) who did the action. |
| 7 | `DISPLAY_NAME` | VARCHAR |  | The new display when the display name (LTK-41) is changed. |
| 8 | `TASK_DESC` | VARCHAR |  | The new description when the description (LTK-42) is changed. |
| 9 | `FREQ_ID` | VARCHAR | FK→ | The new frequency record when the frequency (LTK-300) is changed. |
| 10 | `FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 11 | `TASK_START_UTC_DTTM` | DATETIME (UTC) |  | The new start instant when the start date (LTK-540) is changed. |
| 12 | `TASK_END_UTC_DTTM` | DATETIME (UTC) |  | The new end instant when the end date (LTK-550) or duration (LTK-556) is changed. |
| 13 | `GOAL_ID` | VARCHAR | FK→ | The new goal record when the goal (LTK-220) is changed. |
| 14 | `TASK_START_TIME_C_NAME` | VARCHAR |  | The new start type when the start type (LTK-270) is changed. |
| 15 | `TASK_START_OFFSET_DAYS` | INTEGER |  | The new start offset days when the start offset days (I LTK 580) is changed. |
| 16 | `TASK_START_OFFSET_TYPE_C_NAME` | VARCHAR |  | The new start offset type when the start offset type (LTK-581) is changed. |
| 17 | `DURATION_DAYS` | INTEGER |  | The new duration in days when the duration (LTK-556) is changed. |
| 18 | `DAYS_AFTER_DISCHARGE` | INTEGER |  | The new days after discharge when the days after discharge (LTK-81051) is changed. |
| 19 | `SCHEDULE_STATUS_C_NAME` | VARCHAR |  | The new schedule status when the schedule status (LTK-81011) is changed. |
| 20 | `FLO_THRESHOLD_VALUE` | NUMERIC |  | The new flowsheet threshold value when the flowsheet threshold value (LTK-43) is changed. |
| 21 | `TASK_LOG_PAUSE_REASON_C_NAME` | VARCHAR |  | The new pause reason when the pause reason (I LTK 81014) was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FREQ_ID` | [IP_FREQUENCY](IP_FREQUENCY.md) | sole_pk | high |
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

