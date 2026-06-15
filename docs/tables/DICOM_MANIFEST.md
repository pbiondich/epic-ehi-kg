# DICOM_MANIFEST

> This table contains a manifest's study level metadata.

**Primary key:** `MANIFEST_ID`  
**Columns:** 5  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MANIFEST_ID` | NUMERIC | PK | The unique identifier (.1 item) for the subject name record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient associated with the DICOM manifest |
| 3 | `STUDY_UID_IDENT` | VARCHAR |  | DICOM Study Instance UID (attribute 0020,000D) |
| 4 | `ACCESSION_NUMBER_IDENT` | VARCHAR |  | The internal accession number of the imaging study. |
| 5 | `MANIFEST_SOURCE_C_NAME` | VARCHAR |  | Source of the manifest record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [DICOM_MANIFEST_CONTACT](DICOM_MANIFEST_CONTACT.md) | `MANIFEST_ID` | high |
| [DICOM_MANIFEST_INSTANCE](DICOM_MANIFEST_INSTANCE.md) | `MANIFEST_ID` | high |
| [DICOM_MANIFEST_SERIES](DICOM_MANIFEST_SERIES.md) | `MANIFEST_ID` | high |

