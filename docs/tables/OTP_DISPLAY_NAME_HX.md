# OTP_DISPLAY_NAME_HX

> This table contains columns for the Display Name - History (I OTP 81000) and Display Name Instant - History (I OTP 81001) items.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_INSTANT_DTTM_DTTM` | DATETIME (UTC) |  | Stores the instant that the corresponding display name history line applies to. |
| 4 | `OTP_DISPLAY_NAME_HX` | VARCHAR |  | Stores the history of the order display name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

