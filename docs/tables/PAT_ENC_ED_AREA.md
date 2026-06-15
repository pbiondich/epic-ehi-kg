# PAT_ENC_ED_AREA

> The PAT_ENC_ED_AREA table contains a list of the Care Areas a patient was in during their stay in the ED.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this patient encounter. |
| 2 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with these care areas. Care areas typically represent a group of beds, a group of patients, or a unit within the hospital or organization. |
| 3 | `LINE` | INTEGER | PK | The line number of the care area list. Care areas typically represent a group of beds, a group of patients, or a unit within the hospital or organization. |
| 4 | `ED_CARE_AREA_ID_CARE_AREA_NAME` | VARCHAR |  | The name of the Care Area record. Care areas typically represent a group of beds, a group of patients, or a unit within the hospital or organization. |
| 5 | `ED_AREA_TIME` | DATETIME (Local) |  | The instant that the patient was placed into this care area. Care areas typically represent a group of beds, a group of patients, or a unit within the hospital or organization. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

