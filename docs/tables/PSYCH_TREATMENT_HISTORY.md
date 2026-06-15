# PSYCH_TREATMENT_HISTORY

> Historical instance of psychiatric care for a patient.

**Primary key:** `TREATMENT_HX_ID`  
**Columns:** 8  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_HX_ID` | NUMERIC | PK | The unique identifier (.1 item) for the history event record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient for this treatment event. |
| 3 | `TREAT_HX_LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The level of care for a psychiatric treatment history event. For example, inpatient admission. |
| 4 | `START_DATE` | DATETIME |  | The start date of the event. Can be an inexact date. |
| 5 | `DURATION_COUNT` | INTEGER |  | This item along with a duration unit indicates how long the event lasted (e.g., 2 months) |
| 6 | `DURATION_UNIT_C_NAME` | VARCHAR |  | This item along with a duration count indicates how long the event lasted (e.g., 2 months) |
| 7 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `LOCATION_FREE_TEXT` | VARCHAR |  | Free text location where this event occurred. Meant to be used when the location is not built in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [DENTAL_VISIT_INFO_HX](DENTAL_VISIT_INFO_HX.md) | `TREATMENT_HX_ID` | high |
| [PSYCH_HX_EVENT_TAGS](PSYCH_HX_EVENT_TAGS.md) | `TREATMENT_HX_ID` | high |
| [PSYCH_HX_REASON_FOR_TREAT](PSYCH_HX_REASON_FOR_TREAT.md) | `TREATMENT_HX_ID` | high |

