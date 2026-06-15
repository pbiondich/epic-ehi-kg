# TXP_RETRANSPLANT_DX_RM

> This table extracts the related multiple-response Secondary Re-transplant Diagnosis (I HSB 30553) item.

**Primary key:** `SUMMARY_BLOCK_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the primary retransplant diagnosis associated with a secondary retransplant diagnosis category on the transplant episode. You can use this column in conjunction with SUMMARY_BLOCK_ID to join to TXP_RETRANSPLANT_DX on SUMMARY_BLOCK_ID and LINE. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `RETXP_SEC_DX_C_NAME` | VARCHAR | org | The patient's secondary retransplant diagnoses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

