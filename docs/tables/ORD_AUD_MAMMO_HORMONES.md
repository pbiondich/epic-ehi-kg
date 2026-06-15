# ORD_AUD_MAMMO_HORMONES

> This table contains the audit history for the deprecated mammo hormone history.

**Overflow family:** [ORD_AUD_MAMMO_HORMONES_2](ORD_AUD_MAMMO_HORMONES_2.md), [ORD_AUD_MAMMO_HORMONES_3](ORD_AUD_MAMMO_HORMONES_3.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HORMONES` | VARCHAR |  | Audit of hormone information (category values) relevant to breast imaging exams captured in the hormone history navigator. This column has values delimited by "^". The source item is located at MAMMO_HORMONES.HORMONE_C. |
| 4 | `HORMONES_EXTERNAL_VALUES` | VARCHAR |  | Audit of hormone information (external category values) relevant to breast imaging exams captured in the hormone history navigator. This column has values delimited by "^". The source item is located at MAMMO_HORMONES.HORMONE_C. This column shows the translated external value as of when the column was last extracted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

