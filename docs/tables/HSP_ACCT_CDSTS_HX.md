# HSP_ACCT_CDSTS_HX

> This table contains the history of coding status changes for each account coded.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID with related coding status history information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each coding history will have its own line number. |
| 3 | `CDSTS_HX_UTC_DTTM` | DATETIME (UTC) |  | Coding status changed instant - stored in UTC time. Data will not exist in this column for coding statuses created before UTC instant tracking was enabled for coding history. |
| 4 | `CDSTS_HX_SVC_STS_C_NAME` | VARCHAR |  | Holds the simple visit coding (SVC) completion status when coding status is set by simple visit coding. |
| 5 | `CDSTS_HX_ASGN_USER_ID` | VARCHAR |  | Item to store coding assigned user changes |
| 6 | `CDSTS_HX_ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

