# DOCS_RCVD_PAT_GIVEN_NAMES

> This table extracts the multiple patient given names from a document received.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the patient give name in a document received. Together with the document ID and the real contact date, this forms the foreign key to any table extracted from documents received. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple patient given names associated with a document received and the patient from the patient info table. |
| 5 | `PAT_GIVEN_NAMES` | VARCHAR |  | A patient's given name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

