# REHAB_PN_TRACKING

> This table stores the episode level override item for the progress note frequency in days and/or visits.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `REHAB_PN_NUM_DAYS` | INTEGER |  | Data for how often progress notes should be suggested based on a rolling calendar schedule. |
| 3 | `REHAB_PN_NUM_VISITS` | INTEGER |  | Data for how often progress notes should be suggested based on how many therapy visits have occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

