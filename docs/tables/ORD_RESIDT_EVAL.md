# ORD_RESIDT_EVAL

> Indicates the resident's performance in reading this study.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. This column is frequently used to link to the ORDER table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORD_RESIDT_EVAL_C_NAME` | VARCHAR | org | The resident evaluation category ID for the order. This indicates the resident's performance in reading this study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

