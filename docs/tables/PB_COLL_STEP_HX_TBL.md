# PB_COLL_STEP_HX_TBL

> This table contains information about the history of all collection activity on a PBA. This includes when steps are completed, when collections balances are written or paid off, and the amount of money outstanding in collections.

**Primary key:** `PB_ACCT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PB_COLL_STEP_C_NAME` | VARCHAR | org | Stores the history of the collections step on the account. |
| 4 | `PB_MOD_HX_DATE` | DATETIME |  | Stores the history of when the collections step was modified on the account. |
| 5 | `PB_AMT_OUTST_HX` | NUMERIC |  | Stores the history of the amount outstanding from transactions that are in collections. |
| 6 | `PB_COLL_STEP_NUM` | INTEGER |  | The unique ID for the collection process on the account. |
| 7 | `WHO_COMP_STEP_HX_USER_ID` | VARCHAR |  | Stores the history of the user that completed each step in a collections process. |
| 8 | `WHO_COMP_STEP_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `WAS_STEP_SKIP_YN` | VARCHAR |  | Indicates whether this step of the collection process was manually skipped. |
| 10 | `PB_COLL_STAT_C_NAME` | VARCHAR |  | Stores the history of the collections status on the account. |
| 11 | `COLL_PHONE_CALL_COMM_ID` | NUMERIC |  | Stores the history of any CRM cases that were opened in each step of a collections process. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

