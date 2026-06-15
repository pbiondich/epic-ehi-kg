# RAD_THP_TREATMENT_SITE

> Contains the list of treatment sites and corresponding lateralities for an episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TREATMENT_SITE_C_NAME` | VARCHAR |  | Contains the treatment site that will be treated. |
| 4 | `LATERALITY_C_NAME` | VARCHAR |  | Contains the laterality of the corresponding treatment site. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

