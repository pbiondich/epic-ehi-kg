# COVERAGE_THRD_PARTY_PAYER

> This table contains Third Party Payer information about the coverage.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | The ID of the third party payer that is sponsoring the coverage |
| 4 | `NAME` | VARCHAR |  | The name of the third party payer that is sponsoring the coverage |
| 5 | `EFF_DATE` | DATETIME |  | The date the third party payer is effective for the coverage |
| 6 | `TERM_DATE` | DATETIME |  | The date the third party payer is terminated for the coverage |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

