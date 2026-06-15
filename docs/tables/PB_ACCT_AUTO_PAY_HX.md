# PB_ACCT_AUTO_PAY_HX

> The PB_AUTO_PAY_HX table stores the history of auto pay status for a premium billing account.

**Primary key:** `PB_ACCT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTO_PAY_HX_ACT_C_NAME` | VARCHAR |  | Stores the auto pay action performed. |
| 4 | `AUTO_PAY_HX_ACT_SRC_C_NAME` | VARCHAR |  | Stores the source of the auto pay action performed. |
| 5 | `AUTO_PAY_HX_EDIT_TYPE_C_NAME` | VARCHAR |  | When a current auto pay setup is edited, this columns stores the thing that changed. |
| 6 | `AUTO_PAY_HX_MYPT_ID` | VARCHAR |  | Stores the MyChart ID of the member if the auto pay action was performed from MyChart |
| 7 | `AUTO_PAY_HX_ACT_DATE` | DATETIME |  | Stores the date when a particular auto pay workflow was perfomed |
| 8 | `AUTO_PAY_HX_TERM_RSN_C_NAME` | VARCHAR |  | Stores the reason as to why auto pay was terminated |
| 9 | `AUTO_PAY_HX_ACT_TM` | DATETIME (Local) |  | This item stores the time when a particular auto pay workflow was performed |
| 10 | `AUTO_PAY_HX_PMT_MTHD_ID` | NUMERIC |  | Stores the payment method in place when a current auto pay setup is edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

