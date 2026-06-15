# UB_AUTH_NUM_SOURCE

> This table holds the authorization number source category indicating where the prior authorization or referral number for the UB (or institutional) claim service line was found.

**Primary key:** `CLAIM_PRINT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `UB_AUTH_NUM_SOURCE_C_NAME` | VARCHAR |  | The auth number search precedence category ID identifying where the authorization number was found. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

