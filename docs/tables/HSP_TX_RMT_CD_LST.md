# HSP_TX_RMT_CD_LST

> This table contains remit code lists from the Hospital Permanent Transactions (HTR) master file.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction with associated remit code lists. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each remittance code list will have its own line. |
| 3 | `RMT_CODE_LIST_ID` | VARCHAR |  | This column stores the unique identifier for the remittance code used for the hospital billing transaction. |
| 4 | `RMT_CODE_LIST_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 5 | `RMT_AMT_LIST` | NUMERIC |  | This column stores the remittance code amount associated with transaction. |
| 6 | `RMT_CODE_EXT` | VARCHAR |  | This column stores the external identifier for the remittance code associated with the hospital billing transaction. |
| 7 | `GRP_CODE_LIST_C_NAME` | VARCHAR | org | This item holds the reason group code associated with the reason code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

