# ORDER_REFLEX_COMPONENTS

> Stores the components that caused a reflex order to be placed.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFLEX_COMPONENT_ID` | NUMERIC |  | The unique ID of the component that caused a reflex order to be placed. |
| 4 | `REFLEX_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

