# RES_COMPONENT_LRR

> This table contains discrete, component-based information and findings for this result.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID assigned to the result (RES .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `RESULT_VALUE` | VARCHAR |  | The value for the associated result component row. |
| 4 | `RESULT_UNITS` | VARCHAR |  | The units for the associated result component row. |
| 5 | `RESULT_COMMENT` | VARCHAR |  | The comment for the associated result component row. |
| 6 | `OB_UTZ_RANK_SRC_C_NAME` | NUMERIC |  | The ultrasound rank source category ID for the fetus' associated result component row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

