# HH_EPSD_OASIS_RACE

> This table contains user-entered Outcome and Assessment Information Set (OASIS) race information for Home Health episodes.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OASIS_RACE_M0140_C_NAME` | VARCHAR |  | OASIS race category list selections for the episode. Links to category table ZC_OASIS_RACE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

