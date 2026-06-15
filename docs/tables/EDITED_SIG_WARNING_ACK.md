# EDITED_SIG_WARNING_ACK

> Contains the overrides for the warning about this order being copied from another order with an edited sig.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDITED_SIG_WARNING_ACK_USER_ID` | VARCHAR |  | The user who acknowledged the source order edited sig. |
| 4 | `EDITED_SIG_WARNING_ACK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `EDITED_SIG_WARN_ACK_UTC_DTTM` | DATETIME (UTC) |  | The instant that the source order edited sig was acknowledged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

