# IDENTITY_POC_ID_HX

> This table contains the system Master Person Index ID history for your Plan of Care. Each Plan of Care may have multiple Master Person Index IDs. A line number is used to identify each identification number for a Plan of Care.

**Primary key:** `POC_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_HX` | VARCHAR |  | The unique ID of the Master Patient Index (MPI) identifier before an audit event occurred. |
| 4 | `MPI_HX_INSTANT_DTTM` | DATETIME (Attached) |  | The instant at which the audit event was logged for the identifier. |
| 5 | `MPI_HX_ID_TYPE_ID` | NUMERIC |  | The unique ID of the ID type of the Master Patient Index (MPI) identifier. |
| 6 | `MPI_HX_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 7 | `MPI_HX_USER_ID` | VARCHAR |  | The unique ID of the user that triggered an audit event for the Master Patient Index (MPI) identifier. |
| 8 | `MPI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `MPI_HX_AUDIT_TYPE_C_NAME` | VARCHAR |  | The audit event category ID for the plan of care that updated the identifier. |
| 10 | `MPI_HX_NEW_ID` | VARCHAR |  | The unique ID of the Master Patient Index (MPI) identifier after an audit event has occurred. |
| 11 | `MPI_HX_DOTONE` | VARCHAR |  | The internal Chronicles ID of the record for which this audit event was logged. |
| 12 | `MPI_HX_FROM_DATE` | DATETIME |  | The date the Master Patient Index (MPI) identifier is or was effective from. |
| 13 | `MPI_HX_TO_DATE` | DATETIME |  | The date the Master Patient Index (MPI) identifier is or was effective until. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

