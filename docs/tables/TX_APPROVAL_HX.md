# TX_APPROVAL_HX

> This table will display the approval history for transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APRV_HX_INST_DTTM` | DATETIME (UTC) |  | This column stores the instant that the user worked the hospital temporary transaction before the adjustment was completed. |
| 4 | `APRV_HX_STAT_C_NAME` | VARCHAR |  | The status given to the approval. |
| 5 | `APRV_HX_LVL_C_NAME` | VARCHAR | org | This column stores the status that was on the hospital temporary transaction when a user worked it. |
| 6 | `APRV_HX_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who worked the hospital temporary transaction. |
| 7 | `APRV_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `APRV_HX_CMT` | VARCHAR |  | This column stores the comment entered when approving/rejecting/holding the hospital temporary transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

