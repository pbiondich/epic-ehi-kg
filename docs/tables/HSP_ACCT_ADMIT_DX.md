# HSP_ACCT_ADMIT_DX

> This table contains hospital account admit diagnoses from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. As multiple admission diagnoses can be stored in one hospital account, each diagnosis will have a unique line number. |
| 3 | `ADMIT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ADMIT_DX_TEXT` | VARCHAR |  | A text description of an admission diagnosis stored in the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

