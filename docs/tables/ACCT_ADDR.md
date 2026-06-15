# ACCT_ADDR

> This table contains one row for each line of the billing address of a guarantor account.

**Primary key:** `ACCOUNT_ID`, `ADDRESS_LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the guarantor record. This column is frequently used to link to the ACCOUNT table |
| 2 | `ADDRESS_LINE` | INTEGER | PK | The line number for the guarantor billing address. This line number represents a single line of a guarantor's billing address. |
| 3 | `ADDRESS` | VARCHAR |  | This represents the guarantor's street address. Each ACCOUNT_ID value represents a different guarantor account and each ADDRESS_LINE value represents a different line of that guarantor's address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

