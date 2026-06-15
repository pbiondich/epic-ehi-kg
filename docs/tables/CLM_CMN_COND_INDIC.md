# CLM_CMN_COND_INDIC

> Condition indicator for External Infusion Pump Certificate of Medical Necessity (CMN) form. Code to print in the CRC-03 segment.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CMN_COND_INDIC_C_NAME` | VARCHAR |  | Condition indicator for the External Infusion Pump Certificate of Medical Necessity (CMN) form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

