# ACCOUNT_RQG_GROUPERS

> The list of requisition groupers that have charges on the account.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RQG_GROUPER_ID` | NUMERIC | FK→ | This column stores the unique identifier for a requisition grouper patient that has charges on the guarantor account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

