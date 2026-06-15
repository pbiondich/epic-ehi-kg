# ACCOUNT_STATUS

> This table contains the account status data for each account. Account Status is a multiple response item, that is, an account in your system can have more than one status, such as Returned Mail, Payment Plan, or Collections. Therefore, one row in this table contains one line of account status information for an account. Each row is uniquely identified by the Account ID and line number combination.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the guarantor record. This identifier could be encrypted if you have implemented enterprise reporting’s encryption security function. |
| 2 | `LINE` | INTEGER | PK | Line number to identify the status information within the account. |
| 3 | `ACCOUNT_STATUS_C_NAME` | VARCHAR | org | The category value associated with the status of the account, such as Returned Mail, Collections, and so on. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

