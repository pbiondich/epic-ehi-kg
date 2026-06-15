# CLP_COND_CODE

> This table extracts the condition codes printed on a claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim print record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `CONDITION_CODE_C_NAME` | VARCHAR | org | Condition Code to print on claims |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

