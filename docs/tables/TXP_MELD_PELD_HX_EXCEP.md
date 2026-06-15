# TXP_MELD_PELD_HX_EXCEP

> This table extracts the related multiple-response Model for End-Stage Liver Disease (MELD)/Pediatric End-Stage Liver Disease (PELD) Exceptions (I HSB 30404) item.

**Primary key:** `SUMMARY_BLOCK_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `MELD_PELD_EXCEPTS_C_NAME` | VARCHAR | org | The exceptions provided for the corresponding Model for End-Stage Liver Disease (MELD) score, Pediatric Model for End-Stage Liver Disease (PELD) score, or liver status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

