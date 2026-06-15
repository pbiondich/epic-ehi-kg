# PROC_INFO_SECTION_AUD

> This table holds the procedure information navigator section audit information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_AUD_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `AN_AUD_PROC_DATE` | DATETIME |  | Contains audit trail information on procedure date. |
| 5 | `AN_AUD_PROC_PRE_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `AN_AUD_PROC_TIME` | DATETIME (Local) |  | Contains audit trail information on procedure time. |
| 7 | `AN_AUD_PROC_COMMENT` | VARCHAR |  | Contains audit trail information on procedure comment. |
| 8 | `AN_AUD_PROC_USER_ID` | VARCHAR |  | Contains audit trail information on documenting user. |
| 9 | `AN_AUD_PROC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `AN_AUD_PROC_EDITED_UTC_DTTM` | DATETIME (UTC) |  | Contains audit trail information on when procedure information was edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

