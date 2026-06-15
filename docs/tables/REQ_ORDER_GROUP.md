# REQ_ORDER_GROUP

> This table contains information about orders associated with requisitions and cases.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique ID of the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | The unique ID of the order records that are associated with the requisition. |
| 4 | `ORDER_GROUP_ID` | NUMERIC |  | The order group ID is used to group together tests that were ordered as part of the same order or orderable panel. This item is primarily used for billing purposes to verify that all tests ordered as part of an order or panel are complete so that billing can be triggered at the order or panel level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

