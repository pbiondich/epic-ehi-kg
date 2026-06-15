# RES_RPT_COMP_RTF_CMT_PTR

> This table contains a list of lines which hold multi-line rich text user comments for a repeat component on the result from the RSLT_RTF_CMT_STG table.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the repeat of a component on the result from the RES_REPEAT_COMPONENT table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple rich text comments for the repeat of a component on the result from the RSLT_RTF_CMT_STG table. |
| 4 | `RICH_TEXT_GROUP_LINE` | INTEGER |  | The line number of a specific line of rich text comment for the repeat of a component on the result from the RSLT_RTF_CMT_STG table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

