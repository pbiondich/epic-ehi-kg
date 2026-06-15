# ORD_AUD_MAMMO_HORMONES_2

> This table contains the audit history for the deprecated order mammo hormone history.

**Overflow of:** [ORD_AUD_MAMMO_HORMONES](ORD_AUD_MAMMO_HORMONES.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HORMONES_END_DATE` | VARCHAR |  | Audit of hormone end dates relevant to breast imaging exams captured in the hormone history navigator. This column has values delimited by "^". The source item is located at MAMMO_HORMONES.END_DATE. |
| 4 | `HORMONES_START_DATE` | VARCHAR |  | Audit of hormone start dates relevant to breast imaging exams captured in the hormone history navigator. This column has values delimited by "^". The source item is located at MAMMO_HORMONES.START_DATE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

