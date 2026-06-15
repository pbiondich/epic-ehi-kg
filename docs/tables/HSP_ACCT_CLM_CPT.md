# HSP_ACCT_CLM_CPT

> This table contains hospital account claim CPT codes information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since coders can enter multiple CPT™ codes in a hospital account, each CPT™ code will have a unique line number. |
| 3 | `CLAIM_CODE_QTY` | INTEGER |  | This item holds the quantity as entered in Coding. If the quantity is greater than 1, each unit will be used as if it had been separately entered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

