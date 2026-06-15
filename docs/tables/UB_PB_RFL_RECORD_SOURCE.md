# UB_PB_RFL_RECORD_SOURCE

> This table holds the Professional Billing referral source search precedence category ID identifying where the source referral or auth/cert record was found when the number was found in the referral or auth/cert record.

**Primary key:** `CLAIM_PRINT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `UB_PB_RFL_RECORD_SOURCE_C_NAME` | VARCHAR |  | The Professional Billing referral source search precedence category ID identifying where the source referral or auth/cert record was found. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

