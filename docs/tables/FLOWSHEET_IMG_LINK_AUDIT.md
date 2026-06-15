# FLOWSHEET_IMG_LINK_AUDIT

> This table contains information about Document (DCS) records that represent images that are linked to flowsheets documentation in the audit trail.

**Primary key:** `ID_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ID_ID` | VARCHAR | PK | The unique identifier for the flowsheet data record record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUDIT_DOC_INFO_ID` | VARCHAR |  | Audit trail for item that stores image links for image type rows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

