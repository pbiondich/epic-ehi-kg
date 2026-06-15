# OTP_INFO_5

> This table contains additional information about patient order templates.

**Overflow of:** [OTP_INFO](OTP_INFO.md)  
**Primary key:** `OTP_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The unique identifier (.1 item) for the patient order template record. |
| 2 | `OMT_ORDER_YN` | VARCHAR |  | Only used in Norway currently. The term used in Norway for this treatment is 'LAR'. This item stores Yes if the order is for such treatment. |
| 3 | `PA_PRIORITY_C_NAME` | VARCHAR |  | The prior authorization priority category ID for the most recent medication prior authorization request for a medication order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [OTP_INFO](OTP_INFO.md).

