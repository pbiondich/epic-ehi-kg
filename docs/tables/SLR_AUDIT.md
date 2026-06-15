# SLR_AUDIT

> This table contains auditing information for second-level reviews.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the second-level review. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `REQUEST_LAST_SAVED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the second-level review's request information was most recently edited. |
| 4 | `REQUEST_LAST_SENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the second-level review's request was most recently submitted. |
| 5 | `REVIEW_LAST_SAVED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the second-level review's physician review information was most recently edited. |
| 6 | `EDITING_USER_ID` | VARCHAR |  | The unique ID associated with the user who last edited the second-level review. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `EDITING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `EDIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the second-level review's contact was most recently edited. |
| 9 | `REQUEST_LAST_SAVED_USER_ID` | VARCHAR |  | The unique ID associated with the user who last edited the second-level review request. This column is frequently used to link to the CLARITY_EMP table. |
| 10 | `REQUEST_LAST_SAVED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `REQUEST_LAST_SENT_USER_ID` | VARCHAR |  | The unique ID associated with the user who last submitted the second-level review request. This column is frequently used to link to the CLARITY_EMP table. |
| 12 | `REQUEST_LAST_SENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `REVIEW_LAST_SAVED_USER_ID` | VARCHAR |  | The unique ID associated with the user who last edited the second-level review's physician review information. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `REVIEW_LAST_SAVED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `REQUEST_LAST_SAVED_LOCAL_DTTM` | DATETIME (Attached) |  | The local (patient encounter) instant the second-level review's request information was most recently edited. |
| 16 | `REQUEST_LAST_SENT_LOCAL_DTTM` | DATETIME (Attached) |  | The local (patient encounter) instant the second-level review's request was most recently submitted. |
| 17 | `REVIEW_LAST_SAVED_LOCAL_DTTM` | DATETIME (Attached) |  | The local (patient encounter) instant the second-level review's physician review information was most recently edited. |
| 18 | `EDIT_INSTANT_LOCAL_DTTM` | DATETIME (Attached) |  | The local (patient encounter) instant the second-level review's contact was most recently edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

