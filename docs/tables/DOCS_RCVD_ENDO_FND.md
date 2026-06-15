# DOCS_RCVD_ENDO_FND

> This table stores suggested endoscopy findings received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SUGG_FND_RESULT_RPT_TYPE_C_NAME` | VARCHAR |  | The result report type associated with the finding data in this line. |
| 6 | `SUGG_ENDOSCOPY_TYPE_C_NAME` | VARCHAR | org | The endoscopy finding type associated with this suggestion line |
| 7 | `SUGG_FND_IDENT` | VARCHAR |  | Stores unique identifier for the suggested finding we received |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

