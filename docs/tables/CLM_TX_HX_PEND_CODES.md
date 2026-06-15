# CLM_TX_HX_PEND_CODES

> This table stores resolved service line-level Explanation of Benefits (EOB) codes for a given claim.

**Primary key:** `CLAIM_ID`, `PIECE`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `PIECE` | INTEGER | PK | The piece in the delimited group that the EOB code came from. |
| 3 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 4 | `LINE` | NUMERIC | PK | The line of the service line history for the EOB code. This column is commonly used to join to AP_CLM_TX_HX.LINE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

