# CL_OTP_FST_LST_SCH

> Date and time of the first and last scheduled occurrences of an order template.

**Primary key:** `OTP_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `DATE_FIRST_SCHEDUL` | VARCHAR |  | The first scheduled date of the order template in this record. |
| 3 | `TIME_FIRST_SCHEDUL` | DATETIME (Local) |  | The first scheduled time of the order template in this record. |
| 4 | `DATE_LAST_SCHEDULE` | VARCHAR |  | The last scheduled date of the order template in this record. |
| 5 | `TIME_LAST_SCHEDULE` | DATETIME |  | The last scheduled time of the order template in this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

