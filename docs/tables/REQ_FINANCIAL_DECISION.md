# REQ_FINANCIAL_DECISION

> This table contains the financial decision for an appointment request in each location that was considered.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQ_REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `REQ_NODE_CSN` | NUMERIC |  | This stores the contact serial number (CSN) for the record that contains the financial decision information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

