# CLP_VALUE_DATA

> This table extracts the value codes and value amounts printed on institutional claims.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim print record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `VALUE_CODE_C_NAME` | VARCHAR | org | Stores Value Code to print on institutional claims |
| 4 | `VALUE_AMT` | VARCHAR |  | Value Remark to print on institutional claims |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

