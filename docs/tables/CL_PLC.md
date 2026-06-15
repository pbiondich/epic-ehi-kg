# CL_PLC

> This table extracts the Patient Location (PLC) event tracking information into Clarity. PLC records record information about where a patient was at a certain time. They contain information about where the patient is, when they arrived there, how they got there, and who put them there.

**Primary key:** `LOCATION_EVNT_ID`  
**Columns:** 15  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOCATION_EVNT_ID` | NUMERIC | PK | The unique ID of the patient location event. |
| 2 | `STATUS_C_NAME` | VARCHAR |  | The status of the location event |
| 3 | `CASE_TRACK_EVENT_C_NAME` | VARCHAR | org | Surgical case tracking event |
| 4 | `PRE_CANCEL_STS_C_NAME` | VARCHAR |  | Holds the status of the record before it was canceled |
| 5 | `PRIVATE_YN` | VARCHAR |  | Flag denoting whether or not the location event is confidential |
| 6 | `SOURCE_ORC_ID` | VARCHAR |  | Source Case ID for the patient location |
| 7 | `SOURCE_ORL_ID` | VARCHAR |  | Source Log ID for the patient location |
| 8 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 10 | `LOCATION_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 11 | `START_TIME` | DATETIME (Local) |  | Confirmed time that a location event occurred |
| 12 | `CANCELED_TIME` | DATETIME (Local) |  | The time the event record was canceled. |
| 13 | `END_TIME` | DATETIME (Local) |  | Completion time for the location event |
| 14 | `COMMENTS` | VARCHAR |  | Free text field for entering comments related to the creation of location event |
| 15 | `EVENT_TYPE_C_NAME` | VARCHAR |  | This item will log how the patient location (PLC) event was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [CL_PLC_ADT_INFO](CL_PLC_ADT_INFO.md) | `LOCATION_EVNT_ID` | high |
| [CL_PLC_AUDIT](CL_PLC_AUDIT.md) | `LOCATION_EVNT_ID` | high |
| [CL_PLC_ORD_INFO](CL_PLC_ORD_INFO.md) | `LOCATION_EVNT_ID` | high |

