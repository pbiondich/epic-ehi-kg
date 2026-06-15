# ACCUM_CONDITION_CODES

> This table contains condition codes on a claim when an accumulation occurred.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COND_CODES_C_NAME` | VARCHAR | org | Stores the condition codes for the claim during this accumulation event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

