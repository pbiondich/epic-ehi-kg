# ARPB_TX_MEA

> This tables stores the MEA test-related information.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. This represents a single charge procedure on the transaction record. |
| 3 | `MEA_TEST_C_NAME` | VARCHAR | org | The measurement qualifier category ID for Mouse Embryo Assay (MEA) test associated to the transaction. |
| 4 | `MEA_RESULT` | NUMERIC |  | Th measurement value. |
| 5 | `MEA_DATE` | DATETIME |  | The date on which the measurement is taken. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

