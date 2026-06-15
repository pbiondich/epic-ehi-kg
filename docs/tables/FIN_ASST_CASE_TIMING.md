# FIN_ASST_CASE_TIMING

> This table contains durations of time users have had the case navigator open, a case selected in the summary, or visible in case history.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOGGED_UTC_DTTM` | DATETIME (UTC) |  | This stores the instant that a timing duration was recorded. |
| 4 | `LOGGED_USER_ID` | VARCHAR |  | This stores the user that a timing duration was recorded for. |
| 5 | `LOGGED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DURATION` | INTEGER |  | This stores a duration, in seconds, that a user accessed a case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

