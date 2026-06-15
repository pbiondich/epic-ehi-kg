# RES_SCAN_FILES

> This table contains result entry scan files information.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_DOC_INFO_ID` | VARCHAR |  | Stores document (DCS) IDs associated with the scans on the result record. |
| 4 | `RES_DOC_RPTD_YN_NAME` | VARCHAR |  | Stores a category ID indicating whether the document (DCS) was reported to chart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

