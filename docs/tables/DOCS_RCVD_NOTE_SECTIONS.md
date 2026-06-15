# DOCS_RCVD_NOTE_SECTIONS

> Stores note section data received.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `NOTE_SECTION_IDENTIFIER` | VARCHAR |  | Stores unique identifier for the note section we received |
| 6 | `NOTE_SECTION_TYPE` | VARCHAR |  | Stores LOINC code for the section type |
| 7 | `NOTE_SECTION_NOTE_ID` | VARCHAR |  | HNO ID where the note text is saved |
| 8 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 9 | `NOTE_SECTION_LENGTH` | INTEGER |  | This item stores total number of characters in the note section. |
| 10 | `HUMAN_REVIEWED_YN` | VARCHAR |  | Flag to say if a note section was reviewed by a human before being sent to Epic, or if it was purely auto-generated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

