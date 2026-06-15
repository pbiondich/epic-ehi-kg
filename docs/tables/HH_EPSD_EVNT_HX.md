# HH_EPSD_EVNT_HX

> This contains audit information about the event of an episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_HX_DATE` | DATETIME |  | History of the date of the event in the episode |
| 4 | `DATE_EVENT_C_NAME` | VARCHAR | org | History of the category list selection for the event. |
| 5 | `ENTERED_BY_USER_ID` | VARCHAR |  | History of the user IDs who entered the event. |
| 6 | `ENTERED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EVENT_COMMENT_HX` | VARCHAR |  | History of the comments left about this event. |
| 8 | `EDIT_USER_ID` | VARCHAR |  | The user who made the edits to the event data. |
| 9 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | The instant at which edits were made to the event data. . |
| 11 | `EDIT_LINE` | INTEGER |  | The line number of the event that was edited. This is the line number found in column LINE of HH_EPSD_EVNT_DATES. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

