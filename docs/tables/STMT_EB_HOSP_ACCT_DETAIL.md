# STMT_EB_HOSP_ACCT_DETAIL

> This table contains the hospital accounts included on enterprise guarantor statement and detail bill print records. This hospital account data is extracted to replace hospital account information previously deprecated from ACCT_EB_STMT_HIST, and is not meant for use except in conjunction with table ACCT_EB_STMT_HIST.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier for the statement/detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account included on the associated enterprise guarantor statement or detail bill record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

