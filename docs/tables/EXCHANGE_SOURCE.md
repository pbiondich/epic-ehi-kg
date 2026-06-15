# EXCHANGE_SOURCE

> This table include information about the source exchange ID and its effective date.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_EXCHANGE_ID` | VARCHAR |  | The ID of the Source Exchange |
| 4 | `SOURCE_EXCHANGE_EFF_FROM_DT` | DATETIME |  | The effective date of the Source Exchange ID |
| 5 | `SOURCE_STATE_EXCHANGE_C_NAME` | VARCHAR | org | The source exchange category ID for the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

