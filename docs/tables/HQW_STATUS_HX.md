# HQW_STATUS_HX

> This table stores information on record status of a questionnaire series answer.

**Primary key:** `SERIES_ANS_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK FK→ | The unique identifier for the questionnaire series answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_INST_DTTM` | DATETIME (UTC) |  | Stores the instant when the record status was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | Stores the user who changed the record status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | Stores the action that was applied to the record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

