# ESC_EPISODE_SDOH_ADDR

> Represents SDOH domains at the episode level.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RELATED_SDOH_ADDRESSED_C_NAME` | VARCHAR | org | The Social Drivers of Health domain category ID for the episode |
| 4 | `RELATED_SDOH_METRIC_STATUS_C_NAME` | VARCHAR |  | The status category ID for the Social Drivers of Health domain. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

