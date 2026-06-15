# TXP_RETRANSPLANT_DX

> UNOS retransplant diagnosis information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for a primary retransplant diagnosis on the transplant episode. Multiple pieces of information can be associated with this record. You can use this column in conjunction with SUMMARY_BLOCK_ID to join to TXP_RETRANSPLANT_DX_RM on SUMMARY_BLOCK_ID and GROUP_LINE. |
| 3 | `RETXP_DX_ORGAN_C_NAME` | VARCHAR |  | The organ type for the associated retransplant diagnosis |
| 4 | `RETXP_PRIMARY_DX_C_NAME` | VARCHAR | org | The patient's primary retransplant diagnosis. |
| 5 | `RETXP_PRIMARY_DX_OTHR` | VARCHAR |  | The patient's free-text primary retransplant diagnosis. |
| 6 | `RETXP_SEC_DX_OTHR` | VARCHAR |  | The patient's free-text secondary retransplant diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

