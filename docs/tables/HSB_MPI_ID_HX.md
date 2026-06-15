# HSB_MPI_ID_HX

> This table includes Identity ID history information for the Episode (HSB) master file.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for this related response group. |
| 3 | `MPI_HX_ID` | VARCHAR |  | The historical MPI ID of the corresponding historical MPI ID type for the record. |
| 4 | `MPI_HX_INSTANT` | DATETIME (Attached) |  | The date and time the MPI ID was placed on the record's historical ID table. |
| 5 | `MPI_HX_ID_TYPE` | NUMERIC |  | The MPI ID type of the historical MPI ID linked to the record. |
| 6 | `MPI_HX_ID_TYPE_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 7 | `MPI_HX_USER_ID` | VARCHAR |  | The user that performed the audit action on the historical MPI ID. |
| 8 | `MPI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `MPI_HX_AUDIT_TYPE_C_NAME` | VARCHAR |  | The action the user performed on the historical MPI ID. |
| 10 | `MPI_HX_NEW_ID` | VARCHAR |  | The new MPI ID that was added to the record. |
| 11 | `MPI_HX_DOTONE` | VARCHAR |  | The internal ID of the record when the user performed the action. |
| 12 | `MPI_HX_FROM_DATE` | DATETIME |  | The effective from date of the historical MPI ID on the record. |
| 13 | `MPI_HX_TO_DATE` | DATETIME |  | The effective to date of the historical MPI ID on the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

