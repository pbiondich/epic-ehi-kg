# CVG_Q4_CARRYOVER

> This table holds data regarding exceeded limits during carryover.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique ID of the Coverage. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `Q4CO_EXC_CMB_ID` | NUMERIC |  | Stores the bucket ID for which carryover exceeded the limit |
| 4 | `Q4CO_EXC_CMB_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 5 | `Q4CO_EXC_ROLL_PD` | VARCHAR |  | Stores the roll period for which carryover exceeded the limit |
| 6 | `Q4CO_EXC_EPT_ID` | VARCHAR |  | Stores patient ID when limit exceeded by Q4 carryover |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

