# RDSR_DOSE_SOURCE

> Each row in this table will describe a source of dose Information.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier of the service-object pair (a particular kind of DICOM message) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RDSR_DOSE_SOURCE_C_NAME` | VARCHAR | org | The source category ID for the source of the dose information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

