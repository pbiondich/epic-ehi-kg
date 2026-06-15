# EAR_ID_HX

> This table contains the historic Identity ID information for the guarantor.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this row. Multiple pieces of information can be associated with this row. |
| 3 | `MPI_HX_ID` | VARCHAR |  | The historical IDs for the guarantor. |
| 4 | `MPI_HX_ID_TYPE_ID` | NUMERIC |  | The historic type of ID for the guarantor. |
| 5 | `MPI_HX_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 6 | `MPI_HX_USER_ID` | VARCHAR |  | The historic user who updated the ID for the guarantor. |
| 7 | `MPI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `MPI_HX_AUDIT_TYPE_C_NAME` | VARCHAR |  | The historic type of change for the guarantor ID. |
| 9 | `MPI_HX_NEW_ID` | VARCHAR |  | The historical ID that was added for the guarantor. |
| 10 | `MPI_HX_DOTONE` | VARCHAR |  | The guarantor record ID where the ID change was made. |
| 11 | `MPI_HX_FROM_DATE` | DATETIME |  | The historical effective date for the guarantor ID. |
| 12 | `MPI_HX_TO_DATE` | DATETIME |  | The historical end date for the guarantor ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

