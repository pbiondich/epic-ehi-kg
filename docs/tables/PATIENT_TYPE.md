# PATIENT_TYPE

> This table contains one record for each patient type for each patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient. This value is encrypted if encryption is enabled. |
| 2 | `LINE` | INTEGER | PK | A patient can be defined with one or many types. This is the line number corresponding to the type for each patient. |
| 3 | `PATIENT_TYPE_C_NAME` | VARCHAR | org | The category value for each patient type entered for the patient (i.e. VIP, Study, etc.) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

