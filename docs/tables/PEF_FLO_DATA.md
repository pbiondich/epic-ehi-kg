# PEF_FLO_DATA

> This table contains data on patient-entered flowsheet component information.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the summary/episode block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSB_PEF_FLO_ID` | VARCHAR |  | This column stores the ID of the patient-entered flowsheet component. |
| 4 | `HSB_PEF_FLO_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 5 | `PEF_MIN_VALUE` | NUMERIC |  | This is the minimum allowable value for the patient-entered flowsheet component. |
| 6 | `PEF_MAX_VALUE` | NUMERIC |  | This is the maximum allowable value for the patient-entered flowsheet component. |
| 7 | `PEF_MIN_VALUE_SECONDARY` | NUMERIC |  | This is secondary minimum value for patient-entered flowsheet components. Can be used to store diastolic min for blood pressure flowsheet row. |
| 8 | `PEF_MAX_VALUE_SECONDARY` | NUMERIC |  | This is secondary maximum value for patient-entered flowsheet components. Can be used to store diastolic max for blood pressure flowsheet row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

