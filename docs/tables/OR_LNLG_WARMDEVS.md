# OR_LNLG_WARMDEVS

> This table contains the Warming Devices information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 7  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `WARMING_DEVICE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `WARMING_AREA_LAT_C_NAME` | VARCHAR | org | The laterality if the area. |
| 4 | `WARM_DEVICE_TYPE_C_NAME` | VARCHAR | org | The type of the warming device. |
| 5 | `WARMING_AREA_C_NAME` | VARCHAR | org | The area applied. |
| 6 | `WARMING_TEMPERATUR` | NUMERIC |  | The temperature of the warming device. |
| 7 | `WARMING_SETTING_C_NAME` | VARCHAR | org | The setting of the warming device. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

