# RX_DELIVERY_ADDRESS

> This table contains the multiline address of a med stored in the DOCS_RCVD_MEDS table.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the medication in a document received. Together with the document ID and the real contact date, this forms the foreign key to the CENTRAL_DB_DOCS_RCVD table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple prescription delivery lines associated with the document received and the prescription from the documents received prescription table. |
| 5 | `RX_DELIVERY_LINE` | VARCHAR |  | A delivery address line of the prescription. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

