# TEETH_REVIEWED

> This table contains information about when a patient's teeth were first reviewed.

**Primary key:** `PAT_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `TEETH_REV_DTTM` | DATETIME (Local) |  | The date and time that the patient's teeth were first reviewed during the Add / Remove Teeth functionality in the Tooth Chart activity. |
| 3 | `TEETH_REV_USER` | VARCHAR |  | The user who first reviewed the patient's teeth using the Add/Remove Teeth functionality from within the Tooth Chart activity. |
| 4 | `TEETH_REV_USER_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

