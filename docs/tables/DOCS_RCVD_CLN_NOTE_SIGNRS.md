# DOCS_RCVD_CLN_NOTE_SIGNRS

> Clinical note signer information for notes recieved externally.

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
| 5 | `NOTE_REFERENCE_IDENT` | VARCHAR |  | The reference ID of a clinical note, which uniquely identifies a note sent through C-CDA. |
| 6 | `NOTE_LOCAL_UNIQUE_IDENT` | VARCHAR |  | The locally-assigned unique identifier to identify clinical notes sent through FHIR. |
| 7 | `NOTE_SIGNER_NAME` | VARCHAR |  | A clinical note signer's name. |
| 8 | `NOTE_SIGNED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when a clinical note was signed. |
| 9 | `NOTE_SIGNER_ROLE_C_NAME` | VARCHAR |  | A note signer's role in authenticating the content of a clinical note. |
| 10 | `NOTE_SIGNER_NPI` | VARCHAR |  | A clinical note signer's NPI |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

