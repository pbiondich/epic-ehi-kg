# ACCT_HOME_PHONE_HX

> This table contains the guarantor's home phone history.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_DATE` | DATETIME |  | The date the home phone number was changed. |
| 4 | `PHONE_NUMBER` | VARCHAR |  | The home phone number on the account. |
| 5 | `CHANGE_SOURCE_C_NAME` | VARCHAR |  | The source of the change of the home phone number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

