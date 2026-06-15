# REJECT_TREAT_HX

> History of changes to treatments for a rejection problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique ID of this Problem List entry. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REJECT_TREAT_HX_C_NAME` | VARCHAR | org | History of changes to the rejection treatments. |
| 4 | `REJECT_TREAT_INST` | DATETIME (Local) |  | Instant the rejection treatment was changed. |
| 5 | `REJECT_TREAT_WHO_ID` | VARCHAR |  | User who changed the rejection treatment |
| 6 | `REJECT_TREAT_WHO_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `REJECT_HX_START_DT` | DATETIME |  | Rejection treatments start date |
| 8 | `REJECT_HX_END_DT` | DATETIME |  | Rejection treatments end date |
| 9 | `REJECT_HX_START_TM` | DATETIME (Local) |  | Rejection treatment start time |
| 10 | `REJECT_HX_END_TM` | DATETIME (Local) |  | Rejection treatment end time |
| 11 | `REJECT_HX_COMMENTS` | VARCHAR |  | Rejection treatments comments |
| 12 | `REJECT_HX_UPD_TYPE_C_NAME` | VARCHAR |  | The update type for the rejection treatment related group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

