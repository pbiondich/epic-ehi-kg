# PROBLEM_STAGE_UPDATES

> Stores a history of changes made to the "No Stage Required" flag for problems on a patient's problem list.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_NO_STG_REASON_C_NAME` | VARCHAR | org | Stores the history of reasons that a problem was not staged. |
| 4 | `HX_NO_STG_COMMENT` | VARCHAR |  | Stores the history of comments for a problem that was not staged. |
| 5 | `HX_NO_STG_USER_ID` | VARCHAR |  | Stores the history of users that marked a problem as not needing a stage. |
| 6 | `HX_NO_STG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HX_NO_STG_DTTM` | DATETIME (UTC) |  | Stores the history of instants that a problem was marked as not needing a stage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

