# CRITERIA_REVIEW_HX

> This table contains history about guideline reviews. The records included in this table are Criteria Review Records (CRR) records.

**Primary key:** `CRITERIA_REVIEW_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the review record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_UPDATE_DTTM` | DATETIME (Local) |  | Stores history of update instants in local time zone. |
| 4 | `HX_UPDATE_USER_ID` | VARCHAR |  | Stores history of update reviewers. |
| 5 | `HX_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_UPDATE_SOURCE_C_NAME` | VARCHAR |  | Stores history of update sources. |
| 7 | `HX_CRITERIA_STATUS_C_NAME` | VARCHAR |  | Stores history of guideline status. |
| 8 | `HX_REVIEW_STATUS_C_NAME` | VARCHAR |  | Stores history of review completion status. |
| 9 | `HX_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Stores history of update instants in UTC time zone. |
| 10 | `HX_NOTE_ID` | VARCHAR |  | Stores history of associated notes. |
| 11 | `HX_ANSWER_ID` | VARCHAR |  | Stores history of associated answers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CRITERIA_REVIEW_ID` | [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | sole_pk | high |

