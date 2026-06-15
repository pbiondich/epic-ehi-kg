# ORD_AUD_READING_INFO_2

> This table contains audit information about the reading info on the imaging study.

**Overflow of:** [ORD_AUD_READING_INFO](ORD_AUD_READING_INFO.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `READ_DATES` | VARCHAR |  | Audit column for list of reading dates for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_RAD_READING.READING_DT. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

