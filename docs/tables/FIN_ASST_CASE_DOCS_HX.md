# FIN_ASST_CASE_DOCS_HX

> This Clarity table contains changes made to FA case documents.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOCS_HX_INSTANT_DTTM` | DATETIME (UTC) |  | The instant when the document was changed |
| 4 | `DOCS_HX_USER_ID` | VARCHAR |  | The unique ID of the user who modified the document |
| 5 | `DOCS_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DOCS_HX_DOCUMENT_ID` | VARCHAR |  | The unique ID of the document that was changed |
| 7 | `DOCS_HX_DOC_INFO_TYPE_C_NAME` | VARCHAR | org | The display name of the document type |
| 8 | `DOCS_HX_ACTION_C_NAME` | VARCHAR |  | The action category ID that was taken on the document. |
| 9 | `DOCS_HX_INSTANT_LOCAL_DTTM` | DATETIME (Local) |  | Local instant when a document attached to the case was changed. Uses the time zone of the case's primary service area |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

