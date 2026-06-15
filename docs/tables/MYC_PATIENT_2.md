# MYC_PATIENT_2

> This table supplements the information contained in the MYC_PATIENT table. It contains one row for each web-based chart system account. The data contained in each row consists of basic account information and configuration.

**Overflow of:** [MYC_PATIENT](MYC_PATIENT.md)  
**Primary key:** `MYPT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYPT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the account record. |
| 2 | `HIDE_FINISHED_TASKS_YN` | VARCHAR |  | Indicates whether finished tasks in the To Do activity should be hidden or not. A null value means the user has never set this preference. |
| 3 | `GOAL_MYCNOTE_ID` | NUMERIC |  | WNO ID of the patient goals note. Only populated by the personal goals note type. |
| 4 | `DISMISS_LINK_ACCT_MSG_UTC_DTTM` | DATETIME (UTC) |  | The instant (UTC) the link account message was dismissed in the Track My Health activity. |
| 5 | `TASK_GROUPING_PREFEREN_C_NAME` | VARCHAR |  | This item stores a user's preference for how tasks are grouped in the Care Companion activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

