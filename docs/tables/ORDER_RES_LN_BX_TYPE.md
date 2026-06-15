# ORDER_RES_LN_BX_TYPE

> This table stores the types of lymph nodes (sentinel or axillary) that were sampled during a surgical breast biopsy or procedure.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LN_BIOPSY_TYPE_C_NAME` | VARCHAR |  | The lymph node type category ID for the biopsied lymph nodes (such as sentinel or axillary). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

