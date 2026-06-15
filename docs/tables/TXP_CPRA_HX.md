# TXP_CPRA_HX

> This table contains the calculated Panel Reactive Antibodies (PRA) data for a transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CPRA` | INTEGER |  | The patient's Calculated Panel Reactive Antibodies (CPRA) score history for this transplant episode. |
| 4 | `CPRA_DATE` | DATETIME |  | The effective date of the corresponding Calculated Panel Reactive Antibodies (CPRA) score. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

