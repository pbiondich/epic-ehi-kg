# DOCS_RCVD_ADDL_ADDR_INFO

> The DOCS_RCVD_ADDL_ADDR_INFO table contains information about the patient for whom a given document was received from an external system. Specifically, it contains the discrete address fields, such as house number, floor, unit and building name, of the patient's address for that document, as supplied by the sending system.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact and so on. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ADDL_ADDR_FIELD_C_NAME` | NUMERIC |  | The type of additional address data (floor, unit, building name) stored in the related field (DXR 819). |
| 6 | `ADDL_DATA` | VARCHAR |  | The additional address data that the related "field" (DXR 817) line applies to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

