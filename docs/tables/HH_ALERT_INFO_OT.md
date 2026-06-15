# HH_ALERT_INFO_OT

> This table stores the overtime information for Home Health Alerts.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `NUM` | INTEGER |  | This is the contact number for home health alerts. |
| 5 | `OVERRIDE_NAME` | VARCHAR |  | The user-configured name of the alert. |
| 6 | `OVERRIDE_ACTIVE` | VARCHAR |  | The override for the active status of the alert. |
| 7 | `ALERT_STATUS_C_NAME` | VARCHAR |  | The status of the alert. |
| 8 | `REC_INTVL_OVERRIDE` | INTEGER |  | The user-configured recurrence interval of the alert. |
| 9 | `REMINDER_OFFSET` | INTEGER |  | The user-configured reminder offset for the alert. |
| 10 | `NUM_DAYS_ACTIVE_OVERRIDE` | INTEGER |  | The user-configured number of days active for the alert. |
| 11 | `HIGH_PRIORITY_OFFSET_OVERRIDE` | INTEGER |  | The user-configured offset value for the alert. |
| 12 | `ALERT_DUE_DATE` | DATETIME |  | The default alert due date. |
| 13 | `OVERRIDE_DUE_DATE` | DATETIME |  | The user-configured alert due date. |
| 14 | `NOTE_ID` | VARCHAR | shared | The ID of the note associated with the alert. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

