# ALLERGY_FLAG

> This table holds data of whether the patient's allergies were marked as containing no drug allergies.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALRGY_FLAG_YN` | VARCHAR |  | This column stores a "Y" if the patient's "No Known Allergies" checkbox is selected and an "N" if the checkbox is not selected. |
| 4 | `ALRGY_FLG_UPD_BY_ID` | VARCHAR |  | This item stores the user who updated the patient's No Known Allergies status. |
| 5 | `ALRGY_FLG_UPD_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ALRGY_FLAG_UPD_DTTM` | DATETIME (UTC) |  | This item stores the instant of update for when the patient's No Known Allergies status is changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

