# ORD_AUD_MAMMO_HORMONES_3

> This table contains the audit history for the deprecated mammo hormone history.

**Overflow of:** [ORD_AUD_MAMMO_HORMONES](ORD_AUD_MAMMO_HORMONES.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HORMONES_CUR_TAKING` | VARCHAR |  | Audit trail column for mammo hormones currently taking (category values). This column has values delimited by "^". The source item is located at MAMMO_HORMONES.CURRENTLY_USING_YN. |
| 4 | `HORMONES_CUR_TAKING_EXT_VALS` | VARCHAR |  | Audit trail column for mammo hormones currently taking (external category values). This column has values delimited by "^". The source item is located at MAMMO_HORMONES.CURRENTLY_USING_YN. This column shows the translated external value as of when the column was last extracted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

