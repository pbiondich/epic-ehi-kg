# NEPHROLOGY_INFO

> The NEPHROLOGY_INFO table contains information about a patient's dialysis episode. The records included in this table are HSB records that are designated as dialysis episodes, where the episode type (HSB 35250) has a value of 35.

**Primary key:** `EPISODE_ID`  
**Columns:** 22  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the dialysis episode record. |
| 2 | `CONTACT_TYPE_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 3 | `EPISODE_STATUS_C_NAME` | VARCHAR |  | The episode's status. |
| 4 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `COMMENTS` | VARCHAR |  | The episode comments. |
| 6 | `DIALYSIS_ADMISSION_REASON_C_NAME` | VARCHAR | org | This item stores the patient's reason for starting dialysis treatment in a facility. |
| 7 | `TRANSIENT_YN` | VARCHAR |  | This item is used to indicate whether the patient is receiving temporary treatment at a dialysis facility. |
| 8 | `DIALYSIS_DISCHARGE_REASON_C_NAME` | VARCHAR | org | This item stores the patient's reason for ending dialysis treatment in a facility. |
| 9 | `TRANSFER_DESTINATION_C_NAME` | VARCHAR | org | This item is used to store where a patient will be getting dialysis treatment after discharging from the current facility. |
| 10 | `TREATMENT_TYPE_C_NAME` | VARCHAR | org | This item is used to store a patient's type of dialysis treatment. |
| 11 | `DIALYSIS_HISTORICAL_EPISODE_YN` | VARCHAR |  | This item is used to indicate whether the episode is a historical or external dialysis treatment episode, or an internal dialysis treatment episode. |
| 12 | `DIALYSIS_DISCHARGE_OTHR` | VARCHAR |  | This item stores a free text comment if a patient's dialysis discharge reason is set to Other. |
| 13 | `DIALYSIS_START_DATE` | DATETIME |  | This item is used to store the start date of a patient's dialysis treatment episode. |
| 14 | `DIALYSIS_END_DATE` | DATETIME |  | This item is used to store the end date of a patient's dialysis treatment episode. |
| 15 | `PLACE_OF_SERVICE_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 16 | `MODALITY_START_DATE` | DATETIME |  | This item stores a dialysis patient's start date of their current treatment details. |
| 17 | `DIALYSIS_EPISODE_PURPOSE_C_NAME` | VARCHAR |  | Indicates the purpose of the dialysis episode. |
| 18 | `NEPH_DLYS_TYPE_C_NAME` | VARCHAR |  | The type of dialysis. Either end stage renal disease (ESRD) or acute kidney injury (AKI). If null then the episode is assumed to be ESRD. |
| 19 | `NEPH_TRANSIENT_RSN_C_NAME` | VARCHAR | org | This item stores the patient's reason for receiving temporary treatment at a dialysis facility. |
| 20 | `TREATMENT_SESSIONS_PER_WEEK` | NUMERIC |  | This item stores the most recently prescribed sessions per week of the dialysis treatments. |
| 21 | `TREATMENT_DURATION_MINUTES` | INTEGER |  | This item stores the most recently prescribed duration of each dialysis treatment in minutes. |
| 22 | `EXTERNAL_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

