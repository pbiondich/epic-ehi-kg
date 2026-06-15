# HSP_ACCT_STOP_BILL

> This table contains hospital account stop bill information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of the hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple stop bills can be placed on one hospital account, each stop bill will have a unique line number. |
| 3 | `STOPBILL_SOURCE_C_NAME` | VARCHAR |  | The source for stop bills added automatically by the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

