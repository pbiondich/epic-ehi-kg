# V_EHI_NMM_CASE_MGMT_STATIC

> This view supports extracting RTF data for EHI from the case management masterfile.

**Primary key:** `CASE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID assigned to the case record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient linked to the case record. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

