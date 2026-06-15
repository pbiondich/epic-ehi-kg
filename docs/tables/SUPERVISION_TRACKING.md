# SUPERVISION_TRACKING

> This table holds per-user Encounter Supervision information. It tracks the encounter supervising provider info for each user that accesses the encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number of the per-user Encounter Supervision information in the patient's record. Together with PAT_ENC_CSN_ID, this forms the foreign key to the SUPERVISION_TRACKING table. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `SUP_TRACK_USER_ID` | VARCHAR |  | Tracks the user ID as part of Supervision Information tracking. |
| 8 | `SUP_TRACK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `SUP_TRACK_TYPE_C_NAME` | VARCHAR | org | Tracks the Supervision Type as part of Supervision Information tracking. |
| 10 | `SUP_TRACK_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `SUP_INST_UTC_DTTM` | DATETIME (UTC) |  | Tracks the instant that the Supervision Information was set as part of Supervision Information tracking. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

