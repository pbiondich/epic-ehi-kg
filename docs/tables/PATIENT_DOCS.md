# PATIENT_DOCS

> The PATIENT_DOCS table contains information about each document that is attached to a patient record, including scanned and electronically signed documents.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The unique ID of the patient with this document. |
| 3 | `DOC_INFO_ID` | VARCHAR | FK→ | The ID of the document for this patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

