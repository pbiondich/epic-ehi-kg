# CASE_RPT_ABSTNS

> This table contains information about reportable case abstractions.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 15  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CASE_RPT_AGENCY_C_NAME` | VARCHAR | org | The reporting agency category ID for the reportable case abstraction. |
| 3 | `CASE_RPT_TYPE_C_NAME` | VARCHAR | org | The report type category ID for the reportable case abstraction. |
| 4 | `CASE_RPT_COND_ID` | NUMERIC |  | The unique ID of the associated reportable condition (HFR) record. This column is frequently used to link to the REGISTRY_CONFIG table. |
| 5 | `CASE_RPT_COND_ID_REGISTRY_NAME` | VARCHAR |  | The name of the registry record. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the associated patient (EPT) record. This column is frequently used to link to the PATIENT table. |
| 7 | `CUR_STAT_C_NAME` | VARCHAR | org | The current status category ID for the reportable case abstraction. |
| 8 | `CREATION_DATE` | DATETIME |  | The date that the case was created. |
| 9 | `COND_DATE` | DATETIME |  | The date associated with the condition. |
| 10 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The registry type category ID for the reportable case abstraction. |
| 11 | `HOW_CREATED_C_NAME` | VARCHAR |  | The creation method category ID for the reportable case abstraction. |
| 12 | `CASE_NOTE_ID` | VARCHAR |  | The unique ID of the case note associated with the reportable case abstraction. |
| 13 | `HOSPITAL_CENSUS_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant of the hospital census in UTC if the Hospital Census batch created this abstraction row. |
| 14 | `HOSPITAL_CENSUS_DTTM` | DATETIME (Attached) |  | Stores the instant of the hospital census in local time if the Hospital Census batch created this abstraction. |
| 15 | `ASSOC_RFV_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

