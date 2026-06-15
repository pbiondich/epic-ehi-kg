# ODC_CTX_COMMENTS

> The ODC_CTX_COMMENTS table contains the comment information for the order context record.

**Primary key:** `ORDER_CONTEXT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_CONTEXT_ID` | NUMERIC | PK FK→ | The unique identifier for the order context record, which contains information about when orders are intended to be used. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTEXT_COMMENTS` | VARCHAR |  | The comments describing the intended purpose for the associated orders, entered by the user who created the order context record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_CONTEXT_ID` | [ODC_BASIC](ODC_BASIC.md) | sole_pk | high |

