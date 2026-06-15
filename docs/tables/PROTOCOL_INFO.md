# PROTOCOL_INFO

> This table stores QuickForm-based protocol information for an order. If you have configured the system to use SmartForm-based protocols, you should look to ORDER_CONCEPT instead.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. This column is frequently used to link to the ORDER_PROC table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASGN_PROTOCOL_ID` | VARCHAR |  | The unique ID of the protocol assigned to this order. |
| 4 | `ASGN_PROTOCOL_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

