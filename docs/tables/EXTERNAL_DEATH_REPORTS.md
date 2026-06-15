# EXTERNAL_DEATH_REPORTS

> External reports of patient death information.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_DEATH_STAT_C_NAME` | VARCHAR |  | Stores the current status of a given external report on a patient's death. |
| 4 | `EXT_DEATH_DATE` | DATETIME |  | Stores the reported date of death of a given external report on a patient's death. |
| 5 | `EXT_DEATH_SOURCE_C_NAME` | VARCHAR | org | Stores the source of a given external report on a patient's death. |
| 6 | `EXT_DEATH_COMMENT` | VARCHAR |  | Stores an optional comment of a given external report on a patient's death. |
| 7 | `EXT_DEATH_ORG_ID` | NUMERIC |  | This item holds the DXO ID of the external organization that has reported this deceased information. |
| 8 | `EXT_DEATH_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

