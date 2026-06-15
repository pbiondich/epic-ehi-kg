# BPA_RFL_CRIT_WEB_UPD_INST

> The table to show the instant of the last update for the asynchronous evaluation of the web service related protocol criteria.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `BPA_WEB_UPD_INST_DTTM` | DATETIME (Local) |  | For web service related protocol criteria, this item stores the instant of the last update for the asynchonous evaluation of the criteria. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

