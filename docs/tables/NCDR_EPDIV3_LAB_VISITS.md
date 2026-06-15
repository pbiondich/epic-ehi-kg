# NCDR_EPDIV3_LAB_VISITS

> This table contains information from the Lab Visits section of the NCDR EP Device registry v3.0.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `ROOM_ENTRY_DATE` | DATETIME |  | Indicate the date the patient entered the procedure room. |
| 4 | `ROOM_ENTRY_TM` | DATETIME (Local) |  | Indicate the time the patient entered the procedure room. |
| 5 | `ROOM_EXIT_DATE` | DATETIME |  | Indicate the date the patient exits the procedure room. |
| 6 | `ROOM_EXIT_TM` | DATETIME (Local) |  | Indicate the time the patient exits the procedure room. |
| 7 | `SHD_DC_TL_DYN_C_NAME` | VARCHAR | org | Indicate what tool was used. |
| 8 | `POSTMARK_SURV_YN` | VARCHAR |  | Indicate if the ICD procedure (generator implant or lead procedure) or pacemaker procedure is part of post-market surveillance trial(s). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

