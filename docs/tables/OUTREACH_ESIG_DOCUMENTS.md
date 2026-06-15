# OUTREACH_ESIG_DOCUMENTS

> This table stores documents sent to patients for e-signature prior to an outreach.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESIG_DOCUMENT_ID` | VARCHAR |  | For outreach tasks, the document to send to the patient for e-signature. |
| 4 | `ESIG_REL_ORDER_ID` | NUMERIC |  | The order related to the e-signature document, if any. |
| 5 | `ESIG_DOC_SEND_DATE` | DATETIME |  | The date to send the e-signature document to the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

