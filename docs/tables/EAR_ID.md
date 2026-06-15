# EAR_ID

> This table contains the Identity IDs assigned to the guarantor record.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this row. Multiple pieces of information can be associated with this row. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | ID type for guarantor IDs. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | Guarantor ID |
| 6 | `MPI_FROM_DATE` | DATETIME |  | Date the ID is effective from for the guarantor. |
| 7 | `MPI_TO_DATE` | DATETIME |  | Date the ID is effective to for the guarantor. |
| 8 | `MPI_RET_CHK_PP_ID` | NUMERIC |  | Stores the code used to assign a National Provider ID. |
| 9 | `MPI_RET_CHK_PP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 10 | `MPI_RET_CHK_RULE_ID` | VARCHAR |  | Stores the rule used to assign a National Provider ID |
| 11 | `MPI_RET_CHK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

