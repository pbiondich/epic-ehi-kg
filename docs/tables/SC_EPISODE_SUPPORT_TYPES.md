# SC_EPISODE_SUPPORT_TYPES

> Table for the Compass Rose episode event items that include a history of support and services provided and their start and end dates.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SC_SUPPORT_TYPE_C_NAME` | VARCHAR | org | The support and service type category ID for episode. |
| 4 | `SC_SUPPORT_TYPE_START_DT` | DATETIME |  | The date when the support and service type started. |
| 5 | `SC_SUPPORT_TYPE_END_DT` | DATETIME |  | The date when the support and service type ended. |
| 6 | `SUPPORT_TYPE_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `SUPPORT_TYPE_RESP_REGISTRY_ID` | NUMERIC |  | The unique identifier of the responsible pool for the support and service type. |
| 8 | `SUPPORT_TYPE_RESP_REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

