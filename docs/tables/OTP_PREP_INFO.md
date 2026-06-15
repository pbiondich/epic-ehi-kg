# OTP_PREP_INFO

> Stores information about Beacon treatment plan preparation orders.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOT_NUMBER` | VARCHAR |  | Stores the lot numbers that have been used to prepare this patient order template. |
| 4 | `PREP_DTTM_DTTM` | DATETIME (UTC) |  | Stores the planned time when this order will be prepared. |
| 5 | `PREP_ORDER_ID` | NUMERIC |  | Points to the order that was generated for preparation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

