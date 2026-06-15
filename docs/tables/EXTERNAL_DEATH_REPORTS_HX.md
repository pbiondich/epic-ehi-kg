# EXTERNAL_DEATH_REPORTS_HX

> Stores audit trail data for updates to external death status.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_DEATH_HX_LINE` | INTEGER |  | Stores the link to the relevant line in EPT-85500 that this row is referring to. |
| 4 | `EXT_DEATH_STAT_HX_C_NAME` | VARCHAR |  | Stores the status that a given report was updated to. |
| 5 | `EXT_DEATH_USER_ID` | VARCHAR |  | Stores the user who was responsible for updating the external death status of a given report. |
| 6 | `EXT_DEATH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EXT_DEATH_UPD_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant at which a user updated the external death status of a given report. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

