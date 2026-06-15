# ORD_AUD_END_PROC_ANS

> This table contains the auditing information for the radiology end procedure answers.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `END_PROC_ANS_IDS` | VARCHAR |  | This column contains the auditing information for the end exam questionnaires associated with this imaging study. This column has values delimited by "^". The source item is located at RIS_END_PROC_ANS. END_PROC_ANS_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

