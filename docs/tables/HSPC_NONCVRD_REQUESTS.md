# HSPC_NONCVRD_REQUESTS

> Requests for a patient's Hospice Non-Covered Documentation.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSPC_NONCVRD_REQ_C_NAME` | VARCHAR | org | The hospice non-covered request type category ID for the episode. |
| 4 | `HSPC_NONCVRD_ROI_ID` | VARCHAR |  | The unique ID of the release of information record associated with the hospice non-covered request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

