# CLARITY_COMPONENT

> The CLARITY_COMPONENT table contains basic information about the standard result components that can constitute your procedures. For example, the components of a lab panel are usually the tests performed on a single specimen.

**Primary key:** `COMPONENT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMPONENT_ID` | NUMERIC | PK shared | The unique ID of the component record. |
| 2 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 3 | `NAME` | VARCHAR |  | The name of the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

