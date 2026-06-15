# EDIT_CLM_LINES

> Stores detailed information of the edited claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EC_LINES_GEN` | INTEGER |  | Stores the generation number of the audit for each line. |
| 4 | `EC_LINES_TYPE_C_NAME` | VARCHAR | org | Stores the claim type for the claim being edited. |
| 5 | `EC_LINES_LN_NUM` | NUMERIC |  | Stores the edit claim lines line number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

