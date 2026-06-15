# MEDCOM_RCVD_DETAILS

> Details about MedCom messages received.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LETTER_REASON_C_NAME` | VARCHAR | org | MedCom Category for the incoming document |
| 5 | `MEDCOM_SUBJECT` | VARCHAR |  | MedCom Subject for the incoming document |
| 6 | `MEDCOM_ACTIVITY_C_NAME` | VARCHAR | org | Stores if the MedCom message is a new message, a reply, or a forward |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

