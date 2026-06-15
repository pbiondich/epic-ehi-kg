# BMT_INFUSIONS

> Table of blood and marrow transplant infusion information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSCT_TYPE_C_NAME` | VARCHAR | org | Type of blood and marrow transplant. |
| 4 | `BMT_SOURCE_C_NAME` | VARCHAR | org | Blood and marrow transplant source material. |
| 5 | `BMT_INFUSION_DT` | DATETIME |  | Blood and marrow transplant infusion dates. |
| 6 | `BMT_IS_TANDEM_YN` | VARCHAR |  | Stores if the infusion is part of a blood and marrow tandem transplant. |
| 7 | `BMT_INF_COMMENTS` | VARCHAR |  | Blood and marrow infusion comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

