# ORD_CLIN_IND

> The Clinical Indications (reason for exam) and associated comments.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of users who reviewed this order. |
| 3 | `CLIN_IND_TEXT` | VARCHAR |  | Clinical indications (reason for exam) free text answer to an order-specific question for this order. |
| 4 | `CLIN_IND_CMT_TEXT` | VARCHAR |  | Clinical indications (reason for exam) free text comment to an order-specific question for this order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

