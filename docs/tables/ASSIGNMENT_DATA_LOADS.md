# ASSIGNMENT_DATA_LOADS

> This table holds information about the individual loads that have contributed specific periods of roster assignment and provider attribution.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASGN_LOAD_ID` | NUMERIC |  | The individual data loads that have contributed to this roster assignment period. |
| 4 | `ASGN_LOAD_DEMOG_ID` | NUMERIC |  | The demographic set that this assignment data was received with in the individual data load. |
| 5 | `LOAD_MESSAGE_ID` | NUMERIC |  | Holds the ID of the AMS record that most recently loaded data for a given timestamp. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

