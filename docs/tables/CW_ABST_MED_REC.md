# CW_ABST_MED_REC

> Medication reconciliation information reported to CROWNWeb, the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `MED_RECONCILIATION_DATE` | DATETIME |  | This item stores the date when a medication reconciliation was performed for the patient. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `PROV_TYPE_C_NAME` | VARCHAR |  | This item stores the provider type of the provider who performed the medication reconciliation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

