# AP_CLAIM_VAL_PROG_ADJ

> This table contains the payment adjustments from value-based programs for AP Claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPUTED_PROGRAM_ADJ` | NUMERIC |  | The value-based program adjustment amount for the claim, as computed by the system. |
| 4 | `OVERRIDE_PROGRAM_ADJ` | NUMERIC |  | The value-based program adjustment amount for the claim, as overridden by a user. |
| 5 | `PROGRAM_ADJ_COMMENT` | VARCHAR |  | The value-based program payment adjustment comment entered by the system when calculating the adjustment or by a user when overriding the adjustment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

