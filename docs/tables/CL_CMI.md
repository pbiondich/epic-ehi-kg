# CL_CMI

> This table contains information about component index records. A component index record can either represent a component or a component group record.

**Primary key:** `CMP_INDEX_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CMP_INDEX_ID` | VARCHAR | PK | The unique identifier for the component or component group record. |
| 2 | `CMP_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 3 | `COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

