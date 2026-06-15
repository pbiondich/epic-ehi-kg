# HSP_ACCT_BILL_DRG

> This table contains billing diagnosis related group (DRG) information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID with associated billing DRG information. |
| 2 | `BL_DRG_COND_CODE` | NUMERIC |  | This column stores the billing diagnosis-related group (DRG) condition code on the hospital account. |
| 3 | `BL_DRG_LOS` | INTEGER |  | This column stores the billing DRG length of service in days for the hospital account. |
| 4 | `BL_DRG_PAT_STATUS` | VARCHAR |  | The patient status for the billing DRG on the hospital account. |
| 5 | `BL_DRG_ECCS` | NUMERIC |  | The ECCS (episode clinical complexity score) associated with the billing DRG. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

