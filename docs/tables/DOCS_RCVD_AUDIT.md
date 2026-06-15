# DOCS_RCVD_AUDIT

> Care Everywhere Received Documents Audit contains a list of documents of a particular type received for a patient including the doc, request and message ids, instants, users, status, and contexts.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `DOC_ID_AUDIT` | VARCHAR |  | Document id received from the remote organization |
| 4 | `REQ_DOC_ID_AUDIT` | VARCHAR |  | Document ID that was requested from the remote organization |
| 5 | `CEID_ID_AUDIT` | VARCHAR |  | Care Everywhere ID requested |
| 6 | `INSTANT_AUDIT_TM` | DATETIME (Local) |  | Instant for this audit line |
| 7 | `REQ_TOKEN_AUDIT` | VARCHAR |  | Message request information |
| 8 | `REQ_USER_AUDIT_ID` | VARCHAR |  | User ID of the person requesting the document |
| 9 | `REQ_USER_AUDIT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `REQ_STATUS_C_NAME` | VARCHAR |  | The status for this audit line of the request |
| 11 | `REQ_CONTEXT_C_NAME` | VARCHAR |  | Context in which the request was placed |
| 12 | `REQ_STA_RSN_CODE_C_NAME` | VARCHAR |  | Code for document request status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

