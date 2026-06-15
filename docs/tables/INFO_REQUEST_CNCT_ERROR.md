# INFO_REQUEST_CNCT_ERROR

> This table contains information about errors on Additional Information Contacts.

**Primary key:** `INFO_REQ_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFO_REQ_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the Additional Information Request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `INFO_REQ_ERR_TYPE_C_NAME` | VARCHAR |  | The type of error associated with this Additional Information Contact. |
| 5 | `INFO_REQ_ERR_SEVERITY_C_NAME` | VARCHAR |  | The severity of the error associated with this Additional Information Contact. |
| 6 | `ERROR_MESSAGE_TEXT` | VARCHAR |  | The text of the error message associated with this Additional Information Contact. |
| 7 | `ERROR_LOG_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which this error was logged. |
| 8 | `ERROR_LOG_DTTM` | DATETIME (Local) |  | The instant at which this error was logged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFO_REQ_ID` | [INFO_REQUEST](INFO_REQUEST.md) | sole_pk | high |

