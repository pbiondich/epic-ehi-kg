# DOCS_RCVD_PAT_IDENTIFIER

> This table stores the patient identifier information extracted from a document received.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PAT_IDENTIFIER` | VARCHAR |  | Identifier to link patient with other tables. |
| 5 | `PAT_DISPLAY_NAME` | VARCHAR |  | Patient's name for display. |
| 6 | `PAT_FAMILY_NAME` | VARCHAR |  | Patient's family name. |
| 7 | `PAT_LEGAL_RCPT_MEM_SEX_C_NAME` | VARCHAR | org | The patient legal sex category ID as gathered from a document received. |
| 8 | `PAT_BIRTH_DATE` | DATETIME |  | The date when the patient was born. |
| 9 | `PAT_NATIONAL_IDENTIFIER` | VARCHAR |  | Patient's national identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

