# THRESHOLD_INFO

> Threshold general information including common name and patient ID.

**Primary key:** `RECORD_ID`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the patient threshold record. |
| 2 | `COMMON_NAME` | VARCHAR |  | Common name of the component the reference ranges applies to. |
| 3 | `PATIENT_ID` | VARCHAR |  | The unique identifier (ID) of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `LAB_C_NAME` | VARCHAR | org | The lab category associated with the threshold. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

