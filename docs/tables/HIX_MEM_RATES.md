# HIX_MEM_RATES

> The HIX_MEM_RATES table contains information about the individual member premium for an exchange coverage. The table includes the effective date, premium rate, and the member ID.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HIX_MEM_EFF_DATE` | DATETIME |  | The effective date of the member's premium rate |
| 4 | `HIX_MEM_PREMIUM` | NUMERIC |  | The individually rated premium rate amount for each member on an exchange coverage |
| 5 | `HIX_MEM_ID` | VARCHAR |  | Stores the member's internal ID in an exchange coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

