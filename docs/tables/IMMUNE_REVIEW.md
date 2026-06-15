# IMMUNE_REVIEW

> The table holds the information concerning when and by whom the immunizations section has been reviewed.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMM_REV_HX_DTTM` | DATETIME (Local) |  | This item stores the instant when a user marks the immunization as reviewed. |
| 4 | `IMM_REV_HX_USR_ID` | VARCHAR |  | This item stores the user who marks the immunization record as reviewed. |
| 5 | `IMM_REV_HX_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `IMM_REV_HX_CSN` | NUMERIC |  | CSN of encounter where immunizations were last reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

