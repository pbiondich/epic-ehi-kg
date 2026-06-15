# AUTH_REQ_HX_DECISION_REQT

> This table contains the various decision-related timeliness requirements for a given review category for a contact.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `REVIEW_CATEGORY_C_NAME` | VARCHAR | org | The unique ID of the review category that the decision requirements apply to. |
| 5 | `CALCULATION_METHOD_C_NAME` | VARCHAR |  | The unique ID of the calculation method of the due date for this review category. |
| 6 | `DECISION_REQ_START_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the start instant for authorization request timeliness as determined for this review category. |
| 7 | `DECISION_STANDARD_DUE_UTC_DTTM` | DATETIME (UTC) |  | The calculated decision due date and time (UTC) of the authorization request without any extensions taken for this review category. |
| 8 | `DECISION_CURRENT_DUE_UTC_DTTM` | DATETIME (UTC) |  | The current decision due date and time (UTC) of the authorization request for this review category. |
| 9 | `ADDL_INFO_REQUEST_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) by which an additional information request extension can be taken for this review category. |
| 10 | `ADDL_INFO_RECEIPT_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) when the receipt of additional information is due. Only set if additional information was requested. |
| 11 | `DCSN_REQ_START_SRC_C_NAME` | VARCHAR |  | The source of the start instant for authorization request timeliness as determined for this review category. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

