# IP_EPISODE_LINK

> The episode table for Inpatient episodes. This is used as a substitute for the EPISODE and EPISODE_LINK tables.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | This identifies the encounter within the episode. |
| 3 | `SUM_BLK_TYPE_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 5 | `INP_CSN` | NUMERIC |  | A unique serial number for this Inpatient Data (INP) record. |
| 6 | `INPATIENT_DATA_ID` | VARCHAR | shared | A unique ID assigned to the Inpatient Data (INP) record |
| 7 | `START_DATE` | DATETIME |  | The date the episode was initiated in calendar format. This field is called Noted on the clinical system screen. |
| 8 | `END_DATE` | DATETIME |  | The date the episode was resolved in calendar format. This field is called Resolved on the clinical system screen. |
| 9 | `CARE_INTG_ID` | VARCHAR | FK→ | The unique ID for the inpatient care integrator record. |
| 10 | `STATUS_C_NAME` | VARCHAR |  | The status of the episode record: i.e. Active, Resolved, or Deleted. |
| 11 | `EPISODE_NAME` | VARCHAR |  | The name of the episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

