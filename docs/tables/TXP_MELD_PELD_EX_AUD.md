# TXP_MELD_PELD_EX_AUD

> This table extracts the related multiple-response Model for End-Stage Liver Disease (MELD)/Pediatric End-Stage Liver Disease (PELD) Exceptions Audit Info (I HSB 30411) item.

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
| 4 | `MELDPELD_EX_AUDIT_C_NAME` | VARCHAR | org | Stores the audit information for Model for End-Stage Liver Disease (MELD), Pediatric Model for End-Stage Liver Disease (PELD), and liver status exceptions for the transplant episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

