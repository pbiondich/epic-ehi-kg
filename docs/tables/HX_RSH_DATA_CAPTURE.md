# HX_RSH_DATA_CAPTURE

> The HX_RSH_DATA_CAPTURE table contains information about updates to research data capture forms.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_USER_ID` | VARCHAR |  | A history of the unique IDs of users who have updated this form. |
| 4 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | A history of instants in which this form has been updated. |
| 6 | `FORM_STAT_C_NAME` | VARCHAR |  | A history of status category IDs for this form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

