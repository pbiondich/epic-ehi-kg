# RQG_MPI_HX

> The RQG_MPI_HX table contains MPI ID history information for the Requisition Grouper (RQG) master file.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition grouper record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_HX_ID` | VARCHAR |  | The Identity ID history for this record. |
| 4 | `MPI_HX_ID_TYPE_ID` | NUMERIC |  | The changes to the ID type. This column is frequently used to link to the IDENTITY_ID_TYPE table. |
| 5 | `MPI_HX_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 6 | `MPI_HX_NEW_ID` | VARCHAR |  | The new Identity ID for this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

