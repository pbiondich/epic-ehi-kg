# CODE_INT_CODE_INFO_QUAN

> This table holds the quantity of each coded CPT contributing to coding-only and combined service lines. The quantity in this table is associated with the Coding Info line number in CODE_INT_COD_INF_LN. Values are only available for coding-only and combined lines. Rows will not be extracted for charge-only lines.

**Primary key:** `HSP_ACCOUNT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CODE_INT_CODE_INFO_QUAN` | INTEGER |  | This holds the total quantity contributing to the service line from a single Coding Current Procedural Terminology code. The item will only have a value for coding-only and combined lines. It will be blank for transaction-only lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

