# CAREPLAN_CONTEXT

> This table stores the context related to a care plan.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CAREPLAN_CONTEXT_TYPE_C_NAME` | VARCHAR |  | This item stores the type of context associated with the care plan. |
| 4 | `CAREPLAN_CONTEXT_DETAIL` | VARCHAR |  | This item stores the detail for the type of context on the care plan |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

