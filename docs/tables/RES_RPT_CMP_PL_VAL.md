# RES_RPT_CMP_PL_VAL

> This table displays the values of the components used in the equation of the repeat component.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated repeat result component in the result record. Together with RESULT_ID, this forms the foreign key to the RES_REPEAT_COMP table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values of the pulled repeat component used in equations for a repeat result from the RES_REPEAT_COMP table. |
| 4 | `REPEAT_PULL_VALUE` | VARCHAR |  | These are the values of the components used in the equation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

