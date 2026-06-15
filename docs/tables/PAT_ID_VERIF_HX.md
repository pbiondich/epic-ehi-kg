# PAT_ID_VERIF_HX

> Holds historical information related to patient identity verification.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID_VERIF_MTHD_C_NAME` | VARCHAR |  | Holds the method used for identity verification. |
| 4 | `PAT_ID_VERIF_CLIENT` | VARCHAR |  | Holds the auditing client ID used to track integration usage with an identity verification vendor. |
| 5 | `PAT_ID_VERIF_LVL_C_NAME` | VARCHAR |  | Holds the level of identity proofing for identity verification. |
| 6 | `PAT_ID_VERIF_ORG_ID` | NUMERIC |  | Holds the data exchange organization where identity verification took place. |
| 7 | `PAT_ID_VERIF_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 8 | `PAT_ID_VERIF_WKFL_C_NAME` | VARCHAR |  | Holds the workflow where identity verification took place. |
| 9 | `PAT_ID_VERIF_UTC_DTTM` | DATETIME (UTC) |  | Holds the UTC instant when identity verification took place. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

