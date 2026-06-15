# ACCUM_NON_C2C_LIMIT_TYPES

> This table contains the limit types to which the accumulation will not carry during a mid year coverage transfer that results in accumulation carryover. For example, a copay accumulation with 4 (Deductible) in the NON_CARRYOVER_BEN_FUNCTION_C column does not carry the accumulation amount into the new coverage's deductible accumulator.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NON_CARRYOVER_BEN_FUNCTION_C_NAME` | VARCHAR | org | The list of phases that this ACC is not allowed to carry into |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

