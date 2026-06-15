# OR_LNLG_SCD

> This table contains the SCD information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 8  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `SCD_DEVICE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `SCD_AREA_C_NAME` | VARCHAR | org | The area category ID for the sequential compression device (SCD) associated with the procedural log. |
| 4 | `SCD_AREA_LAT_C_NAME` | VARCHAR | org | The laterality of the area. |
| 5 | `SCD_DEVICE_TYP_C_NAME` | VARCHAR | org | The type of sequential compression device (SCD). |
| 6 | `SCD_PRESSURE` | NUMERIC |  | The pressure setting of the sequential compression device (SCD). |
| 7 | `SCD_LEFT_PULSE` | VARCHAR |  | The left pulse of the sequential compression device (SCD). |
| 8 | `SCD_RIGHT_PULSE` | VARCHAR |  | The right pulse of the sequential compression device (SCD). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

