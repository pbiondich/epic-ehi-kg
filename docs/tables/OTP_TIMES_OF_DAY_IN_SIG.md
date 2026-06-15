# OTP_TIMES_OF_DAY_IN_SIG

> The times of day that appear in the order's patient sig. Phrases like "Morning", "Noon", "Evening", or "Bedtime".

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SIG_TIME_OF_DAY_C_NAME` | VARCHAR | org | Contains the time of day indicators used in the patient sig like "morning", "noon", "evening", or "bedtime". 1 is morning, 2 is noon, 4 is evening, and 5 is bedtime. If this contains data, then I OTP 7660 should equal 1. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

