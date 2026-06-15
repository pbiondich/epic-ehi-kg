# SPECIMEN_ALL_OWNERS

> Stores all the current, previous, and future owners for a specimen.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `ALL_OWNER_PAT_ID` | VARCHAR | FK→ | Stores all the patients who are previous, current, or future owners of a given specimen (embryo, oocyte, or sperm). |
| 5 | `ALL_OWNER_COMMENTS` | VARCHAR |  | Comments associated with the owner of the specimen. |
| 6 | `ALL_OWN_START_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant the owner started their ownership over a particular specimen. |
| 7 | `ALL_OWN_END_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant the owner ended their ownership over a particular specimen. |
| 8 | `PREV_SPEC_REI_SPEC_STATE_C_NAME` | VARCHAR |  | Stores the state of the specimen (in-culture, frozen, discarded, etc.) at the instant ownership changes from active to previous for a given specimen. |
| 9 | `PREV_SPEC_EMB_SPEC_TYPE_C_NAME` | VARCHAR |  | The type of embryology specimen (oocyte, embryo, or sperm) at the instant ownership changes from active to previous for a given specimen. |
| 10 | `PREV_SPEC_CULT_DAY` | INTEGER |  | Stores the latest number of culture days that have occurred for the specimen when it was received in the lab at the instant ownership changes from active to previous for a given specimen. |
| 11 | `PREV_EXT_RTRVL_DATE` | DATETIME |  | Stores the last documented date on which the oocyte retrieval occurred since the instant their ownership had expired. |
| 12 | `PREV_EXT_FREEZE_DATE` | DATETIME |  | Stores the last documented date on which the specimen was frozen since the instant their ownership had expired. |
| 13 | `PREV_SPEC_EXT_CMTS` | VARCHAR |  | Stores the last documented comments associated with the embryology specimen that came from an external lab. |
| 14 | `PREV_OOCYTE_PAT_ID` | VARCHAR | FK→ | Stores the last patient record ID who was an oocyte contributor to the specimen at the end of an owner's period of ownership. |
| 15 | `PREV_OOCYTE_RECORD_ID` | NUMERIC |  | Stores the last non-patient record ID who was an oocyte contributor to the specimen at the end of an owner's period of ownership. |
| 16 | `PREV_EGG_GAMETE_SOURCE_C_NAME` | VARCHAR | org | Stores the last type of genetic contribution of the oocyte contributor. This includes autologous, partner, anonymous donor, and directed donor. |
| 17 | `PREV_SPERM_PAT_ID` | VARCHAR | FK→ | Stores the last patient record ID who was a sperm contributor to the specimen at the end of an owner's period of ownership. |
| 18 | `PREV_SPERM_RECORD_ID` | NUMERIC |  | Stores the last non-patient record ID who was a sperm contributor to the specimen at the end of an owner's period of ownership. |
| 19 | `PREV_SPERM_GAMETE_SOURCE_C_NAME` | VARCHAR |  | Stores the last type of genetic contribution of the sperm contributor. This includes autologous, partner, anonymous donor, and directed donor. |
| 20 | `PREV_OVARIAN_TISSUE_PAT_ID` | VARCHAR | FK→ | Stores the last patient record ID who was an ovarian tissue contributor to the specimen at the end of an owner's period of ownership. |
| 21 | `PREV_TESTICULAR_TISSUE_PAT_ID` | VARCHAR | FK→ | Stores the last patient record ID who was a testicular tissue contributor to the specimen at the end of an owner's period of ownership. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALL_OWNER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PREV_OOCYTE_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PREV_OVARIAN_TISSUE_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PREV_SPERM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PREV_TESTICULAR_TISSUE_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

