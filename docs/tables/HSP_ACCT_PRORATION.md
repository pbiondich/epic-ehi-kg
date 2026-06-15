# HSP_ACCT_PRORATION

> This table contains the Proration related information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COVERAGE_ID` | NUMERIC | FK→ | This column stores the unique identifier for the coverage record on the hospital account. |
| 4 | `CVG_AUTH_NUM` | VARCHAR |  | The coverage authorization number. |
| 5 | `EXP_COPAY_AMT` | NUMERIC |  | The expected copay amount. |
| 6 | `EXP_COINS_PC` | NUMERIC |  | This column stores the expected coinsurance percentage. |
| 7 | `EXP_COINS_AMT` | NUMERIC |  | This column stores the expected coinsurance amount. |
| 8 | `EXP_DED_AMT` | NUMERIC |  | This column stores the expected deductible amount. |
| 9 | `SYS_EXP_COPAY_AMT` | NUMERIC |  | This column stores the copay amount expected by the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

