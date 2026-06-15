# AP_CLAIM_HLTH_ERR

> This table contains information about the healthcare works errors in the claims information database.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HWRKS_ERR_TYPE_C_NAME` | VARCHAR |  | Healthworks error type. |
| 4 | `HWRKS_ERR_CODES` | VARCHAR |  | Healthworks error codes. |
| 5 | `HWRKS_ERROR_MSG` | VARCHAR |  | Healthworks error messages. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

