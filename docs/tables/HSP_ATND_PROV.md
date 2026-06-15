# HSP_ATND_PROV

> The HSP_ATND_PROV table contains information on inpatient or outpatient attending providers. This table is based on PAT_ENC_CSN_ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number of the attending provider for the patient. |
| 2 | `ATTEND_FROM_DATE` | DATETIME (Local) |  | The date and time the attending provider started for the patient. Can be assigned for both hospital encounters and outpatient visits. Dates are not guaranteed to be filled in. If dates are empty, this range is assumed to be open-ended. Date/time range only applies to this encounter. Checking relevant encounter dates should be done in addition to these dates to get the whole picture for an encounter. |
| 3 | `ATTEND_TO_DATE` | DATETIME (Local) |  | The date and time the attending provider ended for the patient. Can be assigned for both hospital encounters and outpatient visits. Dates are not guaranteed to be filled in. If dates are empty, this range is assumed to be open-ended. Date/time range only applies to this encounter. Checking relevant encounter dates should be done in addition to these dates to get the whole picture for an encounter. |
| 4 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ED_ATTEND_YN` | VARCHAR |  | Indicates whether or not this physician was an attending in the ED. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

