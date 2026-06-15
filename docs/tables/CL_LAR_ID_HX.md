# CL_LAR_ID_HX

> This contains the Master Patient Index (MPI) historical ID table items for Research Study Enrollment Information records.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_HX_ID` | VARCHAR |  | This item is the count of historical IDs attached to the record. |
| 4 | `MPI_HX_INSTANT_DTTM` | DATETIME (Attached) |  | This item is the instant at which the IAT audit event record was last changed for the related historical ID. |
| 5 | `MPI_HX_ID_TYPE_ID` | NUMERIC |  | This item is the ID Type/IIT record of the related historical ID. |
| 6 | `MPI_HX_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 7 | `MPI_HX_USER_ID` | VARCHAR |  | This item is the user record ID that triggered the ID change of the related historical ID. |
| 8 | `MPI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `MPI_HX_AUDIT_TYPE_C_NAME` | VARCHAR |  | The audit type of the related historical ID (new, modified, merge, unmerge). |
| 10 | `MPI_HX_NEW_ID` | VARCHAR |  | This item is the historical ID resulting from the ID change. |
| 11 | `MPI_HX_DOTONE` | VARCHAR |  | The unique ID of the MPI-enabled research study record. |
| 12 | `MPI_HX_FROM_DATE` | DATETIME |  | This item is the historical "Effective From" date for the related historical ID. |
| 13 | `MPI_HX_TO_DATE` | DATETIME |  | This item is the historical "Effective To" date for the related historical ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

