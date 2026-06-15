# RADIOTHERAPY_RECORD_INFO

> This table contains no add summary information for External Radiation Therapy Treatment Data records.

**Primary key:** `RT_SUMMARY_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 4 | `RECORD_NAME` | VARCHAR |  | Record name |
| 5 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 6 | `PAT_ID` | VARCHAR | FK→ | Stores the patient being treated or planned to be treated by the radiotherapy summary. |
| 7 | `RADIOTHERAPY_TYPE_C_NAME` | VARCHAR |  | Stores the type of the record. |
| 8 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 9 | `LINKED_EPISODE_ID` | NUMERIC |  | Virtual item containing the ID of the episode (HSB) that contains the radiotherapy course summary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

