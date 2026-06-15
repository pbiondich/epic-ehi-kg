# VETERAN_CVG_LEVEL

> This table contains information about a veteran patient's coverage levels. This table stores the medical coverage levels associated with a veteran patient and whether a coverage level is the patient's primary. A veteran patient's medical coverage level determines what level of service a patient can receive prior to being billed.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VETERAN_CVG_IS_PRIMARY_YN` | VARCHAR |  | This column denotes whether the related veteran coverage level found in VETERAN_MED_CVG_LEVEL_C on the same LINE is primary. |
| 4 | `VETERAN_MED_CVG_LEVEL_C_NAME` | VARCHAR | org | This related group item holds a list of a patient's medical coverage levels. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

