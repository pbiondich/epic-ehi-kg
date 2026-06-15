# TXP_CAS_HX

> This table contains information about a waitlisted transplant patient's lung CAS subscore over time, and the dates on which those scores were recorded.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CAS` | NUMERIC |  | The patient's lung composite allocation subscore for this transplant episode. |
| 4 | `CAS_DATE` | DATETIME |  | The date the corresponding lung composite allocation subscore was entered into UNOS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

