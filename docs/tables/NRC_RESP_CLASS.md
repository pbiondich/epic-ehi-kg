# NRC_RESP_CLASS

> This table contains information about responsibility classes.

**Primary key:** `RESP_CLASS_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESP_CLASS_ID` | NUMERIC | PK | The unique identifier for the responsibility class record. |
| 2 | `RESP_CLASS_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CLAIM_FEE_DETAILS](CLAIM_FEE_DETAILS.md) | `RESP_CLASS_ID` | high |

