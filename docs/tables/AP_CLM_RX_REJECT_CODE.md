# AP_CLM_RX_REJECT_CODE

> This table contains information for reject codes from pharmacy claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REJ_CODE_EXT_CODE_LST_ID` | NUMERIC |  | Code indicating the error encountered. |
| 4 | `REJ_CODE_EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

