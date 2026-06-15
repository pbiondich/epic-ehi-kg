# ORDER_RPTD_SIG_TEXT

> For each row in ORDER_RPTD_SIG_HX, this table contains the complete sig for the data represented by that row. Depending on whether your organization uses discrete sigs or not, this text may be generated from the various discrete fields or entered directly.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with the text of the sig of this medication. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of text of a sig within this record. |
| 4 | `SIG_TEXT` | VARCHAR |  | The text of the medication instructions for the order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

