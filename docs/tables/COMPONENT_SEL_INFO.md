# COMPONENT_SEL_INFO

> This table contains additional information related to the selected components.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPONENT_USER_ID` | VARCHAR |  | The EMP ID associated with the selected components. |
| 4 | `COMPONENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `COMPONENT_ORD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `COMPONENT_ORD_PROV_ADDR` | VARCHAR |  | The address ID of the ordering provider associated with the selected components. |
| 7 | `COMPONENT_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `COMPONENT_AUTH_PROV_ADDR` | VARCHAR |  | The address ID of the ordering provider associated with the selected components. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

