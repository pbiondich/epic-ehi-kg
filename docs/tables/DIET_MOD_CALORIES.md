# DIET_MOD_CALORIES

> Diet modifier calories table.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DIET_MOD_CALORIES_C_NAME` | VARCHAR | org | The diet calorie modifier category ID associated with the order record for this row. |
| 4 | `DIET_CALORIES_CMT` | VARCHAR |  | The comment associated with the diet calorie modifier for this row. |
| 5 | `DIET_CAL_QST_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

