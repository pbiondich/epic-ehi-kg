# COVID_19_HSP_INFECTIONS

> COVID-19 infections associated with hospital encounters.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `INFECTION_START_DATE` | DATETIME |  | Date the COVID-19 infection was first identified. |
| 3 | `SOURCE_INFECTION_ID` | NUMERIC |  | Source INF record for the COVID-19 infection for this encounter. |
| 4 | `INFECTION_START_DTTM` | DATETIME (Local) |  | Instant the COVID-19 infection was first identified. |
| 5 | `SUSP_INFECTION_START_DATE` | DATETIME |  | Date the COVID-19 infection was first suspected. |
| 6 | `SUSP_INFECTION_END_DATE` | DATETIME |  | Date the COVID-19 infection was no longer suspected. |
| 7 | `INFECTION_CONFIRMED_YN` | VARCHAR |  | Whether or not a COVID-19 infection has been confirmed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

