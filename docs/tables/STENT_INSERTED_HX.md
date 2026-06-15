# STENT_INSERTED_HX

> This table contains the history of changes to whether or not a stent was inserted for a related problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STENT_HX_YN` | VARCHAR |  | Indicates the history of whether or not a stent was inserted due to a bronchial stricture. |
| 4 | `STENT_INSERTED_DTTM` | DATETIME (Local) |  | Instant at which a change was made to the stent inserted question. |
| 5 | `STENT_WHO_ID` | VARCHAR |  | Who changed the stent inserted question. |
| 6 | `STENT_WHO_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

