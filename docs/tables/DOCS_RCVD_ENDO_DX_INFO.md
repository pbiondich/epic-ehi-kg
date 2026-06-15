# DOCS_RCVD_ENDO_DX_INFO

> Contains information about endoscopy procedure diagnoses extracted from customer systems for use in Cosmos.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ENDO_DX_REF_IDENT` | VARCHAR |  | This item stores the unique reference id associated with the endoscopy diagnosis. |
| 6 | `ENDO_DX_SRC_REFID` | VARCHAR |  | Stores the reference ID of the endoscopy procedure this diagnosis is related to. |
| 7 | `ENDO_DX_DDP_REFID` | VARCHAR |  | Stores the deduplicated reference ID of the endoscopy procedure this diagnosis is related to. |
| 8 | `ENDO_DX_IND_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 9 | `ENDO_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

