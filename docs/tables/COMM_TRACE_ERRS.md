# COMM_TRACE_ERRS

> Errors encountered during the communication.

**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COMM_ERR_C_NAME` | VARCHAR | org | Contains the list of error(s) generating when sending the response. This item is the error number. |
| 5 | `ERROR_DESCRIPTION` | VARCHAR |  | Contains the list of error(s) generating when sending the response. This item is the error description. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

