# ORD_AUD_READING_INFO

> This table contains audit information about the reading info on the imaging study.

**Overflow family:** [ORD_AUD_READING_INFO_2](ORD_AUD_READING_INFO_2.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `READING_RAD_EXTERNAL_VALUES` | VARCHAR |  | Audit column for list of reading physicians (external values) for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_RAD_READING.PROV_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `READING_RAD_IDS` | VARCHAR |  | Audit column for list of reading physicians (IDs) for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_RAD_READING.PROV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

