# IMMNZTN_LAST_REVIEW

> The table holds the information about when and by whom the immunizations section has been reviewed.

**Primary key:** `PAT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `IMM_LST_REV_INST_DTTM` | DATETIME (Local) |  | This item store the last instant when the immunization record is marked as reviewed. |
| 3 | `IMM_LST_REV_USER_ID` | VARCHAR |  | This item stores the last user who marked the immunizations history as reviewed. |
| 4 | `IMM_LST_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `IMM_LST_REV_CSN_ID` | NUMERIC |  | CSN of encounter during the last time the immunizations were reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

