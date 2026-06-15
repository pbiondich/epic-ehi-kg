# RDSR_DERIVED_DOSE

> Each row in this table will list a type of radiation dose and its value derived from the Modality Performed Procedure Step (MPPS) or Radiation Dose Structured Reporting (RDSR) message. Derived means that it could have been calculated or directly received in the MPPS or RDSR message.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier of the service-object pair (a particular kind of DICOM message) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RDSR_DOSE_TYPE_C_NAME` | VARCHAR | org | The radiation type category ID for the derived dose. |
| 4 | `RDSR_DERIVED_DOSE` | NUMERIC |  | The derived dose, which is either a calculated value or a value received in the Radiation Dose Structured Report (RDSR). |
| 5 | `RDSR_DOSE_UNIT_C_NAME` | VARCHAR | org | The unit category ID for the derived dose. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

