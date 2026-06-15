# PROC_PROV_INFO_ORD

> This table contains information about the providers that will perform the requested procedure.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `PROC_PROV_SERVICE_C_NAME` | VARCHAR | org | This item contains the service for the performing provider. |
| 5 | `PROC_PROV_ROLE_C_NAME` | VARCHAR | org | This item contains the role of the performing provider. |
| 6 | `PROC_PROV_PANEL_NUM` | INTEGER |  | This item contains which panel the performing provider is on. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

