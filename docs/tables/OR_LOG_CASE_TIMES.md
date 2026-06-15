# OR_LOG_CASE_TIMES

> The OR_LOG_CASE_TIMES table contains OR management system log timing information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log referred to by the case times. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the tracking event in the surgical log. |
| 3 | `TRACKING_EVENT_C_NAME` | VARCHAR | org | The category value which lists the event being tracked within your facility for the surgical log. |
| 4 | `TRACKING_TIME_IN` | DATETIME (Local) |  | The date and time at which the patient was moved into the corresponding item in the event column in the surgical log. |
| 5 | `TRACKING_TIME_OUT` | DATETIME (Local) |  | The date and time at which the patient was moved out of the corresponding item in the event column in the surgical log. |
| 6 | `TRACKING_TIME_ELPS` | INTEGER |  | The total amount of time in seconds for the event in the surgical log. |
| 7 | `TRACK_EVENT_TYPE_C_NAME` | VARCHAR | org | The category indicating the type of event, whether preop, intraop, or postop. |
| 8 | `TRACKING_STATUS_C_NAME` | VARCHAR | org | The category value indicating the progress status that corresponds to this timing event. |
| 9 | `TRACKING_STAT_INST` | DATETIME (Local) |  | The instant at which the status took effect. |
| 10 | `TRACKING_PAT_LOCATION_EVNT_ID` | NUMERIC |  | The patient location that triggered this event to be documented. |
| 11 | `TRACKING_LOCATION_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 12 | `INTERVAL_EVENT_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant of update for a case tracking event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

