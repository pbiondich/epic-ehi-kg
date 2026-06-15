# OTP_NORWAY_PRECAUTIONS

> Norway Precautions.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRECAUTIONS_MEDICAL_COND_ID` | NUMERIC |  | Stores structured Precautions for Norway |
| 4 | `PRECAUTIONS_MEDICAL_COND_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

