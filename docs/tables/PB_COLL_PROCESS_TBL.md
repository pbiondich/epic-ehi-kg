# PB_COLL_PROCESS_TBL

> The related table for all the collections processes on a PBA.

**Primary key:** `PB_ACCT_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PB_COLL_STAT_C_NAME` | VARCHAR |  | The status of the collections process. Used to determine system behavior. |
| 4 | `PB_COLL_STEP_C_NAME` | VARCHAR | org | The current step of the collections process on the account. |
| 5 | `PB_IN_COLL_SINCE_DATE` | DATETIME |  | Represents the date on which this instance entered the collections process. |
| 6 | `COLL_PROCESS_NUM` | INTEGER |  | The unique ID for the collection process on the account. |
| 7 | `PB_IN_STAT_SINCE_DATE` | DATETIME |  | Represents the date in which this instance entered the current status of the collections process. |
| 8 | `PB_IN_STEP_SINCE_DATE` | DATETIME |  | Represents the date in which this instance entered the current step of the collections process. |
| 9 | `PB_ORIG_AMT_OUTST_N` | NUMERIC |  | Stores the total amount outstanding that was originally added to collections. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

