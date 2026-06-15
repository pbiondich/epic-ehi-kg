# CODE_INT_CODE_INT_LN

> This table connects the coded CPTs used in coding-only and combined service lines with the line where the CPT was stored in Code Integration (HAR 2110 related group). CPTs from multiple lines can be included on one service line. Values are only available for coding-only and combined lines. The table will be blank for charge-only lines.

**Primary key:** `HSP_ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCT_ID` | NUMERIC | PK | The unique identifier for the hospital account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CODE_INT_CODE_INT_LN` | INTEGER |  | This holds line numbers for the coded Current Procedural Terminology code included in the service line. The item will only have a value for coding-only and combined lines. It will be blank for transaction-only lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

