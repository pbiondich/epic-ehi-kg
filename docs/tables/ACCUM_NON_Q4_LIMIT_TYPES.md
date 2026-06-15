# ACCUM_NON_Q4_LIMIT_TYPES

> This table contains the limit types to which the accumulation will not carry in the new plan year via fourth quarter carryover. For example, a copay accumulation with 2 (Maximum Out of Pocket) in the NON_CARRYOVER_BEN_FUNCTION_C column does not carry the accumulation amount into the new plan year's maximum out of pocket accumulator.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NON_Q4_BEN_FUNCTION_C_NAME` | VARCHAR | org | This item lists the phases that the ACC cannot Q4 carry into. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

