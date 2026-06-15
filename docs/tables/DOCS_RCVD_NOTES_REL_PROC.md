# DOCS_RCVD_NOTES_REL_PROC

> This table stores the free text names of procedures associated with the external note.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of a clinical note in the received document. Together with DOCUMENT_ID and CONTACT_DATE_REAL, this forms the foreign key to the DOCS_RCVD_CLINICAL_NOTES table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple external procedures names associated with the received document and the clincal note from the DOCS_RCVD_CLINICAL_NOTES table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `NOTE_REL_PROC_NAME` | VARCHAR |  | Free text name of a procedure associated with the external note |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

