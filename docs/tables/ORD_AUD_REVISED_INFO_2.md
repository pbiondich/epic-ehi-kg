# ORD_AUD_REVISED_INFO_2

> This table contains audit information about the revised info.

**Overflow of:** [ORD_AUD_REVISED_INFO](ORD_AUD_REVISED_INFO.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVISE_DATES` | VARCHAR |  | This column contains the audit information about all the revising date. The values are delimited by "^". The source item is located at RIS_REVISE_RSLTS.REVISED_DATETIME. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

