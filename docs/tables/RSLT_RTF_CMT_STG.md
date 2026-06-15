# RSLT_RTF_CMT_STG

> This table contains a list of rich text user comments for a component or a culture isolate on the result.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for a group of rich text user comments for a component or a culture isolate on the result from the tables RSLT_COMP_RCHTXT, RSLT_REPEAT_RTF_VAL_PTR or RES_MICRO_CUL_RTF_CMT_PTR. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number for one line of rich text user comments for a component or a culture isolate on the result from the tables RSLT_COMP_RCHTXT, RSLT_REPEAT_RTF_VAL_PTR or RES_MICRO_CUL_RTF_CMT_PTR. |
| 4 | `RICH_TEXT` | VARCHAR |  | The rich text user comments for a component or a culture isolate on the result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

