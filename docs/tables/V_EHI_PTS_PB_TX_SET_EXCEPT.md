# V_EHI_PTS_PB_TX_SET_EXCEPT

> This view filters out premium billing payment data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_TXSET_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `LINE` | INTEGER | PK | Line counter for the exception on the transaction set. |
| 3 | `EXCEPT_PB_TX_ID` | VARCHAR |  | The unique ID of the premium billing detailed transaction associated with the exception. |
| 4 | `EXCEPT_PMT` | NUMERIC |  | Amount actually paid for the exception. |
| 5 | `EXCEPT_RSN_C_NAME` | VARCHAR | org | Reason for the exception. |
| 6 | `EXCEPT_CMT` | VARCHAR |  | Comment associated with the exception. |
| 7 | `EXCEPT_REM_AMT` | NUMERIC |  | Remaining amount for the exception. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

