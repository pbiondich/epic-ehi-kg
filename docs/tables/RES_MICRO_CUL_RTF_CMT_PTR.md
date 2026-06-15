# RES_MICRO_CUL_RTF_CMT_PTR

> This table containers a list of lines for rich text comments for culture isolates on the result from the RSLT_RTF_CMT_STG table.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for a culture isolate on the result from the RES_MICRO_CULTURE table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple rich text comments for a culture isolate on the result from the RSLT_RTF_CMT_STG table. |
| 4 | `COMMENT_GROUP_LINE` | INTEGER |  | The line number of a group of rich text comments for a culture isolate on the result from the RSLT_RTF_CMT_STG table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

