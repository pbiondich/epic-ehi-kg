# AUT_ONC_EXP_REQCOUNT

> The AUT_ONC_EXP_REQCOUNT table contains data about requested counts defaulting from treatment plans. The items here are stamps and live items to compare what the system thinks the value should be versus what users have inputted.

**Primary key:** `AUTH_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization record. |
| 2 | `NUM_SVCS_APPROVED` | INTEGER |  | The number of services or units approved by the payor. |
| 3 | `NUM_SVCS_REQUESTED` | INTEGER |  | The number of services or units requested. |
| 4 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage associated with the authorization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

