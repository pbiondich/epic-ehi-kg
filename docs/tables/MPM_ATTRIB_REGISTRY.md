# MPM_ATTRIB_REGISTRY

> This table contains data about registries that are attributed to patients for My Panel Metrics.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REGISTRY_ID` | NUMERIC | shared | The HFR ID of a registry attributed to the patient for the purpose of My Panel Metrics. |
| 4 | `REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the registry record. |
| 5 | `MEASURE_GROUP_C_NAME` | VARCHAR | org | Measure groups attributed to registries for this patient for the purpose of My Panel Metrics. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

