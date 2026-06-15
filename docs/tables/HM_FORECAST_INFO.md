# HM_FORECAST_INFO

> Health Maintenance forecast information for the next completion.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_FORECAST_TOPIC_ID` | NUMERIC |  | This column stores a Health Maintenance topic that has forecast information. |
| 4 | `HM_FORECAST_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `EARLIEST_VALID_DATE` | DATETIME |  | This column stores the earliest date that the current completion will be considered valid. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

