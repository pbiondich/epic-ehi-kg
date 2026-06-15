# CVG_ALT_ADDR

> The alternate street address for this coverage. This may be the address that claims are sent to.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | Corresponds to the address line number for a coverage. |
| 3 | `ALTR_ADDR` | VARCHAR |  | Alternate coverage street address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

