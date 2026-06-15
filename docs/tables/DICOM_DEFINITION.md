# DICOM_DEFINITION

> This table stores single response data that is not tracked overtime for the DICOM Definition (FDD) masterfile. This includes AE Title/modality build.

**Primary key:** `DEFINITION_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DEFINITION_ID` | NUMERIC | PK | The unique identifier (.1 item) for the record record. |
| 2 | `DICOM_NAME` | VARCHAR |  | The name of an Application Entity (modality). This is not the AE Title. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

