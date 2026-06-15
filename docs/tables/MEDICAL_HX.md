# MEDICAL_HX

> The MEDICAL_HX table contains data from medical history contacts entered in clinical system patient encounters. Since one patient encounter may contain multiple medical history contacts, each contact is uniquely identified by a patient encounter serial number and a line number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number of the medical history contact within the encounter. Each line of history is stored in enterprise reporting as its own record; a given patient may have multiple records (identified by line number) that reflect multiple lines of history. |
| 2 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 3 | `MEDICAL_HX_DATE` | VARCHAR |  | The free-text date entered in clinical system’s Medical History window for the diagnosis. This field is free-text due to the imprecise nature of patient-provided historical information. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 5 | `MED_HX_ANNOTATION` | VARCHAR |  | This column contains the medical history annotation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

