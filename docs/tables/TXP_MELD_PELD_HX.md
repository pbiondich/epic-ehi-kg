# TXP_MELD_PELD_HX

> This table contains the liver score history for a transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MELD_SCORE` | INTEGER |  | The patient's Model for End-Stage Liver Disease (MELD) score for this transplant episode. |
| 4 | `PELD_SCORE` | INTEGER |  | The patient's Pediatric Model for End-Stage Liver Disease (PELD) score for the transplant episode. |
| 5 | `MELD_DATE` | DATETIME |  | The date the corresponding Model for End-Stage Liver Disease (MELD) value or liver status was last updated for the transplant episode. |
| 6 | `PELD_DATE` | DATETIME |  | The date the corresponding Pediatric Model for End-Stage Liver Disease (PELD) value or liver status was last updated for the transplant episode. |
| 7 | `MELD_PELD_OTHER_EX` | VARCHAR |  | The free-text exception for the corresponding Model for End-Stage Liver Disease (MELD) score, Pediatric Model for End-Stage Liver Disease (PELD) score, or liver status for the transplant episode. |
| 8 | `LIVER_STATUS_C_NAME` | VARCHAR |  | The liver status that has been entered in the United Network of Organ Sharing (UNOS) instead of a Model for End-Stage Liver Disease (MELD) or Pediatric Model for End-Stage Liver Disease (PELD) score for the transplant episode. |
| 9 | `MELD_MTS_OFFSET` | INTEGER |  | The patient's MELD relative to a median for this transplant episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

