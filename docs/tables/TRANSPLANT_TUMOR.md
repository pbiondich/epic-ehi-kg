# TRANSPLANT_TUMOR

> Table of incidental tumors found on the removed organ at the time of transplant.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECIP_REMOV_ORGN_ID` | NUMERIC |  | The ID of the transplant recipient's removed organ, where the incidental tumor was found at time of transplant. |
| 4 | `RECIP_REMOV_ORGN_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 5 | `TXP_TUMOR_C_NAME` | VARCHAR |  | The type of incidental tumor found in the transplant recipient's removed organ. |
| 6 | `TXP_TUMOR_OTHER` | VARCHAR |  | Type of tumor found in the transplant recipient's removed organ. This is stored as free text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

