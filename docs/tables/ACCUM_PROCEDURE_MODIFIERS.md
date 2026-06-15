# ACCUM_PROCEDURE_MODIFIERS

> This table stores procedure modifiers on a claim when an accumulation occurred.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INT_MODIFIER_ID` | VARCHAR |  | Stores the procedure modifiers for the service matched to during this accumulation event. |
| 4 | `INT_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

