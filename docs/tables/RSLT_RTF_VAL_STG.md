# RSLT_RTF_VAL_STG

> This table containers a list of rich text values for a component on the result.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for a group of rich text values for a component on the result from the tables RSTL_COMP_RTF_VAL_PTR or RSLT_REPEAT_RTF_VAL_PTR. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number for one line of rich text values for a component on the result from the tables RSTL_COMP_RTF_VAL_PTR or RSLT_REPEAT_RTF_VAL_PTR. |
| 4 | `RICH_TEXT` | VARCHAR |  | The rich text values for a component on the result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

