# MEDICAL_READINESS_HX

> This table stores historical medical readiness information for a patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `HX_MED_READINESS_DTTM` | DATETIME (Local) |  | The medical readiness date and time for this patient encounter. This date and time may be expected or confirmed, depending on whether the patient is medically ready or not. |
| 7 | `HX_MED_READINESS_TIMEFRAM_C_NAME` | VARCHAR |  | The medical readiness timeframe category ID for the patient encounter |
| 8 | `HX_MED_READINESS_YN` | VARCHAR |  | Indicates whether this patient encounter is medically ready for discharge. 'Y' indicates that this encounter has been marked medically ready for discharge. 'N' or NULL indicates that it has not been marked medically ready for discharge. |
| 9 | `HX_MED_READY_INST_ENTRY_DTTM` | DATETIME (UTC) |  | The instant at which this patient's medical readiness information was last updated |
| 10 | `HX_MED_READINESS_USER_ID` | VARCHAR |  | The unique ID of the user who last updated medical readiness information for this patient encounter |
| 11 | `HX_MED_READINESS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `HX_MED_READINESS_SOURCE_C_NAME` | VARCHAR |  | The medical readiness source category ID for this patient encounter |
| 13 | `HX_MED_READY_ENTRY_LOCAL_DTTM` | DATETIME (Local) |  | The instant at which this patient's medical readiness information was updated in their local time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

