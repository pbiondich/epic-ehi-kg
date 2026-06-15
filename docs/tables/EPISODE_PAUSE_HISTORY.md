# EPISODE_PAUSE_HISTORY

> This table stores the audit data for the items in the Social Care - Pause Status (I HSB 64100) related group, such as audit data for episode pauses.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAUSE_HISTORY_STATUS_C_NAME` | VARCHAR | org | The status category ID of the pause when it was added, edited, or deleted. |
| 4 | `PAUSE_HISTORY_START_DATE` | DATETIME |  | The date the pause was set to start before being updated. |
| 5 | `PAUSE_HISTORY_END_DATE` | DATETIME |  | The date the pause was set to end before being updated. |
| 6 | `PAUSE_HISTORY_REASON_C_NAME` | VARCHAR | org | The pause reason category ID when the pause period was added, edited, or deleted. |
| 7 | `PAUSE_HISTORY_UPDATE_USER_ID` | VARCHAR |  | The unique ID of the user who most recently updated the pause period. |
| 8 | `PAUSE_HISTORY_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `PAUSE_HISTORY_UPD_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that a pause period was last updated. |
| 10 | `PAUSE_HISTORY_KEY` | VARCHAR |  | This item stores the key used to identify a particular scheduled pause period. |
| 11 | `PAUSE_HISTORY_EVENT_C_NAME` | VARCHAR |  | The audit even category ID for the event that occurred for the pause period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

