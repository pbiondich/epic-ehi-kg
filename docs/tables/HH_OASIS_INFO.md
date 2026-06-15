# HH_OASIS_INFO

> Contains Home Health Outcome and Assessment Information Set (OASIS) noadd single items.

**Primary key:** `OASIS_SET_ID`  
**Columns:** 11  
**Org-specific columns:** 3  
**Joined by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK | Unique identifier for the OASIS data set. |
| 2 | `OASIS_DATA_SET_C_NAME` | VARCHAR | org | The type of OASIS data set. Links to category list ZC_OASIS_DATA_SET. |
| 3 | `OASIS_SET_STATUS_C_NAME` | VARCHAR | org | OASIS data set status. Links to category list ZC_OASIS_SET_STATUS. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. Links to table PAT_ENC. |
| 5 | `OASIS_VERSION_C_NAME` | VARCHAR | org | OASIS version. Links to category list ZC_OASIS_VERSION. |
| 6 | `ADDENDUM_YN` | VARCHAR |  | This is a flag that indicates whether an addendum has been created for an OASIS assessment contact since the last time the dataset was submitted to the state. |
| 7 | `CUR_OASIS_LOCK_STAT_C_NAME` | VARCHAR |  | The current lock status of the OASIS assessment data set. Links to category list ZC_OASIS_LOCK_STAT. |
| 8 | `DATASET_TYPE_C_NAME` | VARCHAR |  | Stores what type of dataset the record is. Currently datasets can be OASIS or HIS. |
| 9 | `ADND_3RD_EXPORT_YN` | VARCHAR |  | This is a flag that indicates whether an OASIS assessment contact has had an addendum created since the last time the dataset was submitted to a 3rd party. |
| 10 | `LAST_ADDENDUM_DATE` | DATETIME |  | This is the date of the last addendum created for an OASIS assessment contact. |
| 11 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient associated with the data set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (10)

| From | Column | Confidence |
|------|--------|------------|
| [HH_EPS_NY_INFO](HH_EPS_NY_INFO.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_DATA](HH_OASIS_DATA.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_ENC](HH_OASIS_ENC.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_LOCK](HH_OASIS_LOCK.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_SNAPSHOT_HX](HH_OASIS_SNAPSHOT_HX.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_SUBM](HH_OASIS_SUBM.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_SUBM_RESP](HH_OASIS_SUBM_RESP.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_TRL_ENC](HH_OASIS_TRL_ENC.md) | `OASIS_SET_ID` | high |
| [HH_OASIS_TRL_INFO](HH_OASIS_TRL_INFO.md) | `OASIS_SET_ID` | high |
| [HSPC_HIS_VOID_HX](HSPC_HIS_VOID_HX.md) | `OASIS_SET_ID` | high |

