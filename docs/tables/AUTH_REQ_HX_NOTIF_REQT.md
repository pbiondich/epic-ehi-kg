# AUTH_REQ_HX_NOTIF_REQT

> This table contains the various notification-related requirements for a given review category for a contact, along with when these requirements were satisfied.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `REVIEW_CATEGORY_C_NAME` | VARCHAR | org | The unique ID of the review category that the notification requirements apply to. |
| 5 | `NOTIF_RECPNT_TYPE_C_NAME` | VARCHAR |  | The unique ID of the required recipient type of the notification requirement. |
| 6 | `NOTIF_TOPIC_C_NAME` | VARCHAR |  | The unique ID of the notification topic of the notification requirement. |
| 7 | `RELATED_COMM_ID` | VARCHAR |  | The communication record that satisfies this notification requirement. |
| 8 | `NOTIF_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) that the notification requirement is due. |
| 9 | `NOTIF_COMPLETE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) that the notification requirement was completed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

