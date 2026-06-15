# CASE_RATE_CVG

> This table contains information on the coverages related to the patient(s) involved in the case rate.

**Primary key:** `CASE_RATE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_RATE_ID` | VARCHAR | PK FK→ | The unique identifier for the case rate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage IDs for the patient(s) involved in the case rate procedures. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CASE_RATE_ID` | [CASE_RATE](CASE_RATE.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

