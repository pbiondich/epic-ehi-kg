# MA_PREMIUM_OVERRIDE

> Medicare Advantage coverage premium override periods.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFF_DATE` | DATETIME |  | The effective date for a Medicare Advantage premium override period. |
| 4 | `TERM_DATE` | DATETIME |  | The term date for a Medicare Advantage premium override period. |
| 5 | `PREMIUM_PARTC` | NUMERIC |  | The Medicare Advantage Part C premium override effective for this period. |
| 6 | `PREMIUM_PARTD` | NUMERIC |  | The Medicare Advantage Part D premium override effective for this period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

