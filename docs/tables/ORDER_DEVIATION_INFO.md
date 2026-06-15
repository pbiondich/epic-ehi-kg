# ORDER_DEVIATION_INFO

> This table stores order-level deviation information (in an oncology treatment plan context), including deviation instant, user, and change type.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEVIATION_UTC_DTTM` | DATETIME (UTC) |  | This is the instant the order deviated within a patient's oncology treatment plan. |
| 4 | `DEVIATION_USER_ID` | VARCHAR |  | This is the user who caused an order deviation within a patient's oncology treatment plan. |
| 5 | `DEVIATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

