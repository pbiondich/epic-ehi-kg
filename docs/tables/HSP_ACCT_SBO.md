# HSP_ACCT_SBO

> This table contains the balances on the hospital account (HAR). These balances are always populated for Hospital Billing HARs. They are also populated for Professional Billing HARs in service areas using the Enterprise Self-Pay platform. For legacy mixed hospital accounts the balances are the combined Hospital Billing and Professional Billing transaction balances on each HAR.

**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID with associated single billing office information. |
| 2 | `SBO_TOT_BALANCE` | NUMERIC |  | Contains the total balance of Hospital Billing (HB) or Professional Billing (PB) transactions on the hospital account, including charges, payments and adjustments in all statuses. |
| 3 | `SBO_TOTAL_CHARGES` | NUMERIC |  | Hospital Billing (HB) or Professional Billing (PB) charges on the hospital account in all statuses. |
| 4 | `SBO_TOTAL_PAYMENTS` | NUMERIC |  | Hospital Billing (HB) or Professional Billing (PB) payments on the hospital account in all statuses. |
| 5 | `SBO_TOTAL_ADJ` | NUMERIC |  | Contains Hospital Billing (HB) or Professional Billing (PB) adjustments on the hospital account in all statuses. |
| 6 | `SBO_PREBILL_BALANC` | NUMERIC |  | Contains Hospital Billing (HB) prebilled balances including charges, payments and adjustments. |
| 7 | `SBO_INS_BALANCE` | NUMERIC |  | Contains Hospital Billing (HB) or Professional Billing (PB) insurance balances including charges, payments and adjustments. |
| 8 | `SBO_UND_BALANCE` | NUMERIC |  | Contains Hospital Billing (HB) or Professional Billing (PB) undistributed balances. |
| 9 | `SBO_SP_BAL` | NUMERIC |  | Contains Hospital Billing (HB) or Professional Billing (PB) self pay balances including charges, payments and adjustments. |
| 10 | `SBO_BAD_DEBT_BAL` | NUMERIC |  | Contains Hospital Billing (HB) or Professional Billing (PB) bad debt balances including charges, payments and adjustments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

