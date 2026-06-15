# HSP_TX_MEA_TESTS

> Related group information for MEA items.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `MEA_TEST_C_NAME` | VARCHAR | org | Lab test name. |
| 4 | `MEA_RESULT` | NUMERIC |  | Lab result value. |
| 5 | `MEA_PERFORMED_DATE` | DATETIME |  | Date the lab test was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

