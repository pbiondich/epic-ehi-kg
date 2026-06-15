# MA_PREMIUM_LIS

> Stores Medicare Advantage (MA) Low Income Subsidies (LIS) and their effective periods.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFF_DATE` | DATETIME |  | The effective date for a Low Income Subsidy (LIS) period. |
| 4 | `TERM_DATE` | DATETIME |  | The term date for a Low Income Subsidy (LIS) period. |
| 5 | `LIS_PERCENTAGE` | INTEGER |  | The Part D Low Income Premium Subsidy (LIPS) for an LIS period. |
| 6 | `LIS_CODE_C_NAME` | VARCHAR |  | This item stores the Low Income Source Code (Applicant or Deemed). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

