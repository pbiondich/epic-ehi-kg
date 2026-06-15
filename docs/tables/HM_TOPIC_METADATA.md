# HM_TOPIC_METADATA

> This table contains rows of Health Maintenance topics with metadata values that are calculated for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOPIC_ID` | NUMERIC |  | This column stores Health Maintenance topics that have calculated data that should persist even when the topic no longer applies to the patient. |
| 4 | `TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `EXT_DATA_CHECKSUM` | INTEGER |  | This column indicates whether external data was used to complete the related Health Maintenance topic. |
| 6 | `EXT_CLIN_DATA_DATE` | DATETIME |  | If external clinical data (e.g. Care Everywhere or immunization registries) was used to complete the related Health Maintenance topic, this item will contain the date of the relevant completion. |
| 7 | `EXT_CLAIM_DATE` | DATETIME |  | If external claims data was used to complete the related Health Maintenance topic, this item will contain the date of the relevant completion. |
| 8 | `PT_REPORTED_DATE` | DATETIME |  | If a patient reported action was used to complete the related Health Maintenance topic, this item will contain the date of the relevant completion. |
| 9 | `EXT_HEALTH_PLAN_DATE` | DATETIME |  | If the related HM topic is currently satisfied by external health plan data, this item will contain the date of the relevant completion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

