# TRANSPLANT_COOR_HX

> This table contains a list of all coordinator(s) who have been or are listed as the transplant episode coordinators. This table also contains all organ classes that have been added or removed from the episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The transplant episode record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_COORD_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `TX_COORD_UPD_USR_ID` | VARCHAR |  | The user who updated transplant coordinator field. |
| 5 | `TX_COORD_UPD_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TX_COORD_UPD_INST` | DATETIME (Local) |  | The instant when transplant coordinator was updated |
| 7 | `TX_COORD_STAT_C_NAME` | VARCHAR |  | Stores whether the coordinator is active or inactive |
| 8 | `TX_CLASS_HX_C_NAME` | VARCHAR |  | Stores organ classifications that have been added or deleted from the episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

