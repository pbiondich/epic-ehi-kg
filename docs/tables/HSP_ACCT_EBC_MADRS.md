# HSP_ACCT_EBC_MADRS

> This table contains the mother's address of residence information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account id with associated electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with mother's address of residence on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_MOM_ADDR_RSDN` | VARCHAR |  | The mother's address of residence on the electronic birth certificate associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

