# ORD_LAB_PERFORM

> Contains the structure to support multiple lab specimens for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PERF_SPECIMEN_ID` | VARCHAR |  | The specimen used for the performable procedure on the corresponding line. |
| 4 | `PERF_ORDER_ID` | NUMERIC |  | The unique identifier associated with the order record for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

