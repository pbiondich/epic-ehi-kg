# APPT_LENGTH_OVERRIDE

> This table contains information about why an appointment's length was different than its scheduled length.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `OVERRIDE_LENGTH` | INTEGER |  | If the scheduled length of an appointment is not the expected length, enter the expected length here. This does not change the length of the appointment but does visually change how long the appointment is in the Rooming view of the Visit Assignment Wizard. |
| 7 | `APPT_LEN_OVRD_REASON_C_NAME` | VARCHAR | org | The reason for changing the expected length of an appointment. |
| 8 | `OVERRIDE_COMMENT` | VARCHAR |  | A comment about overriding an appointment's expected length. |
| 9 | `OVERRIDE_USER_ID` | VARCHAR |  | The user who changed the expected length of the appointment. |
| 10 | `OVERRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `OVERRIDE_INSTANT_DTTM` | DATETIME (Attached) |  | The time when the expected length of the appointment was set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

