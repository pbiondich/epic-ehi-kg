# OR_LOG_PANEL_TIME1

> The OR_LOG_PANEL_TIME1 table contains OR management system log panel timing information for the first panel.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the panel time refers to. |
| 2 | `LINE` | INTEGER | PK | The line number of the panel time in the surgical log. |
| 3 | `PANEL_TIME_EVENT_C_NAME` | VARCHAR | org | The event set up to take place in a panel in the surgical log. |
| 4 | `PANEL_START_TIME` | DATETIME (Local) |  | The date and time the event began in the surgical log. |
| 5 | `PANEL_END_TIME` | DATETIME (Local) |  | The date and time the event ended in the surgical log. |
| 6 | `PANEL_EVENT_ELPSD` | INTEGER |  | Indicates the total amount of time for the event in the surgical log. |
| 7 | `PANEL_PROC_ID` | VARCHAR |  | The unique ID of the surgical procedure, if this event is associated with a particular procedure. |
| 8 | `PANEL_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 9 | `PANEL_EVENT_C_NAME` | VARCHAR |  | The panel level event. This line will be blank when a procedure level event was documented. |
| 10 | `PROCEDURE_EVENT_C_NAME` | VARCHAR |  | The procedure level event. This line will be blank when a panel level event was documented. |
| 11 | `INST_PNL1_INTER_UTC_DTTM` | DATETIME (UTC) |  | Instant of update for an event in panel 1. This will be used for Event Interval functionality. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

