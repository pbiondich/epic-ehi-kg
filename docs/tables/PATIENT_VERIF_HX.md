# PATIENT_VERIF_HX

> When the verification status of a patient is changed the previous and new verification information is stored in this group of items.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VERIF_HX_PRE_STAT_C_NAME` | VARCHAR | org | When verification status changes stores previous value |
| 4 | `VERIF_HX_NEW_STAT_C_NAME` | VARCHAR |  | When verification status changes stores new value |
| 5 | `VERIF_HX_USER_ID` | VARCHAR |  | When verification status changes stores ID of user making change |
| 6 | `VERIF_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VERIF_HX_CHNG_DT` | DATETIME |  | When verification status changes stores date of change |
| 8 | `VERIF_HX_NXT_REV_DT` | DATETIME |  | When verification status changes stores calculated next review date |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

