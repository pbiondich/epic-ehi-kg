# TXP_INTESTINE_STATUS_HX

> This table contains the intestine status information for a transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INTESTINE_STATUS_C_NAME` | VARCHAR | org | The patient's intestine status as defined by the United Network of Organ Sharing (UNOS). |
| 4 | `INTESTINE_STATUS_DT` | DATETIME |  | The date the corresponding intestine status was last updated for the transplant episode. |
| 5 | `IN_ST_RSN_OTHER` | VARCHAR |  | The free-text reason for the patient's intestine status for the transplant episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

