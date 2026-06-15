# RYN_WHT_SERVICE_VISITS

> The Ryan White patient's service visits in the reporting period.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_SVC_VISIT_TYPE_C_NAME` | VARCHAR |  | Core medical service visit types during the reporting period. |
| 4 | `RYN_WHT_SVC_VISITS_CNT` | INTEGER |  | The number of patient visits with the provider for each core medical service during the reporting period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

