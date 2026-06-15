# SOCIAL_CARE_EPISODE

> This table stores episode information for Compass Rose episodes.

**Primary key:** `EPISODE_ID`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `EPISODE_DEF_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 3 | `EPI_STATUS_C_NAME` | VARCHAR |  | The status category ID for the episode. |
| 4 | `EPISODE_START_DATE` | DATETIME |  | The date the episode was started. |
| 5 | `EPISODE_END_DATE` | DATETIME |  | The date the episode was ended. |
| 6 | `EPISODE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for a special contact which stores Social Care information at episode-level. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 7 | `DECISION_FIN_ASST_CASE_ID` | NUMERIC |  | The unique ID of the case which contains all the decisions created in the episode. |
| 8 | `RESPONSIBLE_USER_ID` | VARCHAR |  | The unique ID of the responsible user for the episode. |
| 9 | `RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `INIT_REFERRAL_ID` | NUMERIC |  | The unique ID of the referral that initiated the episode. |
| 11 | `PROGRAM_EPISODE_ID` | NUMERIC |  | The unique ID of the program episode for a service episode. If the episode is voided, it will contain a link to the parent record at the time the episode was voided. |
| 12 | `TRACKING_STATUS_C_NAME` | VARCHAR | org | The tracking status category ID for the episode. |
| 13 | `EPISODE_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 14 | `EPISODE_SUMMARY` | VARCHAR |  | An overview of a Social Care episode. |
| 15 | `CMGMT_ENROLL_DATE` | DATETIME |  | The date when the episode became active. Refer to CMGMT_ENROLL_CALC_DATE for more robust reporting. |
| 16 | `CMGMT_ENROLL_CALC_DATE` | DATETIME |  | The date that the user documented as the enrollment date or the date the status was originally changed to Active if no enrollment date is documented. If the overall episode status is Enrolling, the value will be blank. |
| 17 | `SOURCE_EVENT_TRIGGER_C_NAME` | VARCHAR |  | The source event category ID for an automatically created Compass Rose episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `EPISODE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

