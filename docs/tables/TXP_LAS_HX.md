# TXP_LAS_HX

> This table contains the lung allocation score information for a transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAS` | NUMERIC |  | The patient's lung allocation score for this transplant episode. |
| 4 | `LAS_DATE` | DATETIME |  | Date on which the patient's lung allocation score was last updated. |
| 5 | `LAS_EXCEPTION_OTHER` | VARCHAR |  | Free-text exception for the corresponding lung allocation score. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

