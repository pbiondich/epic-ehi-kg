# OR_LNLG_XRAYS

> This table contains the X-Ray information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 9  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `XRAY_DEVICE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `XRAY_TYPE_C_NAME` | VARCHAR | org | The X-Ray device type. |
| 4 | `XRAY_AREA_C_NAME` | VARCHAR | org | The area applied. |
| 5 | `XRAY_AREA_LAT_C_NAME` | VARCHAR | org | The laterality of the area. |
| 6 | `XRAY_DEVTYPE_C_NAME` | VARCHAR | org | The type of X-ray. |
| 7 | `XRAY_DAP` | NUMERIC |  | The Dose Area Product (DAP) for the x-ray machine (in Gray square centimeters). |
| 8 | `XRAY_RESULT_TIME` | INTEGER |  | The length of time it takes for radiology to return x-ray results to the surgeon. |
| 9 | `XRAY_AIR_KERMA` | NUMERIC |  | This item stores the X-Ray Air Kerma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

