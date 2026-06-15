# DOCS_RCVD_EVT_LAST_COMPLD

> This tables contains information regarding the most recently compiled event list received document.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAST_COMPLD_EVT_ORG_ID` | NUMERIC |  | The unique ID of the data exchange organization that compiled this row's Event List most recently. |
| 4 | `LAST_COMPLD_EVT_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 5 | `LST_COMPLD_EVT_DOCUMENT_CSN_ID` | NUMERIC |  | The unique contact serial number of the received document for the last compiled Event List. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

