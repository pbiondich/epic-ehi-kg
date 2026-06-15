# HSP_ACCT_CONS_SP_STS_HX

> Consolidated balances status history.

**Primary key:** `HSP_ACCT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the account's consolidated balances status changed. |
| 4 | `CHANGE_TYPE_C_NAME` | VARCHAR |  | Stores the type of the consolidated balances status change. |
| 5 | `USER_ID` | VARCHAR | FK→ | Stores the user behind the consolidated balances status change. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `WITHDRAWAL_REASON_C_NAME` | VARCHAR | org | Stores the reason the account was withdrawn. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

