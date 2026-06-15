# HX_EXTERNAL_DEMOG_SETS

> A list of all external demographic sets (REQs) that this compiled assignment has been associated with.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_EXTERNAL_DEMOG_ID` | NUMERIC |  | The unique IDs of the External Demographic Sets that have been associated with this assignment data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

