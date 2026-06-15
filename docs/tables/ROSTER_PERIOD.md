# ROSTER_PERIOD

> Compiled roster tracking eligibility periods for each roster ID.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ROSTER_IDNT_C_NAME` | VARCHAR | org | The identifier of the roster file that included this patient. |
| 4 | `RSTR_PER_EFF_DATE` | DATETIME |  | The effective date of the roster period. |
| 5 | `RSTR_PER_TERM_DATE` | DATETIME |  | The termination date of the roster period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

