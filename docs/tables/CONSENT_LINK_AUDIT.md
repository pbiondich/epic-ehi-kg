# CONSENT_LINK_AUDIT

> This table stores the link review history

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONSENT_LNK_CASE_ID` | VARCHAR |  | The case the consent is historically linked to. |
| 4 | `CONSENT_LNK_PANEL` | VARCHAR |  | The panels on a case the consent is historically linked to |
| 5 | `CONSENT_LNK_CINST_UTC_DTTM` | DATETIME (UTC) |  | The instant at which a historically linked consent was linked |
| 6 | `CONSENT_LNK_CUSER_ID` | VARCHAR |  | The user who linked a historically linked consent |
| 7 | `CONSENT_LNK_CUSER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CONSENT_LNK_CACT_C_NAME` | VARCHAR |  | The action by which a historically linked consent was linked |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

