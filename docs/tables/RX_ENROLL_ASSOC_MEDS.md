# RX_ENROLL_ASSOC_MEDS

> This table contains a list of generic medications (MDL) that were associated with the Coordinated Care Management episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOC_MED_PRBLM_LIST_ID` | NUMERIC |  | The current generic medications associated with this Coordinated Care Management episode |
| 4 | `ASSOC_MED_PRIM_OR_OTHR_C_NAME` | VARCHAR |  | Whether the current generic medications associated with this Coordinated Care Management episode are primary or other |
| 5 | `ASSOC_MED_THERAPY_START_DATE` | DATETIME |  | The therapy start dates for the current generic medications associated with this Coordinated Care Management episode |
| 6 | `ASSOC_MED_THERAPY_END_DATE` | DATETIME |  | The therapy end dates for the current generic medications associated with this Coordinated Care Management episode |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

