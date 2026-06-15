# AUTH_FULL_REFERRAL

> This table holds the full list of referral and authorization records available for consideration when determining the prior authorization and referral numbers for the claim. This may include records that were not referenced in the lookup because the authorization number was found earlier in the list or from another source.

**Primary key:** `CLAIM_PRINT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUTH_FULL_REFERRAL_ID` | NUMERIC |  | The unique ID of every referral or auth/cert record considered in the authorization number lookup, whether we read the authorization number from the record or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

