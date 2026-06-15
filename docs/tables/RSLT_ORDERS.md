# RSLT_ORDERS

> This table contains information about orders associated with result records.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_ORDER_ID` | NUMERIC |  | The unique ID of the source order for the result. For tests that have been redrawn or moved, this is the removed order. For tests that have not be redrawn or removed, this is an order that the current result for the test will file to. This is the culture order for susceptibility tests. Anatomic pathology results may have multiple source orders. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

