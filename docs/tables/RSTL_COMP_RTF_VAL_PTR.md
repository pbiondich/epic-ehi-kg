# RSTL_COMP_RTF_VAL_PTR

> This table stores the rows in table RSLT_RTF_VAL_STG with rich text results for a component.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated component value in the result. Together with VALUE_GROUP_LINE, this forms the foreign key to the RSLT_RTF_VAL_STG table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple rich text results associated with the result and result component from the RES_COMPONENTS table. |
| 4 | `VALUE_GROUP_LINE` | INTEGER |  | The line number of a portion of rich text results associated with a component in the RES_COMPONENTS table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

