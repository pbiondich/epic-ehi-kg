# EPISODE_PAUSE

> This table contains data on past and present Social Care episode pause periods that currently exist in the system.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAUSE_STATUS_C_NAME` | VARCHAR | org | The pause status category ID for the pause period. |
| 4 | `PAUSE_START_DATE` | DATETIME |  | The date when the pause was started. |
| 5 | `PAUSE_END_DATE` | DATETIME |  | The date when the pause was ended. |
| 6 | `PAUSE_REASON_C_NAME` | VARCHAR | org | The pause reason category ID for the pause period. |
| 7 | `UPDATE_USER_ID` | VARCHAR |  | The unique ID of the user who most recently updated the pause period. |
| 8 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that a pause period was last updated. |
| 10 | `PAUSE_KEY` | VARCHAR |  | This item contains the key used to identify a pause period (i.e. row in the HSB-64100 related group). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

