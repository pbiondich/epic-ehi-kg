# SUSPENSE_ACCT

> Stores information about suspense accounts for premium billing.

**Primary key:** `ACCOUNT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `EXTENRAL_ID` | VARCHAR |  | External ID |
| 3 | `OWNING_BUSSEG_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

