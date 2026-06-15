# TXP_HEART_STATUS_HX

> This table contains the heart status information for a transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HEART_STATUS_C_NAME` | VARCHAR | org | Patient's heart status value as defined by the United Network for Organ Sharing (UNOS). |
| 4 | `HEART_STATUS_DT` | DATETIME |  | Date on which the patient's heart status value was last updated. |
| 5 | `HR_ST_RSN_OTHER` | VARCHAR |  | Free-text reason for the patient's heart status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

