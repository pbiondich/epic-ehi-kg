# PROBLEM_TREAT_SUMM_AUDIT

> This table stores treatment summary audit information for a problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_SUMM_AUDIT_USER_ID` | VARCHAR |  | The user who marked a problem as needing or not needing treatment summary. |
| 4 | `TX_SUMM_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `TX_SUMM_AUDIT_DTTM` | DATETIME (UTC) |  | The UTC instant when a problem is marked as needing or not needing treatment summary. |
| 6 | `TX_SUMM_ACTION_C_NAME` | VARCHAR |  | The category value of audit action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

