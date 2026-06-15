# RSLT_COMP_RCHTXT

> This table contains a a list of lines which hold multi-line rich text comments for components on the result.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for a component on the result from the RES_COMPONENTS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple rich text comments for a component on the result from the RSLT_RTF_CMT_STG table. |
| 4 | `RCH_TEXT_GROUP_LINE` | INTEGER |  | The line number of a specific group of rich text comments for a component on the result from the RSLT_RTF_CMT_STG table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

