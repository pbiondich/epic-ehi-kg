# PATIENT_ENC_VIDEO_VISIT

> This table contains the video visit related data for a patient that is stored at the patient contact level.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `PAT_ENC_LVL_VIDEO_VISIT_ID` | NUMERIC |  | Contains any patient encounter level video visit that is associated with a given patient encounter. |
| 5 | `TH_MODE_VV_CHG_USER_ID` | VARCHAR |  | Stores the user who switched the telehealth mode of a visit away from a video visit. |
| 6 | `TH_MODE_VV_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VIDEO_VISITS_FOR_ALL_YN` | VARCHAR |  | Denotes that the visit was initiated in a pre-login state. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

