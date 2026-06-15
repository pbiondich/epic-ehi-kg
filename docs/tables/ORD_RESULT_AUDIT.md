# ORD_RESULT_AUDIT

> This table contains the audit trail of pathology results linked to an order. Each row in this table corresponds to changes made to a pathology result. From this table, ORD_RESULT_AUDIT, join to the two primary keys of RESULT_AUDIT using ORD_RESULT_AUDIT.FINDING_ID and ORD_RESULT_AUDIT.FINDING_AUD_LINE. The table RESULT_AUDIT contains the specific changes made to each pathology result.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_ID` | NUMERIC | shared | Contains the ID of the result finding record being audited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

