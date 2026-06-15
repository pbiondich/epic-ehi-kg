# HSP_ACCT_ATND_PROV

> This table contains hospital account attending provider information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number of the attending provider for the patient associated with the hospital account. Multiple attending providers can be stored in one hospital account, and each will have a unique line number. |
| 3 | `ATTENDING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ATTEND_DATE_FROM` | DATETIME |  | The date on which a provider began to be an attending provider for the patient associated with the hospital account. |
| 5 | `ATTEND_DATE_TO` | DATETIME |  | The date on which a provider ceased to be an attending provider for the patient associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

