# HSP_ACCT_CA_FLG_HX

> This table stores the coding and abstracting flags that have been added to or removed from the hospital accounts.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CA_FLAG_HX_C_NAME` | VARCHAR | org | This item lists the C&A Flags that have been added to or removed from the hospital account. |
| 4 | `CA_FLAG_HX_A_USR_YN` | VARCHAR |  | This item indicates whether the C&A Flag was added by a user or by the system. |
| 5 | `CA_FLAG_HX_A_INST` | DATETIME (Local) |  | This item indicates when the Coding and Abstracting (C&A) Flag was added. |
| 6 | `CA_FLAG_HX_A_EMP_ID` | VARCHAR |  | The user who added this C&A flag |
| 7 | `CA_FLAG_HX_A_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CA_FLAG_HX_A_CMT` | VARCHAR |  | A comment specified when the C&A Flag was added. |
| 9 | `CA_FLAG_HX_R_USR_YN` | VARCHAR |  | This item indicates whether the C&A Flag was removed by a user or by the system. |
| 10 | `CA_FLAG_HX_R_INST` | DATETIME (Local) |  | This item indicates when the Coding and Abstracting (C&A) Flag was removed. |
| 11 | `CA_FLAG_HX_R_EMP_ID` | VARCHAR |  | The user who removed this C&A flag |
| 12 | `CA_FLAG_HX_R_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `CA_FLAG_HX_R_CMT` | VARCHAR |  | A comment specified when the C&A Flag was removed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

