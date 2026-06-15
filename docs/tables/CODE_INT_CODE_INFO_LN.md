# CODE_INT_CODE_INFO_LN

> This table connects the coded CPTs used in coding-only and combined service lines with the line where the CPT was entered in Coding (HAR 1750 related group). CPTs from multiple lines can be included on one service line. Values are only available for coding-only and combined lines. Rows will not be extracted for charge-only lines.

**Primary key:** `HSP_ACCOUNT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CODE_INT_CODE_INFO_LN` | INTEGER |  | This item holds line numbers for the coded Current Procedural Terminology code included in the service line. The item will only have a value for coding-only and combined lines. It will be blank for transaction-only lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

