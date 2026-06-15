# HSP_ACCT_PAT_CSN

> This table contains hospital account patient contact serial number (CSN) information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple patient contacts can be associated with one hospital account, each contact will have a unique line number. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique identifier for the treatment plan record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

