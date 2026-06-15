# DD_DIA_CMS_TELEMEDICINE

> This table contains data elements submitted for CMS ESRD monthly forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `PAT_HAD_TELEMEDICINE_VISIT_YN` | VARCHAR |  | It stores whether the dialysis patient had a telemedicine visit in the reporting month. |
| 3 | `NUMBER_TELEMEDICINE_VISITS` | NUMERIC |  | It stores the number of telemedicine visits in the reporting month. |
| 4 | `TELEMEDICINE_LAST_VISIT_DATE` | DATETIME |  | It stores the last telemedicine visit date for the reporting month. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

