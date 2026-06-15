# EPSD_JOURNEY_EVAL_REASONS

> This table stores the reasons for which episodes need to be evaluated for Care Journey creation. Episodes with reasons set in I HSB 39000 are evaluated for Care Journey creation in a scheduled job.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPSD_JRNY_EVAL_REASONS_C_NAME` | VARCHAR |  | This column stores a list of reasons for which care journey creation needs to be evaluated for this episode. Episodes with a value set here will be processed in a nightly background job. If a journey is created for this episode, all values will be cleared from this column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

