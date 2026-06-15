# COVID_19_HSP_CONF_INF_HX

> Contains information on all confirmed COVID-19 periods for a hospital admission.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONFIRMED_INF_START_DATE` | DATETIME |  | Stores the start date for a period during which a patient had a confirmed COVID-19 infection |
| 4 | `CONFIRMED_INF_END_DATE` | DATETIME |  | Stores the end date for a period during which a patient had a confirmed COVID-19 infection |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

