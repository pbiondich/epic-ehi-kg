# PAT_MCARE_HEALTH_STATUS

> This table stores the Medicare health status flags for a member.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MCARE_HEALTH_STATUS_C_NAME` | VARCHAR |  | Stores the category number for a Health Status Flag. A health status flag is an indicator that comes from CMS for Medicare Advantage members. |
| 4 | `START_DATE` | DATETIME |  | Stores the start date of the corresponding health status flag. |
| 5 | `END_DATE` | DATETIME |  | Stores the end date of the corresponding health status flag. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

