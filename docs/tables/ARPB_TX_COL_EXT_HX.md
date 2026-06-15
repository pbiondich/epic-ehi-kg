# ARPB_TX_COL_EXT_HX

> Contains the collections agency extract history.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_HX_AGENCY_ID` | NUMERIC |  | The unique ID of the collection agency record. |
| 4 | `EXT_HX_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 5 | `EXT_HX_ACTIVITY_C_NAME` | VARCHAR |  | Collection agency extract insurance amount |
| 6 | `EXT_HX_ACT_DATE` | DATETIME |  | Collection agency extract activity date |
| 7 | `EXT_HX_PAT_AMT` | NUMERIC |  | Collection agency extract patient amount. |
| 8 | `EXT_HX_INS_AMT` | NUMERIC |  | Collection agency extract insurance amount. |
| 9 | `EXT_HX_USER_ID` | VARCHAR |  | The collection agency extract user ID for the transaction record. |
| 10 | `EXT_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `EXT_HX_COMMENT` | VARCHAR |  | Collection agency extract comment. |
| 12 | `EXT_HX_PMT_AMT` | NUMERIC |  | Stores the amount of a payment collected by the collection agency extract framework |
| 13 | `EXT_HX_RET_REASON_C_NAME` | VARCHAR | org | Stores the reason for the agency returning a transaction in the agency extract framework. |
| 14 | `EXT_HX_ACCT_INST_UTC_DTTM` | DATETIME (UTC) |  | The extract activity instant. This value is stored as a UTC instant |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

