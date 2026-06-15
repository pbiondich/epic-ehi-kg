# MPI_LPL_ID

> Active MPI ID table.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | The ID Type (IIT) ID of the identifier. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID_NUM` | VARCHAR |  | The record's assigned identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

