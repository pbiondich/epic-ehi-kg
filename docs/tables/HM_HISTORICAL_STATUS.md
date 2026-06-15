# HM_HISTORICAL_STATUS

> Records Health Maintenance status over time.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_TOPIC_ID` | NUMERIC | FK→ | The Health Maintenance topic that applied to the patient at the time the snapshot was taken. |
| 4 | `HM_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `HM_STATUS_C_NAME` | VARCHAR |  | Indicates the patient's due status for the Health Maintenance topic at the time the snapshot was taken. |
| 6 | `NEXT_DUE_DATE` | DATETIME |  | The patient's next due date for this Health Maintenance topic at the time the snapshot was taken. |
| 7 | `LAST_COMPLETED_DATE` | DATETIME |  | The date this patient last had a completion for the Health Maintenance topic, as of the time the snapshot was taken. |
| 8 | `HAS_OUTSIDE_COMPLETION_YN` | VARCHAR |  | Indicates whether external data was used to complete the related Health Maintenance topic at the time the snapshot was recorded. |
| 9 | `EXTERNAL_CLINICAL_DATE` | DATETIME |  | If the related HM topic is currently satisfied by external clinical data (e.g. Care Everywhere or immunization registries), this item will contain the date of the relevant completion. |
| 10 | `EXTERNAL_CLAIM_DATE` | DATETIME |  | If the related HM topic is currently satisfied by external claims data, this item will contain the date of the relevant completion. |
| 11 | `PAT_REPORTED_DATE` | DATETIME |  | If the related HM topic is currently satisfied by patient-reported data, this item will contain the date of the relevant patient-reported satisfaction. |
| 12 | `EXTERNAL_HEALTH_PLAN_DATE` | DATETIME |  | If the related HM topic is currently satisfied by external health plan data, this item will contain the date of the relevant completion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HM_TOPIC_ID` | [CLARITY_HM_TOPIC](CLARITY_HM_TOPIC.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

