# OR_LNLG_IMPLANTS

> This table contains the implants information for the surgical/invasive procedure log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 19  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `IMP_NO_INV_ITEM_YN` | VARCHAR |  | Specifies if this implant has no inventory item specified. |
| 3 | `IMPLANT_ID` | VARCHAR | shared | The unique identifier for the implant record. |
| 4 | `IMPLANT_ACTION_C_NAME` | VARCHAR | org | The action taken on the implant. |
| 5 | `IMPLANT_NUM_USED` | INTEGER |  | The number of implants used. |
| 6 | `IMPLANT_AREA_C_NAME` | VARCHAR | org | The implant area category ID for the implant associated with the procedural log. |
| 7 | `IMPLANT_LATERAL_C_NAME` | VARCHAR | org | The laterality of the area. |
| 8 | `IMPLANT_RSN_WSTD_C_NAME` | VARCHAR | org | The reason why the implant was wasted. |
| 9 | `IMPLANT_CREATED_YN` | VARCHAR |  | Was the implant created in the log? |
| 10 | `IMP_TRAY_TYPE_C_NAME` | VARCHAR | org | This item stores the instrument type of the implant tray. |
| 11 | `IMP_TRAY_ID` | NUMERIC |  | This item is populated if the current implant row is an implant tray, and stores the tray id. |
| 12 | `IMP_TRAY_ID_RECORD_NAME` | VARCHAR |  | Name of the implant tray |
| 13 | `IMPLANT_FLASH_YN` | VARCHAR |  | Indicates whether this implant has been flash-sterilized. |
| 14 | `FLSH_AUTCLVE_C_NAME` | VARCHAR | org | The autoclave category number that was used to sterilize this implant. |
| 15 | `FLSH_LOAD` | VARCHAR |  | The load batch ID that this implant was flash sterilized in. |
| 16 | `FLSH_RSN_C_NAME` | VARCHAR | org | The category number of the reason that this implant was flash sterilized. |
| 17 | `FLSH_VER_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `FLSH_RSLT_C_NAME` | VARCHAR | org | The category number of the result of this implants flash sterilization process. |
| 19 | `FLSH_PRE_RSN_C_NAME` | VARCHAR | org | The category number of the reason this implant was pre-released in the flash sterilization process. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

