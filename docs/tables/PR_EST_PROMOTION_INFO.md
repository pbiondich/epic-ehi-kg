# PR_EST_PROMOTION_INFO

> This table extracts promotion-related information that is present in the estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROMOTION_ID` | NUMERIC | FK→ | The promotion records applied to the estimate. |
| 4 | `PROMOTION_ID_PROMOTION_NAME` | VARCHAR |  | The promotion record name. |
| 5 | `DISCOUNT_AMOUNT` | NUMERIC |  | The flat discount amount associated with the promotion record at the time the promotion was added to the estimate. |
| 6 | `DISCOUNT_PERCENT` | NUMERIC |  | The promotion discount percent at the time the promotion was applied to the estimate. |
| 7 | `OVERRIDE_DISCOUNT_AMOUNT` | NUMERIC |  | The promotion discount amount if overridden by the user. |
| 8 | `OVERRIDE_DISCOUNT_PERCENT` | NUMERIC |  | The discount percent amount if it was overridden by the user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROMOTION_ID` | [PMC_INFO](PMC_INFO.md) | sole_pk | high |

