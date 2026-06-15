# BMT_HLA_MATCHING

> This is a table of donor human leukocyte antigen (HLA) matching information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BMT_HLA_MATCH_TYPE_C_NAME` | VARCHAR | org | The specific human leukocyte antigen type for matching between a blood and marrow transplant donor and recipient. |
| 4 | `BMT_HLA_MATCH_VAL` | INTEGER |  | The graft-versus-host match value for a specific human leukocyte antigen type between a blood and marrow transplant donor and recipient. |
| 5 | `HVG_MATCH_VAL` | INTEGER |  | The host-versus-graft match value for a specific human leukocyte antigen type between a blood and marrow transplant donor and recipient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

