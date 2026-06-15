# CLAIM_SCRB_HX

> Stores claim scrubber history information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_SCRB_HX_ACTV_C_NAME` | VARCHAR |  | Store claim scrubber activity history. |
| 4 | `CLM_SCRB_HX_REQ_ID` | VARCHAR |  | Store claim scrubber history request ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

