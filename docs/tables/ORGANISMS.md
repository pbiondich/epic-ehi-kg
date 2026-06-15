# ORGANISMS

> Organisms that caused an infection problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique ID of this Problem List entry. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this contact. |
| 3 | `ORGANISMS_ID` | NUMERIC |  | List of organism records that caused the infection problem. |
| 4 | `ORGANISMS_ID_NAME` | VARCHAR |  | The name of the organism. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

