# INFECTIONS

> This table contains basic information about patient infections.

**Primary key:** `INFECTION_ID`  
**Columns:** 29  
**Org-specific columns:** 3  
**Joined by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK | The unique identifier for the infection record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category ID for the infection. |
| 3 | `INFECTION_RECORD_TYPE_C_NAME` | VARCHAR |  | The record type category ID for the infection. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 6 | `INFECTION_TYPE_C_NAME` | VARCHAR | org | The infection type category ID for the infection. |
| 7 | `INF_STATUS_C_NAME` | VARCHAR |  | The infection status category ID for the infection. |
| 8 | `HOW_ADDED_C_NAME` | VARCHAR |  | The how added category ID for the infection. This indicates the method by which the infection was added to the patient chart. |
| 9 | `ADD_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that the infection was added to the patient chart. |
| 10 | `ADD_USER_ID` | VARCHAR |  | The unique ID associated with the user who added the infection. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `ADD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `RESOLVE_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that the infection was resolved in the patient chart. |
| 13 | `RESOLVE_USER_ID` | VARCHAR |  | The unique ID associated with the user who resolved the infection. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `RESOLVE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `EXPIRATION_DATE` | DATETIME |  | The date when the infection is set to automatically expire. |
| 16 | `DOESNT_EXPIRE_YN` | VARCHAR |  | Indicates whether the infection should not automatically expire. 'Y' indicates that the infection requires clinical judgement to be marked as resolved. 'N' or NULL indicates that it is safe for the infection to expire automatically if an expiration date is given. |
| 17 | `REVIEW_DATE` | DATETIME |  | The date that the infection should be reviewed. |
| 18 | `ONSET_DATE` | DATETIME |  | The date that the infection began. |
| 19 | `COMMENTS` | VARCHAR |  | User-entered comments associated with the infection. |
| 20 | `SPECIMEN_TYPE_C_NAME` | VARCHAR | org | The specimen type category ID for the infection. |
| 21 | `SPECIMEN_SOURCE_C_NAME` | VARCHAR | org | The specimen source category ID for the infection. |
| 22 | `RECORD_CREATION_DATE` | DATETIME |  | The date the infection record was created. |
| 23 | `ADD_LOCAL_DTTM` | DATETIME (Attached) |  | The local date and time that the infection was added to the patient chart. |
| 24 | `RESOLVE_LOCAL_DTTM` | DATETIME (Attached) |  | The local date and time that the infection was resolved in the patient chart. |
| 25 | `ISOLATION_LINKS_CALCULATED_YN` | VARCHAR |  | Indicates whether all linked isolations have been calculated. 'Y' indicates all linked isolations have been calculated. 'N' or NULL indicates that there may be isolations that would be considered linked to the infection, but that pre-date the linking calculation. |
| 26 | `REQUIRED_ISOLATION_OPTION_C_NAME` | VARCHAR |  | The isolation override option category ID that was most-recently applied. |
| 27 | `COMMENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that the current comment was saved. |
| 28 | `COMMENT_USER_ID` | VARCHAR |  | The unique ID associated with the user who entered the current comment. This column is frequently used to link to the CLARITY_EMP table. |
| 29 | `COMMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (7)

| From | Column | Confidence |
|------|--------|------------|
| [CW_ABST_INFECTIONS](CW_ABST_INFECTIONS.md) | `INFECTION_ID` | high |
| [INFECTIONS_INDICATE_ALERT](INFECTIONS_INDICATE_ALERT.md) | `INFECTION_ID` | high |
| [INFECTION_COMMENT_HISTORY](INFECTION_COMMENT_HISTORY.md) | `INFECTION_ID` | high |
| [INFECTION_INDICATOR](INFECTION_INDICATOR.md) | `INFECTION_ID` | high |
| [INFECTION_ISO_OVERRIDE](INFECTION_ISO_OVERRIDE.md) | `INFECTION_ID` | high |
| [INF_EXPIRATION_CHANGE_HX](INF_EXPIRATION_CHANGE_HX.md) | `INFECTION_ID` | high |
| [SYNDRO_SURV_EVENT_INFS](SYNDRO_SURV_EVENT_INFS.md) | `INFECTION_ID` | high |

