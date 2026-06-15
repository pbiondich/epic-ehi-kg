# AP_CLAIM_SEQ_GRP_ITEMS

> This table stores the data used for claim sequencing when additional logic is necessary.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEQ_GRP_ITM_TYPE_C_NAME` | VARCHAR |  | Stores the type of value stored in I CLM 18766, to be used in claim sequencing. |
| 4 | `SEQ_GRP_ITM_CODE` | VARCHAR |  | Stores the value or code for the type stored in I CLM 18765, to be used in claim sequencing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

