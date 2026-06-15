# REJECT_TREAT

> Table of treatments done to treat a rejection problem

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique ID of this Problem List entry. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REJECT_TREAT_C_NAME` | VARCHAR | org | List of treatments for a rejection problem |
| 4 | `REJECT_TX_START_DT` | DATETIME |  | Rejection treatment start date |
| 5 | `REJECT_TX_END_DT` | DATETIME |  | Rejection treatment end date |
| 6 | `REJECT_TX_START_TM` | DATETIME (Local) |  | Rejection treatment start time |
| 7 | `REJECT_TX_END_TM` | DATETIME (Local) |  | Rejection treatment end time |
| 8 | `REJECTION_COMMENTS` | VARCHAR |  | Comments about the rejection treatment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

