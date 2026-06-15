# HSB_MPI_ID

> This table includes Identity ID information for the Episode (HSB) master file.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The ID of the Summary Block record. |
| 2 | `LINE` | INTEGER | PK | The line number of the related response item. |
| 3 | `MPI_ID_TYPE` | NUMERIC |  | This item stores the MPI ID Type of the ID found in the MPI_ID column. |
| 4 | `MPI_ID_TYPE_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | The MPI ID associated with the MPI ID type found in the MPI_ID_TYPE column of this summary block record. |
| 6 | `MPI_FROM_DATE` | DATETIME |  | This column contains the first date on which the Identity ID became effective. |
| 7 | `MPI_TO_DATE` | DATETIME |  | This column contains the date on which the Identity ID will no longer be effective. |
| 8 | `MPI_RET_CHK_PP_ID` | NUMERIC |  | This column contains the ID of the retrieval check programming point. |
| 9 | `MPI_RET_CHK_PP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 10 | `MPI_RET_CHK_RULE_ID` | VARCHAR |  | This column contains the retrieval check rule. |
| 11 | `MPI_RET_CHK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

