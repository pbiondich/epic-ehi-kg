# ACCT_COVERAGE

> This table contains coverage lists for every accounts receivable (EAR) record.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique account record ID. This ID number may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | Line number to identify the status information within the account. |
| 3 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID for the guarantor record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

