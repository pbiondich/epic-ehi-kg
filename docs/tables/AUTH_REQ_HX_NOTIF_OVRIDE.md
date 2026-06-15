# AUTH_REQ_HX_NOTIF_OVRIDE

> This table contains overrides to authorization request notification milestones. The values in this table override system computer values for turnaround time.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COMM_PURPOSE_C_NAME` | VARCHAR |  | The communication purpose category ID of the notification override. |
| 5 | `NOTIF_RECPNT_TYPE_C_NAME` | VARCHAR |  | The recipient type category ID of the notification override. |
| 6 | `NOTIF_METHOD_C_NAME` | VARCHAR |  | The notification method category ID of the notification override. |
| 7 | `OVERRIDE_LOCAL_DTTM` | DATETIME (Local) |  | The date and time (local) of the notification override. |
| 8 | `OVERRIDE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the notification override. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

