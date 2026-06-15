# ADV_EVT_OUTCOME_HISTORY

> The ADV_EVT_OUTCOME_HISTORY table contains historical outcome information about adverse event records for a patient.

**Primary key:** `ADVERSE_EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the adverse event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `HX_OUTCOME_C_NAME` | VARCHAR | org | The category ID of an outcome of the adverse event at the time the adverse event was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADVERSE_EVENT_ID` | [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | sole_pk | high |

