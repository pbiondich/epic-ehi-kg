# IDENTITY_POC_ID

> This table contains the system Master Person Index ID numbers for your Plan of Care. Each Plan of Care may have multiple Master Person Index IDs. A line number is used to identify each identification number for a Plan of Care.

**Primary key:** `POC_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | The unique ID of the ID type of the Master Patient Index (MPI) identifier. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | The unique ID of the Master Patient Index (MPI) identifier. |
| 6 | `MPI_FROM_DATE` | DATETIME |  | The date the Master Patient Index (MPI) identifier is effective from. |
| 7 | `MPI_TO_DATE` | DATETIME |  | The date the Master Patient Index (MPI) identifier is effective until. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

