# DOCS_RCVD_COM_RESRC_SVC

> This table stores the services recommended at a particular community resource.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COMM_RESRC_SVC_REFERENCE_IDENT` | VARCHAR |  | The unique reference ID of a discrete community resource usage |
| 6 | `COMM_RESRC_SVC_USAGE_REF_IDENT` | VARCHAR |  | Stores the reference ID of the community resource usage that is recommending this community resource service. |
| 7 | `COMM_RESRC_SVC_RECD_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

