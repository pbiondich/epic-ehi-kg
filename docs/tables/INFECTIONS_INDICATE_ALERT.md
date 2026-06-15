# INFECTIONS_INDICATE_ALERT

> This table contains information about the alerts that indicated infections.

**Primary key:** `INFECTION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK FK→ | The unique identifier for the infection record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INDICATE_ALERT_CSN_ID` | NUMERIC |  | The unique contact serial number associated with an alert that indicated the infection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

