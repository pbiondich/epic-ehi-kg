# CVG_RIDERS

> Table contains the Riders information in the Insurance Coverage Database.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RIDER_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 4 | `RIDERS_SELECTED_C_NAME` | VARCHAR |  | Riders that have been selected. |
| 5 | `RIDER_EFF_DATE` | DATETIME |  | Date when the rider becomes effective |
| 6 | `RIDER_TERM_DATE` | DATETIME |  | Date when the rider is no longer effective |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

