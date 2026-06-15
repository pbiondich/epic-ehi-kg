# DOCS_RCVD_TXP_SCORE

> Cosmos longitudinal patient score data related to a patient's transplant episode.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TXP_SCORE_REF_IDENT` | VARCHAR |  | Unique id representing a longitudinal patient score asscociated with a transplant episode |
| 2 | `TXP_EPISODE_REF_IDENT` | VARCHAR |  | Transplant episode reference ID corresponding to the score being calculated |
| 3 | `TXP_SCORE` | VARCHAR |  | A transplant score value |
| 4 | `TXP_SCORE_NAME` | VARCHAR |  | The name of the type of score being calculated |
| 5 | `TXP_SCORE_DATE` | DATETIME |  | The anchor date at which a score was calculated |
| 6 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 7 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 8 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

