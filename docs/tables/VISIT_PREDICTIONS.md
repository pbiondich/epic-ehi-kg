# VISIT_PREDICTIONS

> The VISIT_PREDICTIONS table contains information about when and where in the hospital a patient is expected to be during their visit. This will currently only include projections used for OR throughput.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `EXPECTED_PAT_LOC_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 4 | `EXPECTED_REASON_C_NAME` | VARCHAR | org | The reason for the patient's expected stay in this location. |
| 5 | `EXPECTED_START_DTTM` | DATETIME (Local) |  | The instant at which the patient is expected to arrive in this location. |
| 6 | `EXPECTED_DURATION` | NUMERIC |  | The amount of time (in minutes) a patient is expected to stay in this location. |
| 7 | `PREDICTION_SRC_FEV_ID` | VARCHAR |  | The unique ID of the event that created this prediction. |
| 8 | `PREDICTION_SRC_FEV_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 9 | `PREDICTION_SRC_PND_ID` | VARCHAR |  | The unique ID of the pending record that created this prediction. |
| 10 | `PREDICTION_DTTM` | DATETIME (UTC) |  | The instant at which this prediction was made. |
| 11 | `PREDICTION_CAUSE_C_NAME` | VARCHAR |  | The reason or event that triggered this prediction to be made. |
| 12 | `ACTIVE_PRED_YN` | VARCHAR |  | Indicates whether this prediction is the most current. |
| 13 | `UPDATED_BY_USER_ID` | VARCHAR |  | The unique ID of the user who manually entered this prediction. |
| 14 | `UPDATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

