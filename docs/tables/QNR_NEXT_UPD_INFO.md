# QNR_NEXT_UPD_INFO

> Table to store the next update dates, actions and occurrences remaining for a questionnaire in the questionnaire series answer record.

**Primary key:** `SERIES_ANS_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK FK→ | The unique ID of the Series Answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QNR_NEXT_UPD_DATE` | DATETIME |  | The date on which the next time this Series Answer record is updated |
| 4 | `QNR_NXT_UPD_ACT_C_NAME` | VARCHAR |  | The action that will occur the next time this Series Answer record is updated |
| 5 | `QNR_NEXT_UPD_LINE` | INTEGER |  | This column stores the questionnaire ID corresponding to the next update date. |
| 6 | `QNR_OCCUR_REMAINING` | INTEGER |  | This item stores the number of occurrences remaining for the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

