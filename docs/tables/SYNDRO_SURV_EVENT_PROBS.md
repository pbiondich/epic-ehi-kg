# SYNDRO_SURV_EVENT_PROBS

> Contains the problems associated with syndromic surveillance events.

**Primary key:** `SYNDRO_SURV_EVENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SYNDRO_SURV_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the syndromic surveillance event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_DATE` | DATETIME |  | The date of the problem that met the syndrome criteria. |
| 4 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | The unique ID of the problem (LPL) that met the syndrome criteria. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |
| `SYNDRO_SURV_EVENT_ID` | [SYNDRO_SURV_EVENTS](SYNDRO_SURV_EVENTS.md) | sole_pk | high |

