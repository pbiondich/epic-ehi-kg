# ROSTER_FILE_PERIOD

> Contains a list of changes to a patient's roster status over time. The current values are also stored in the ROSTER_PERIOD table.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ROSTER_IDENTIFIER_C_NAME` | VARCHAR | org | The identifier of the roster file that included this patient. |
| 4 | `ROSTER_START_DATE` | DATETIME |  | The effective date of the roster period as indicated by the roster file. |
| 5 | `ROSTER_TERM_DATE` | DATETIME |  | The termination date of the roster period as indicated by the roster file. |
| 6 | `ROSTER_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this roster line was added/updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

