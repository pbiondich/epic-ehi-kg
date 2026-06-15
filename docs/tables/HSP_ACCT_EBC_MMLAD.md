# HSP_ACCT_EBC_MMLAD

> This table contains the mother's mailing address information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with mother's mailing address on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_MOM_MAIL_ADDR` | VARCHAR |  | The mother's mailing address on the electronic birth certificate associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

