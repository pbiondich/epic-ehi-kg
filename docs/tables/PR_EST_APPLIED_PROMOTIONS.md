# PR_EST_APPLIED_PROMOTIONS

> This table extracts the related multiple response Applied Promotion Discount Amount (I PES 1008) item.

**Primary key:** `ESTIMATE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number corresponding to the promotion record. This promotion record can be looked up by referencing this line number in PR_EST_PROMOTION_INFO. |
| 4 | `APPLIED_PROMO_DISCOUNT_AMT` | NUMERIC |  | The applied promotion discount amount per promotion record on the estimate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

