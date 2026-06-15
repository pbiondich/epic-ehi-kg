# DENTAL_PAT_PHASE

> This table contains information about dental phasing.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `DENT_PAT_PHASE_C_NAME` | VARCHAR |  | The overall dental phase value of the patient. |
| 6 | `DENT_PHASE_MOD_USER_ID` | VARCHAR |  | The user who set the patient phase value. |
| 7 | `DENT_PHASE_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `DENTAL_PHASE_END_DATE` | DATETIME |  | The date a dental phase ended. |
| 9 | `DENTAL_PHASE_START_DATE` | DATETIME |  | The date a dental phase started. |
| 10 | `DENT_PHASE_AUTO_SELECT_FACTORS` | VARCHAR |  | Stores information used to support automatic selection of patient phase. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

