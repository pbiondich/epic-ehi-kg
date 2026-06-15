# CL_LAR_ID

> This contains the Master Patient Index (MPI) ID table items for Research Study Enrollment Information records.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | The ID type for this research study's Master Patient Index (MPI) ID. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | The external Master patient Index (MPI) ID for this research study. |
| 6 | `MPI_FROM_DATE` | DATETIME |  | Date the ID is effective from for the research study. |
| 7 | `MPI_TO_DATE` | DATETIME |  | Date the ID is effective to for the research study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

