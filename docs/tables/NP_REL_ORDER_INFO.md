# NP_REL_ORDER_INFO

> This table extracts the related group of items ORD 705-707. These items contain the next pass release user ID, instant, and workstation ID from a multistep order transmittal rule.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NP_RELEASE_USER_ID` | VARCHAR |  | The user ID of the user who initiated the next pass through an order rule for generating tasks |
| 4 | `NP_RELEASE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `NP_RELEASE_INS_DTTM` | DATETIME (Local) |  | This date stamp indicates the time a rule (order transmittal rule) was reviewed for tasks to generate from an order (multistep order) |
| 6 | `NP_RELEASE_WS_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

