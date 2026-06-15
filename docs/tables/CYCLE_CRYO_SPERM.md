# CYCLE_CRYO_SPERM

> Contains information about the sperm that was cryopreserved as part of a fertility treatment cycle.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CRYO_SPERM_ID_NAME` | VARCHAR |  | Stores a custom ID title for the cryopreservation. If not set, a generated default will be shown to the user, based on the line number. |
| 4 | `CRYO_SPERM_DATE` | DATETIME |  | Stores the date of cryopreservation for sperm. |
| 5 | `SPERM_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR | org | Stores the cryopreserved sperm source, such as from a partner or donor. |
| 6 | `SPERM_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR | org | Stores the cryopreserved sperm state at the beginning of the cycle, such as fresh or thawed. |
| 7 | `CRYO_SPERM_DONOR` | VARCHAR |  | Stores the cryopreserved sperm donor ID. |
| 8 | `CRYO_SPERM_COLL_C_NAME` | VARCHAR | org | Stores the cryopreserved sperm's collection method. |
| 9 | `CRYO_SPERM_VOLUME` | NUMERIC |  | Stores the cryopreserved sperm's volume in milliliters. |
| 10 | `CRYO_SPERM_CONCEN` | NUMERIC |  | Stores the cryopreserved sperm's concentration, in millions per milliliter. |
| 11 | `CRYO_SPERM_MOTILITY` | INTEGER |  | Stores the cryopreserved sperm's motility, in percent. |
| 12 | `CRYOSPM_PROGRESS_C_NAME` | VARCHAR | org | Stores the cryopreserved sperm's grade of progression. |
| 13 | `CRYO_SPERM_MORPHOLOGY` | INTEGER |  | Stores the cryopreserved sperm's morphology, as a percent that are normal. |
| 14 | `CRYO_SPERM_FROZ_VIALS` | INTEGER |  | Stores the number of vials frozen for cryopreserved sperm. |
| 15 | `CRYO_SPERM_VOL_PER_VIA` | NUMERIC |  | Stores the volume per vial for the cryopreserved sperm, in milliliters. |
| 16 | `CRYO_SPERM_COLLECT_COMMENT` | VARCHAR |  | Stores the comments for the collection method for the cryopreserved sperm. |
| 17 | `CRYO_SPERM_COMMENTS` | VARCHAR |  | Stores cryo specific comment for sperm. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

