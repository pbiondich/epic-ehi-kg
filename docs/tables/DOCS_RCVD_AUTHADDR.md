# DOCS_RCVD_AUTHADDR

> The DOCS_RCVD_AUTHADDR table contains information about the Direct Address of the author(s) by whom a given document was created.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `AUTHOR_ADDR` | VARCHAR |  | Author Addresses column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the Direct addresses of the authors that were received in the document's metadata. |
| 6 | `AUTHOR_DXA_ID` | NUMERIC |  | Author Direct audit (DXA) ID column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the Direct audit (DXA) record ID of the author that was received in the document's metadata. |
| 7 | `AUTHOR_DXA_ID_MIXED_DIRECT_ADDR` | VARCHAR |  | Formatted like an email address, this is how Direct messaging knows where to send a message. This item is stored in mixed case to use in display in addressing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

