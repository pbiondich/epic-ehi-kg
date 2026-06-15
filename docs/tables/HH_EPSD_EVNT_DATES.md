# HH_EPSD_EVNT_DATES

> This table contains event dates information for Home Health episodes. This information can be entered manually in the Episode of Care Information form in Intake. For certain events, such as Admit, Discharge, and SOC, the information is triggered automatically.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DATE_OF_EVENT` | DATETIME |  | Date of event in the episode. |
| 4 | `DATE_EVENT_C_NAME` | VARCHAR | org | Category list selection for event on this date. Links to category table ZC_DATE_EVENT. |
| 5 | `DATE_ENTERED_BY_ID` | VARCHAR |  | ID of the user who entered the event. Links to CLARITY_EMP. |
| 6 | `DATE_ENTERED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EVENT_COMMENTS` | VARCHAR |  | Comments text typed in by a user. |
| 8 | `EVENT_CREAT_DTTM` | DATETIME (UTC) |  | Stores the time and date when an event type was created for the first time for a Home Care episode. |
| 9 | `EVENT_UPDATE_DTTM` | DATETIME (UTC) |  | Stores the time and date when an event type was last updated for a Home Care episode. If an event is not updated after being created then this item will contain the same value as Summary Block / Episode record (HSB) 27408. |
| 10 | `LAST_UPDATE_USER_ID` | VARCHAR |  | The unique ID associated with the user who most recently edited the event in this row. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `LAST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

